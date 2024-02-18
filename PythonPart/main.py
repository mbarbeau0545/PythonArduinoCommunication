#################################################################################
#  @file       main.py
#  @brief       Script Python to control every Arduino Card (with the right software)
#  @details     
#              In order to exchange data between Python and the Arduino,
#              A protocol has been made to do so.\n
#         
# 
#                          |-------|------------------------|
#                          | Octet |       Description      |
#                          |-------|------------------------|
#                          |   0   | Start Byte(char(0))    |
#                          |-------|------------------------|
#                          |   1   | Check Sum              |
#                          |-------|------------------------|
#                          |   2   | Signal Type            |
#                          |-------|------------------------|
#                          |   3   | Function to use        |
#                          |-------|------------------------|
#                          |   4   | Pin Number             |
#                          |-------|------------------------|
#                          |   5   | Value                  | 
#                          |-------|------------------------|
#                          |   6   | None                   |
#                          |-------|------------------------|
#                          |   7   | End Byte(10)           |
#                          |-------|------------------------|
# 
#               Python send 8 bytes of data as shown above, to indicate 
#               Which function has to be used and wich pin is concerned 
#               We also send the value assigned to the dedicate pin 
#
#
#  @author      AUDMBA
#  @date        10/02/2024
#  @version     1.0
################################################################################
#                                       IMPORT
################################################################################
from ModuleLog.ModuleLog import*
from TypeCommon import*
from Config_Pyduino_Com import*
import serial 
from array import array
import sys
import time
################################################################################
#                                       Constants
################################################################################
# Max time waiting for read or write msg on serial communication
MAX_TIME_WAITING = 2000
#Arduino Parameter
ARDUINO_CART_USE = PYDUINO_ARDUINO_UNO_R3
COMMUNICATION_PORT = "COM5"
COMMUNICATION_SPEED = 9600
TIMEOUT_DELAY = 0x03
g_MaxAnaPin_ua = [
     (0x00),
    UNO_R3_ANA_NB,
     (0x00),
     (0x00),
     (0x00),
     (0x00),
     (0x00),
    UNO_MEGA_2560_ANA_NB,
]
g_MaxDigPin_ua = [
     (0x00),
    UNO_R3_DIG_NB,
     (0x00),
     (0x00),
     (0x00),
     (0x00),
     (0x00),
    UNO_MEGA_2560_DIG_NB,
]
# max number of byte we can send
PYDUINO_DATA_BYTES_NB_SEND_DATA     =  (0x08)
START_BYTE_SEND_DATA =  (0xFE)
END_BYTE_SEND_DATA   =  (0xFF)

# Fisrt command for Arduino to start communication 
g_CommandArduino_StartCom_ua = [
    START_BYTE_SEND_DATA,
     (0x00),
     (0x00),
     (0x00),
     (0x00),
     (0x00),
     (0x00),
    END_BYTE_SEND_DATA,
]
#Cmd c=should be receiving by arduino to complete communication
ARDUINO_START_MSG = "Start communication statut : ok"

# Fisrt command for Arduino to start communication 
g_CommandArduino_EndCom_ua = [
    START_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
    END_BYTE_SEND_DATA,
]
# Last command for Arduino to end communication
#-------------------------------------------
# Structure for sending Command to arduino
#-------------------------------------------
PYDUINO_DATA_INDEX_START_BYTE           =  (0x00)  # First byte, message arrived 
PYDUINO_DATA_INDEX_CHECKSUM_BYTE        =  (0x01)  # Checksum byte
PYDUINO_DATA_INDEX_SIGNAL_TYPE_BYTE     =  (0x02)  # Which t_ePyduino_PinType is concernced
PYDUINO_DATA_INDEX_FUNCTION_BYTE        =  (0x03)  # Which t_ePyduino_Function is concerned
PYDUINO_DATA_INDEX_PIN_NUMBER_BYTE      =  (0x04)  # Whihc pin is concerned
PYDUINO_DATA_INDEX_ASSIGN_VALUE_BYTE    =  (0x05)  # Value to make
PYDUINO_DATA_INDEX_NONE_BYTE2           =  (0x06)  # To define has to be 0xOO in this case
PYDUINO_DATA_INDEX_ENDING_BYTE          =  (0x07)  # End byte, message is finished 



