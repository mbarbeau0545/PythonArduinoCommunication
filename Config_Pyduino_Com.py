#################################################################################
#  @file        main.py
#  @brief       Arduino Parameter for comunication between Arduino and Python
#  @details     TemplateDetailsDescription.\n
#
#  @author      AUDMBA
#  @date        jj/mm/yyyy
#  @version     1.0
################################################################################
#                                       IMPORT
################################################################################

################################################################################
#                                       DEFINE
################################################################################




#-------------------------------------------------
# All Arduino card take in charged in this library
#-------------------------------------------------
PYDUINO_ARDUINO_UNO_REV3    = int(0x01)
PYDUINO_ARDUINO_UNO_R3      = int(0x02)
PYDUINO_ARDUINO_UNO_R4      = int(0x03)
PYDUINO_ARDUINO_ATMEGA328P  = int(0x04)
PYDUINO_ARDUINO_ATMEGA32    = int(0x05)
PYDUINO_ARDUINO_ATMEGA32U4  = int(0x06)
PYDUINO_ARDUINO_NANO_V3     = int(0x07)

#-------------------------------------------------------------
# START PARAMETER FOR DIFFERENT ARDUINO PARAMETER
#-------------------------------------------------------------
#----------------------------------------
# START Parameter for Arduino UNO R3
#----------------------------------------

UNO_R3_PIN_ANA_A0 = int(0x00)
UNO_R3_PIN_ANA_A1 = int(0x01)
UNO_R3_PIN_ANA_A2 = int(0x02)
UNO_R3_PIN_ANA_A3 = int(0x03)
UNO_R3_PIN_ANA_A4 = int(0x04)
UNO_R3_PIN_ANA_A5 = int(0x05)

PYDUINO_ANA_NB = int(0x06)


PYDUINO_DIG_RX_D0 = int(0x00)
PYDUINO_DIG_TX_D1 = int(0x01)
PYDUINO_DIG__D2   = int(0x02)
PYDUINO_DIG__D3   = int(0x03)
PYDUINO_DIG__D4   = int(0x04)
PYDUINO_DIG__D5   = int(0x05)
PYDUINO_DIG__D6   = int(0x06)
PYDUINO_DIG__D7   = int(0x07)
PYDUINO_DIG__D8   = int(0x08)
PYDUINO_DIG__D9   = int(0x09)
PYDUINO_DIG__D10  = int(0x0A)
PYDUINO_DIG__D11  = int(0x0B)
PYDUINO_DIG__D12  = int(0x0C)
PYDUINO_DIG__D13  = int(0x0D)

PYDUINO_DIG_NB    = int(0x0E)


#-------------------------------------------------
# END Parameter for Arduino UNO R3
#-------------------------------------------------

#-------------------------------------------------------------
# END PARAMETER FOR DIFFERENT ARDUINO PARAMETER
#-------------------------------------------------------------

#-------------------------------------------------
# Arduino Function Available
#-------------------------------------------------
PYDUINO_FUNCTION_ANALOG_READ      = int(0x00)
PYDUINO_FUNCTION_ANALOG_WRITE     = int(0x01)
PYDUINO_FUNCTION_DIGITAL_READ     = int(0x02)
PYDUINO_FUNCTION_DIGITAL_WRITE    = int(0x03)

PYDUINO_FUNCTION_NB               = int(0x04)

#-------------------------------------------------
# Arduino Signal Type Managed
#-------------------------------------------------

PYDUINO_ANALOGIC_TYPE             = int(0x00)
PYDUINO_DIGITAL_TYPE              = int(0x01)
PYDUINO_NB_TYPE                   = int(0x02)

HIGH = int(1)
LOW = int(0)

################################################################################
#                                       CLASS
################################################################################


################################################################################
#		                    END OF FILE
################################################################################
##########################
# Function_name
##########################

######################################################
#
# @brief
# @details
#
#
#
#
# @params[in]
# @params[out]
# @retval
#
#####################################################

