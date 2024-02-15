/* ******************************************************************
 * Copyright (C) 2017 - KUHN SA - Electronics
 * 
 * This document is KUHN SA property.
 * It should not be reproduced in any medium or used in any way
 * without prior written consent of KUHN SA
/*********************************************************************
 * @file        Pyduino_Com.h
 * @brief       Communication Function to set and get pin value on Arduino.
 * @details     In order to exchange data between Python and the Arduino,
 *              A protocol has been made to do so.\n
 *         
 * 
 *                          |-------|------------------------|
 *                          | Octet |       Description      |
 *                          |-------|------------------------|
 *                          |   0   | Start Byte(char(0))    |
 *                          |-------|------------------------|
 *                          |   1   | Check Sum              |
 *                          |-------|------------------------|
 *                          |   2   | Signal Type            |
 *                          |-------|------------------------|
 *                          |   3   | Function to use        |
 *                          |-------|------------------------|
 *                          |   4   | Pin Number             |
 *                          |-------|------------------------|
 *                          |   5   | Value                  | 
 *                          |-------|------------------------|
 *                          |   6   | None                   |
 *                          |-------|------------------------|
 *                          |   7   | End Byte(10)           |
 *                          |-------|------------------------|
 * 
 *             Python send 8 bytes of data as shown above, to indicate 
 *             Which function has to be used and wich pin is concerned 
 *             We also send the value assign to the dedicate pin 
 *
 * @author      AUDMBA
 * @date        10/2/2024
 * @version     1.0/
 */

// ********************************************************************
// *                      Includes
// ********************************************************************
#include "Types_Common.h"
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
    PYDUINO_SIGNAL_ANALOGIC = 0,
    PYDUINO_SIGNAL_DIGITAL,

    PYDUINO_SIGNAL_NB,
}t_ePyduino_SignalType;

typedef enum 
{
    PYDUINO_START_BYTE = 0,          //first byte, message arrived 
    PYDUINO_CHECKSUM_BYTE,           //checksum byte
    PYDUINO_SIGNAL_TYPE_BYTE,        // Which t_ePyduino_PinType is concernced
    PYDUINO_FUNCTION_TYPE_BYTE,      //Which t_ePyduino_Function is concerned
    PYDUINO_PIN_NUMBER_BYTE,         //Whihc pin is concerned
    PYDUINO_ASSIGN_VALUE_BYTE,       //Assign value
    PYDUINO_NONE_BYTE2,              // To define has to be 0xOO in this case
    PYDUINO_ENDING_BYTE,            // End byte, message is finished 

    PYDUINO_BYTESNB_RCV_DATA,

}t_ePyduino_RcvData;


/*----------------------------STRUCTURE---------------------------------*/


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
        *	@details    
        *               
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
        //t_eReturnCode Stop_Communication();
        /**
        *
        *	@brief      Set the arduino Command wanted by user
        *	@details    
        *
        *
        *  @param[in] f_FunctionSet_e   : The function wanted by python in t_ePyduino_Function choice
        *  @param[in] f_PinType         : The pin type (Signal, Analogic)
        *  @param[in] f_selectedPin_u8  : The concerned pin
        *  @param[in] f_values          : Value to assign
        *  @param[out]
        * 
        *  @retval RC_OK			                @copydoc RC_OK
        *  @retval RC_ERROR_PARAM_INVALIDOK			@copydoc RC_ERROR_PARAM_INVALID
        *
        */
        t_eReturnCode SetArduinoCommand(t_ePyduino_Function f_FunctionSet_e, t_ePyduino_SignalType f_PinType ,t_uint8 f_selectedPin_u8, t_uint8 f_values);
        /**
        *
        *	@brief      Get the last arduino Command set by python user
        *	@details    
        *
        *
        *  @param[in] f_FunctionSet_e   : The function wanted by python in t_ePyduino_Function choice
        *  @param[in] f_PinType         : The pin type (Signal, Analogic)
        *  @param[in] f_selectedPin_u8  : The concerned pin
        *  @param[in] f_values          : Value to assign
        *  @param[out]
        * 
        *  @retval RC_OK			                @copydoc RC_OK
        *  @retval RC_ERROR_PARAM_INVALIDOK			@copydoc RC_ERROR_PARAM_INVALID
        *
        */
        t_eReturnCode GetArduinoCommand(t_ePyduino_Function f_FunctionSet_e, t_ePyduino_SignalType f_PinType ,t_uint8 f_selectedPin_u8, t_uint8 f_values);
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
        *	@brief      Set an analogic command on Arduino
        *	@details    
        *
        *
        *  @param[in] f_FunctionSet_e   : The function wanted by python in t_ePyduino_Function choice
        *  @param[in] f_selectedPin_u8  : The concerned pin
        *  @param[in] f_values          : Value to assign
        *  @param[out]
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode SetAnalogicCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values);
        /**
        *
        *	@brief      Set an Digitial command on Arduino
        *	@details    
        *
        *
        *  @param[in] f_FunctionSet_e   : The function wanted by python in t_ePyduino_Function choice
        *  @param[in] f_selectedPin_u8  : The concerned pin
        *  @param[in] f_values          : Value to assign
        *
        *  @retval RC_OK			@copydoc RC_OK
        *
        */
        t_eReturnCode SetDigitalCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values);
        /**
        *
        *	@brief      Reset to (t_uint8)0, elements of the array receiving the Data 
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


