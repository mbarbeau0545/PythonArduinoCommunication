/*********************************************************************
 * @file        ModuleArduino.h
 * @brief       Template_BriefDescription.
 * @details     TemplateDetailsDescription.\n
 *           |-------|------------------------|
 *           | Octet |       Description      |
 *           |-------|------------------------|
 *           |   0   | Start Byte(char(0))    |
 *           |-------|------------------------|
 *           |   1   | Check Sum              |
 *           |-------|------------------------|
 *           |   2   | Signal Type            |
 *           |-------|------------------------|
 *           |   3   | Function to use        |
 *           |-------|------------------------|
 *           |   4   | Pin Number             |
 *           |-------|------------------------|
 *           |   5   | Value                  | 
 *           |-------|------------------------|
 *           |   6   | None                   |
 *           |-------|------------------------|
 *           |   7   | End Byte(10)           |
 *           |-------|------------------------|
 *
 * @author      AUDMBA
 * @date        10/2/2024
 * @version     1.0/
 */

// ********************************************************************
// *                      Includes
// ********************************************************************
#include "Include/Config/TypeCommon.h"
#include <Arduino.h>
// ********************************************************************
// *                      Defines
// ********************************************************************
#define START_BYTE_RCV_DATA (byte)0xFE
#define END_BYTE_RCV_DATA   (byte)0XFF
#define MAX_NB_RCV_DATA (t_uint8)8                     /**<number max of bytes we can receive in one message*/
// ********************************************************************
// *                      Types
// ********************************************************************
/*------------------------------ENUM-----------------------------------*/


typedef enum
{
    PYDUINO_FUNCTION_ANALOG_READ = 0,
    PYDUINO_FUNCTION_ANALOG_WRITE,
    PYDUINO_FUNCTION_DIGITAL_READ,
    PYDUINO_FUNCTION_DIGITAL_WRITE,

    PYDUINO_FUNCTION_NB,

}t_ePyduino_Function;

typedef enum
{
    PYDUINO_ANALOGIC_TYPE = 0,
    PYDUINO_DIGITAL_TYPE,
    PYDUINO_NB_TYPE,
}t_ePyduino_SignalType;

typedef enum 
{
    PYDUINO_START_BYTE = 0,          //first byte, message arrived 
    PYDUINO_CHECKSUM_BYTE,           //checksum byte
    PYDUINO_SIGNAL_TYPE_BYTE,        // Which t_ePyduino_PinType is concernced
    PYDUINO_FUNCTION_TYPE_BYTE,      //Which t_ePyduino_Function is concerned
    PYDUINO_PIN_NUMBER_BYTE,         //Whihc pin is concerned
    PYDUINO_ASSIGN_VALUE_BYTE,              // To define has to be 0xOO in this case
    PYDUINO_NONE_BYTE2,              // To define has to be 0xOO in this case
    PYDUINO_ENDING_BYTE,            // End byte, message is finished 

    PYDUINO_BYTESNB_RCV_DATA,

}t_ePyduino_RcvData;

typedef enum 
{
    PYDUINO_ARDUINO_UNO_REV3,
    PYDUINO_ARDUINO_UNO_R3,
    PYDUINO_ARDUINO_UNO_R4,
    PYDUINO_ARDUINO_ATMEGA328P,
    PYDUINO_ARDUINO_ATMEGA32,
    PYDUINO_ARDUINO_ATMEGA32U4,
    PYDUINO_ARDUINO_NANO_V3,
}t_ePyduino_ArduinoCart;
/*----------------------------STRUCTURE---------------------------------*/
/*typedef struct
{
    t_char initiateDataMsg_c;
    t_uint8 checkSum_u8;
    t_ePyduino_CommandType isAnaorDigValue_u;
    t_uPyduino_Pin_ArduinoUnoR3 TypeCommand_e;


}t_sPyduino_RcvData;*/
/*------------------------------UNION--------------------------------*/

// ********************************************************************
// *                      Constants
// ********************************************************************

// ********************************************************************
// *                      Variables
// ********************************************************************

// ********************************************************************
// *                      Classe Prototype
// ********************************************************************
class Pyduino_Com
{
    public:
    //Constructor
        /**
        *
        *	@brief      Initiate the communication with Python
        *	@details    Set the right version of Arduino the right Port used
        *               The right Baudrate and the right timelaps delay 
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode Start_Communication();

        /**
        *
        *	@brief      Stop the communication with Python
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode Stop_Communication();
        /**
        *
        *	@brief      Set the arduino Command wanted by user
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode SetArduinoCommand(t_ePyduino_Function f_FunctionSet_e, t_ePyduino_SignalType f_PinType ,t_uint8 f_selectedPin_u8, t_uint8 f_values);
        /**
        *
        *	@brief      Wait for python orders and collecting them in a buffer 
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode GetArduinoCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u, t_uint16 f_values);
        /**
        *
        *	@brief      Wait for python orders and collecting them in a buffer 
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode ListenPythonForCommand();
        /**
        *
        *	@brief      Send msg with what Arduino understand to do 
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode cb_ArduinoRcvCommandFromPython();

    private:
        /**
        *
        *	@brief      Check the number of bytes received is conform with what's expected
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode CheckSum_RcvData();

        /**
        *
        *	@brief      Check the number of bytes received is conform with what's expected
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode SetAnalogicCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values);
        /**
        *
        *	@brief      Check the number of bytes received is conform with what's expected
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode SetDigitalCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values);
        /**
        *
        *	@brief      Check the number of bytes received is conform with what's expected
        *	@details    
        *
        *
        *  @param[in]
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        void Initialize_ArrayData(void);

    
};
// ********************************************************************
// *                      Classe Implementation
// ********************************************************************

//****************************************************************************
//                      Local functions - Prototypes
//****************************************************************************

/**
 *
 *	@brief
 *	@details
 *
 *
 *	@params[in]
 *	@params[out]
 *
 *  @retval RC_OK			@copydoc RC_OK
 *
 */

//****************************************************************************
//                      Public functions - Implementation
//****************************************************************************

//****************************************************************************
//                      Local functions - Implementation
//****************************************************************************

//****************************************************************************
// End of File
//****************************************************************************