################################################################################
#                                       Variable
################################################################################
g_CommandArduinoLED_ON_ua = [
    START_BYTE_SEND_DATA,                            # First byte, message arrived        
     (0x00),                                          # Checksum byte
    PYDUINO_SIGNAL_DIGITAL,                            # Which t_ePyduino_PinType is concernced
    PYDUINO_FUNCTION_DIGITAL_WRITE,                  # Which t_ePyduino_Function is concerned
    UNO_R3_DIG__D5,                                  # Whihc pin is concerned
    3,                                            # Value
    (0x00),                                          # To define has to be 0xOO in this case
    END_BYTE_SEND_DATA                               # End byte, message is finished 
]
g_CommandArduinoLED_OFF_ua = [
    START_BYTE_SEND_DATA,
     (0x00),
    PYDUINO_SIGNAL_DIGITAL,
    PYDUINO_FUNCTION_DIGITAL_WRITE,
    UNO_R3_DIG__D5,
    PYDUINO_ASSIGN_VALUE_LOW,
    (0x00),
    END_BYTE_SEND_DATA
]
################################################################################
#                                       CLASS
################################################################################

#----------------------
# ArduinoCommunication
#----------------------
class ArduinoCommunication():
    #----------------------
    # __init__
    #----------------------
    def __init__(self, f_Communication_port_str:str, f_CommuniationSpeed_ui:int, f_TimeOut_Delay_ui:int):
        self.moduleIntialize_b  = bool(False)
        self.serieCom = serial.Serial()
        RC = t_eReturnCode()
        Ret_e= RC.OK
        if(isinstance(f_Communication_port_str,str) != bool(True)
        and isinstance(f_CommuniationSpeed_ui,int)  != bool(True)
        and  isinstance(f_CommuniationSpeed_ui,int) != bool(True) ):
            Ret_e = RC.ERROR_PARAM_INVALID
            raise Exception("ArduinoCommunication_init : Parmater are invalid")
        if(Ret_e == RC.OK):
            self.serieCom.port = f_Communication_port_str
            self.serieCom.baudrate = f_CommuniationSpeed_ui
            self.serieCom.timeout  = f_TimeOut_Delay_ui
            #generate Output file
            self.makeLog = MngLogFile("Log","Pyduino_file.log",log.DEBUG, "Repertory all exchange between Python and the Arduino")
    #----------------------
    # Initialize_ArduinoCom
    #----------------------
    def Initialize_ArduinoCom(self)->t_eReturnCode:
        """
            @brief      Initialize the communication wit hthe Arduino device
            @details      We send a start msg to the Arduino and he has to response Back
                          by sending ARDUINO_START_MSG
            @retval 
                RC.OK                             Communcation between python and Arduino is fully completed\n
                RC.ERROR_WRONG_STATE              Aguments are not valid\n    
                RC.ERROR_NOT_ALLOWED              @copydoc Send_ArduinoCommand()\n
                RC.ERROR_BUSY                     @copydoc Send_ArduinoCommand()\n
        """
        ArduinoStart_msg_str =" "
        counterLoop_ui =  (0)
        RC = t_eReturnCode()
        Ret_e = RC.OK
        if(self.moduleIntialize_b == bool(True)):
            Ret_e = RC.ERROR_WRONG_STATE
            raise Exception("Module Already initialize\n")
        if(Ret_e == RC.OK):
            try:
                self.serieCom.open()
            except:
                Ret_e = RC.ERROR_MODULE_NOT_INITIALIZED
                self.makeLog.LCF_SetMsgLog(log.ERROR, "Cannot open the serial communication Retcode ",Ret_e)
                raise Exception("Initialize_ArduinoCom : Cannot open the serial canal with Arduino")
            #send the Start MSG
        self.makeLog.LCF_SetMsgLog(log.INFO, f"Connection on port {self.serieCom.port} succeed")
        if(Ret_e == RC.OK):
            while(counterLoop_ui <  (MAX_TIME_WAITING) ):
                counterLoop_ui += int(1)
                ArduinoStart_msg_str = self.serieCom.readlines()            
                if(ARDUINO_START_MSG in str(ArduinoStart_msg_str)):
                    self.makeLog.LCF_SetMsgLog(log.INFO, str(ArduinoStart_msg_str))
                    break
            if(counterLoop_ui <  (MAX_TIME_WAITING)):
                self.moduleIntialize_b = bool(True)
                self.makeLog.LCF_SetMsgLog(log.INFO, "Module Pyduino_Cm initialize, RetCode ",Ret_e)

                
            
        return Ret_e
    #------------------------
    # Unintialize_ArduinoCom
    #------------------------
    def Unintialize_ArduinoCom(self)->None:
        """
            @brief      Unitialize the Arduino communication with python
                        close Serial Com
        """
        self.serieCom.close()
        self.moduleIntialize_b = bool(False)
        return
    #------------------------
    # Send_ArduinoCommand
    #------------------------
    def Send_ArduinoCommand(self, f_arduinoCommand_ua)->t_eReturnCode:
        """
            @brief      Send Command to arduino with 8 bytes of data
            @details    We verify each byte from f_arduinoCommand_ua is confirm with
                        what's allow to send then we try to send the msg in Serial Com if 
                        the bus can accept the msg, if he don't we retry 
            
            @param[in] f_arduinoCommand_ua : commend to send on Arduino
            @retval 
                RC.OK                             msg was send\n
                RC.ERROR_NOT_ALLOWED              f_arduinoCommand_ua not as expected\n
                RC.ERROR_BUSY                     msg not send\n
        """
        RC = t_eReturnCode()
        Ret_e= RC.OK
        #verify parameter
        if(isinstance(f_arduinoCommand_ua,list) != bool(True)):
            Ret_e = RC.ERROR_PARAM_INVALID
            raise Exception("Send_ArduinoCommand : param invalid")
        #verify if element in f_arduinoCommand_ua are ok
        if(Ret_e == RC.OK):
            if( f_arduinoCommand_ua[PYDUINO_DATA_INDEX_START_BYTE]            == START_BYTE_SEND_DATA
            and f_arduinoCommand_ua[PYDUINO_DATA_INDEX_ENDING_BYTE]           == END_BYTE_SEND_DATA
            and f_arduinoCommand_ua[PYDUINO_DATA_INDEX_SIGNAL_TYPE_BYTE]      < PYDUINO_SIGNAL_NB
            and f_arduinoCommand_ua[PYDUINO_DATA_INDEX_FUNCTION_BYTE]         < PYDUINO_FUNCTION_NB
            and f_arduinoCommand_ua[PYDUINO_DATA_INDEX_ASSIGN_VALUE_BYTE]     < PYDUINO_ASSIGN_VALUE_NB
            ):
                if(f_arduinoCommand_ua[PYDUINO_DATA_INDEX_SIGNAL_TYPE_BYTE] == PYDUINO_SIGNAL_ANALOGIC):
                    #depending on arduino used
                    if(f_arduinoCommand_ua[PYDUINO_DATA_INDEX_PIN_NUMBER_BYTE] < g_MaxAnaPin_ua[ARDUINO_CART_USE]):
                        Ret_e = RC.OK
                    else:
                        Ret_e = RC.ERROR_NOT_ALLOWED
                #
                elif(f_arduinoCommand_ua[PYDUINO_DATA_INDEX_SIGNAL_TYPE_BYTE] == PYDUINO_SIGNAL_DIGITAL):
                    #depending on arduino used
                    if(f_arduinoCommand_ua[PYDUINO_DATA_INDEX_PIN_NUMBER_BYTE] < g_MaxDigPin_ua[ARDUINO_CART_USE]):
                        Ret_e = RC.OK
                    else:
                        Ret_e = RC.ERROR_NOT_ALLOWED
            else:
                Ret_e = RC.ERROR_NOT_ALLOWED
        if(Ret_e == RC.OK):
            #verify if the bus can handle 8 bytes emition 
            try:
                self.serieCom.write(bytes(f_arduinoCommand_ua))
                self.makeLog.LCF_SetMsgLog(log.INFO, "Python send ",str(f_arduinoCommand_ua))
                msg = self.Read_ArduinoSerial()
                self.makeLog.LCF_SetMsgLog(log.INFO, f"Python rcv {str(msg)}:")
            except: 
                Ret_e = RC.ERROR_BUSY
                self.makeLog.LCF_SetMsgLog(log.ERROR, "Cannot send Data on SerialCommunication in Send_ArduinoCommand Retcode:",Ret_e)
        return Ret_e
    #------------------------
    # Read_ArduinoSerial
    #------------------------
    def Read_ArduinoSerial(self)->str:
        """
            @brief      Read a complete lines from Serial Bus and return it 
        """
        return self.serieCom.readline().decode()
    
################################################################################
#                              FUNCTION DECLARATION
################################################################################


################################################################################
#                             FUNCTION IMPLMENTATION
################################################################################
def main()-> None:
    RC = t_eReturnCode()
    Ret_e = RC.OK
    serieCom = ArduinoCommunication(COMMUNICATION_PORT,COMMUNICATION_SPEED,TIMEOUT_DELAY)
    Ret_e = serieCom.Initialize_ArduinoCom()
    while(1):
        if(Ret_e == RC.OK):

            Ret_e =   serieCom.Send_ArduinoCommand(g_CommandArduinoLED_ON_ua)
            time.sleep(3)
            Ret_e =   serieCom.Send_ArduinoCommand(g_CommandArduinoLED_OFF_ua)
            print(Ret_e)
            time.sleep(3)
            print(f"Arduino second: {Ret_e}")
    return
   


################################################################################
#			                MAIN
################################################################################
if (__name__ == '__main__'):
    main()

################################################################################
#		                    END OF FILE
################################################################################



"""    
     @brief
     @details




     @params[in]
     @params[out]
     @retval
"""


