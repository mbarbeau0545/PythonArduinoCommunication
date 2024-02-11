#################################################################################
#  @file        main.py
#  @brief       Template_BriefDescription.
#  @details     TemplateDetailsDescription.\n
#
#  @author      AUDMBA
#  @date        jj/mm/yyyy
#  @version     1.0
#           |-------|------------------------|
#           | Octet |       Description      |
#           |-------|------------------------|
#           |   0   | Start Byte(char(0))    |
#           |-------|------------------------|
#           |   1   | Check Sum              |
#           |-------|------------------------|
#           |   2   | Signal Type            |
#           |-------|------------------------|
#           |   3   | Function to use        |
#           |-------|------------------------|
#           |   4   | Pin Number             |
#           |-------|------------------------|
#           |   5   | Value                  | 
#           |-------|------------------------|
#           |   6   | None                   |
#           |-------|------------------------|
#           |   7   | End Byte(10)           |
#           |-------|------------------------|
################################################################################
#                                       IMPORT
################################################################################

from Config.TypeCommon import*
from Config_Pyduino_Com import*
import serial
import sys
import time
################################################################################
#                                       Constants
################################################################################
#Arduino Parameter
COMMUNICATION_PORT = "COM4"
COMMUNICATION_SPEED = 9600
TIMEOUT_DELAY = 3

START_BYTE_SEND_DATA = int(0xFE)
END_BYTE_SEND_DATA   = int(0xFF)

#-------------------------------------------
# Structure for sending Command to arduino
#-------------------------------------------
PYDUINO_DATA_INDEX_START_BYTE           = int(0x00)  # First byte, message arrived 
PYDUINO_DATA_INDEX_CHECKSUM_BYTE        = int(0x01)  # Checksum byte
PYDUINO_DATA_INDEX_SIGNAL_TYPE_BYTE     = int(0x02)  # Which t_ePyduino_PinType is concernced
PYDUINO_DATA_INDEX_FUNCTION_TYPE_BYTE   = int(0x03)  # Which t_ePyduino_Function is concerned
PYDUINO_DATA_INDEX_PIN_NUMBER_BYTE      = int(0x04)  # Whihc pin is concerned
PYDUINO_DATA_INDEX_ASSIGN_VALUE_BYTE    = int(0x05)  # To define has to be 0xOO in this case
PYDUINO_DATA_INDEX_NONE_BYTE2           = int(0x06)  # To define has to be 0xOO in this case
PYDUINO_DATA_INDEX_ENDING_BYTE          = int(0x07)  # End byte, message is finished 

PYDUINO_DATA_BYTES_NB_SEND_DATA     = int(0x08)


################################################################################
#                                       Variable
################################################################################
g_CommandArduinoLED_ON_ua = [
    START_BYTE_SEND_DATA,
    int(0),
    PYDUINO_DIGITAL_TYPE,
    PYDUINO_FUNCTION_DIGITAL_WRITE,
    PYDUINO_DIG__D5,
    HIGH,
    int(0),
    END_BYTE_SEND_DATA
]
g_CommandArduinoLED_OFF_ua = [
    START_BYTE_SEND_DATA,
    int(0),
    PYDUINO_DIGITAL_TYPE,
    PYDUINO_FUNCTION_DIGITAL_WRITE,
    PYDUINO_DIG__D5,
    LOW,
    int(0),
    END_BYTE_SEND_DATA
]
################################################################################
#                                       CLASS
################################################################################

################################################################################
#                              FUNCTION DECLARATION
################################################################################
SerieCommand = serial.Serial()
# ==================================
# Fonction : Collect_Instruction
# ==================================
def Collect_Instruction()-> str:
    stringInstruction_str = input(">")
    return stringInstruction_str

# ==================================
# Fonction : Collect_Instruction
# ==================================
def SendArduinoCommande(f_Command_Arduino)->None:
    
    SerieCommand.write(bytes(f_Command_Arduino))
    return

# ==================================
# Fonction : Collect_Instruction
# ==================================
def DisplayArduinoResponse()-> None:
    ArduinoResponse = SerieCommand.readline()
    print(ArduinoResponse)
    return 
################################################################################
#                             FUNCTION IMPLMENTATION
################################################################################
def main()-> None:
    Countor = 0
    try:
        print()
        print("Tentative d'initialisation du port série...")
        SerieCommand.port = COMMUNICATION_PORT
        SerieCommand.baudrate = COMMUNICATION_SPEED
        SerieCommand.timeout = TIMEOUT_DELAY
        SerieCommand.open()

    except:
        print("[ERREUR] Impossible d'ouvrir le port " + COMMUNICATION_PORT)
        sys.exit()
    print("Connexion réussie sur le port " + COMMUNICATION_PORT + " !")
    # Boucle perpétuelle de capture d'instructions, saisies manuellement par l'utilisateur (nota : EXIT permet de sortir de cette boucle)
    print()
    print("PRG1 - Test pilotage Blink Arduino depuis programme Python")
    while(Countor < 10):
        SendArduinoCommande(g_CommandArduinoLED_ON_ua)
        DisplayArduinoResponse()
        time.sleep(2)
        SendArduinoCommande(g_CommandArduinoLED_OFF_ua)
        DisplayArduinoResponse()
        time.sleep(2)
        Countor+= int(1)

    SerieCommand.close()
    print(f"EXIT : port série {COMMUNICATION_PORT} fermé, fin du programme.")
    
    return
################################################################################
#			                MAIN
################################################################################
if (__name__ == '__main__'):
    main()

################################################################################
#		                    END OF FILE
################################################################################
# ==================================
# Fonction : Collect_Instruction
# ==================================


"""    
     @brief
     @details




     @params[in]
     @params[out]
     @retval
"""


