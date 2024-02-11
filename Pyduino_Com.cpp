/*********************************************************************
 * @file        Template.c
 * @brief       Template_BriefDescription.
 * @details     TemplateDetailsDescription.\n
 *
 * @author      xxxxxx
 * @date        jj/mm/yyyy
 * @version     1.0
 */

// ********************************************************************
// *                      Includes
// ********************************************************************
#include "Pyduino_Com.h"
// ********************************************************************
// *                      Defines
// ********************************************************************

// ********************************************************************
// *                      Types
// ********************************************************************
t_uint8 g_rcvData_ua8[MAX_NB_RCV_DATA] = 
{
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
    (t_uint8)0,
};
// ********************************************************************
// *                      Constants
// ********************************************************************

// ********************************************************************
// *                      Variables
// ********************************************************************

// ********************************************************************
// *                      Classe Prototype
// ********************************************************************
t_eReturnCode Pyduino_Com::SetArduinoCommand(t_ePyduino_Function f_FunctionSet_e, t_ePyduino_SignalType f_PinType ,t_uint8 f_selectedPin_u8, t_uint8 f_values)
{
    t_eReturnCode Ret_e = RC_OK;
    if(f_FunctionSet_e < (t_uint8)0 || f_FunctionSet_e > (t_uint8)PYDUINO_FUNCTION_NB)
    {
        Ret_e = RC_ERROR_PARAM_INVALID;
    }
    if(f_PinType < (t_uint8)0 || f_PinType > (t_uint8)PYDUINO_NB_TYPE)
    {
        Ret_e = RC_ERROR_PARAM_INVALID;
    }
    if(Ret_e == RC_OK)
    {
        switch(f_PinType)
        {
            case PYDUINO_ANALOGIC_TYPE:
            {
                Ret_e =  SetAnalogicCommand(f_FunctionSet_e, f_selectedPin_u8, f_values);
                break;
            }
            case PYDUINO_DIGITAL_TYPE : 
            {
                Ret_e = SetDigitalCommand(f_FunctionSet_e, f_selectedPin_u8, f_values);
                break;
            }
            case PYDUINO_NB_TYPE:
            {
                break;
            }
        }
        Serial.print("[Arduino] -> SetArduinoCommand : ");
        Serial.println(Ret_e);        
    }
    return Ret_e;
}
t_eReturnCode Pyduino_Com::SetAnalogicCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values)
{
    t_eReturnCode Ret_e = RC_OK;
    //Values has to be contain between 0 and 256, for PWM pin
    if(f_values < (t_uint16)0 || f_values > (t_uint16)256)
    {
        Ret_e = RC_ERROR_PARAM_INVALID;
    }
    if(Ret_e == RC_OK)
    {       
        switch(f_FunctionSet_e)
        {
            case PYDUINO_FUNCTION_ANALOG_WRITE :
            {
                analogWrite(f_selectedPin_u8, f_values);
            }
            default:
            {
                Ret_e = RC_ERROR_NOT_SUPPORTED;
            }
        }
    }
    return Ret_e;
}
t_eReturnCode Pyduino_Com::SetDigitalCommand(t_ePyduino_Function f_FunctionSet_e, t_uint8 f_selectedPin_u8, t_uint16 f_values)
{
    t_eReturnCode Ret_e = RC_OK;
    //Values has to be 0 or 1 
    if(f_values != HIGH && f_values != LOW)
    {
        Ret_e = RC_ERROR_PARAM_INVALID;
    }
    if(Ret_e == RC_OK)
    {       
        switch(f_FunctionSet_e)
        {
            case PYDUINO_FUNCTION_DIGITAL_WRITE :
            {
                digitalWrite(f_selectedPin_u8, f_values);
            }
            default:
            {
                Ret_e = RC_ERROR_NOT_SUPPORTED;
            }
        }
    }
    return Ret_e;
}

t_eReturnCode Pyduino_Com::ListenPythonForCommand(void)
{
    t_eReturnCode Ret_e = RC_OK;
    byte ReceivedBytes_by;
    t_uint8 countor_RcvData_u8;
    t_bool ReceptionningCommand_b;
    
    //Arduino waiting instructions  which are commmunicate from Python through Serial Com
    while(Serial.available() > 0 && Ret_e == RC_OK)
    {
        //We save the former byte if there is more than one byte received
        ReceivedBytes_by = (byte)Serial.read();
        //--------------------------------------------------------
        //-------------------Reminder-----------------------------
        //Fisrt Byte should be the Start bytes define in .h file
        // Last Byte should be the Ending byte define in ?h file
        //--------------------------------------------------------
        //Testing if the recv byte is the starting byte
        if(ReceivedBytes_by == (byte)START_BYTE_RCV_DATA)
        {
            //we're gonna asemble the msg
            countor_RcvData_u8 = (t_uint8)1;
            ReceptionningCommand_b = true;
            //Initialize g_rcvData_ua8
            Initialize_ArrayData();
            g_rcvData_ua8[PYDUINO_START_BYTE] =  (t_uint8)ReceivedBytes_by;
        }
        else if(ReceptionningCommand_b == (t_bool)true)
        {
            g_rcvData_ua8[countor_RcvData_u8] = (t_uint8)ReceivedBytes_by;
            countor_RcvData_u8++;

            if(countor_RcvData_u8 == (t_uint8)MAX_NB_RCV_DATA 
              && g_rcvData_ua8[PYDUINO_ENDING_BYTE] == (t_uint8)END_BYTE_RCV_DATA)
            {
                //Re-initialize stuff
                ReceptionningCommand_b = (t_bool)false;
                countor_RcvData_u8 = (t_uint8)1;
                //Calling a function to do the check sum 
                //Callling function to do what he has to be done if check sum correct
                //Make a msg wether the check sum succeed or failed and nothing is done
                Ret_e = CheckSum_RcvData();
                if(Ret_e == RC_OK)
                {
                    Ret_e = SetArduinoCommand((t_ePyduino_Function)g_rcvData_ua8[PYDUINO_FUNCTION_TYPE_BYTE],
                                            (t_ePyduino_SignalType)g_rcvData_ua8[PYDUINO_SIGNAL_TYPE_BYTE],
                                            (t_uint8) g_rcvData_ua8[PYDUINO_PIN_NUMBER_BYTE],
                                            (t_uint8)g_rcvData_ua8[PYDUINO_ASSIGN_VALUE_BYTE]);
                }
                else 
                {
                    Serial.print("[Arduino] -> Command not as expected : ");
                    Serial.println(Ret_e);
                }                
            }
        }        
    }
    return Ret_e;
}

void Pyduino_Com::Initialize_ArrayData(void)
{
    t_uint8 ResetIndex_u8;
    for(ResetIndex_u8 = (t_uint8)0 ; ResetIndex_u8 < (t_uint8)MAX_NB_RCV_DATA ; ResetIndex_u8++ )
    {
        g_rcvData_ua8[ResetIndex_u8] = (t_uint8)0;
    }
    return;
}
t_eReturnCode Pyduino_Com::CheckSum_RcvData(void)
{
t_eReturnCode Ret_e = RC_OK;
    //lenth of data received 
    //t_uint16 lenthData_received_u16;
    //Do check sum 
    if(g_rcvData_ua8[PYDUINO_NONE_BYTE2] != (t_uint8)0)
    {
        Ret_e = RC_ERROR_WRONG_RESULT;
    }
    return Ret_e;
}
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


