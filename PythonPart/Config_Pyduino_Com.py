# ###############################################################################
# Copyright (C) 2017 - KUHN SA - Electronics
# 
# This document is KUHN SA property.
# It should not be reproduced in any medium or used in any way
# without prior written consent of KUHN SA
#################################################################################
#  @file        main.py
#  @brief       Arduino Parameter for comunication between Arduino and Python
#  @details     TemplateDetailsDescription.\n
#
#  @author      AUDMBA
#  @date        10/02/2024
#  @version     1.0
################################################################################
#                                       IMPORT
################################################################################

################################################################################
#                                       DEFINE
################################################################################

#-------------------------------------------------
# Arduino Function Available
#-------------------------------------------------
PYDUINO_FUNCTION_ANALOG_READ      =  (0x00)
PYDUINO_FUNCTION_ANALOG_WRITE     =  (0x01)
PYDUINO_FUNCTION_DIGITAL_READ     =  (0x02)
PYDUINO_FUNCTION_DIGITAL_WRITE    =  (0x03)

PYDUINO_FUNCTION_NB               =  (0x04)

#-------------------------------------------------
# Arduino Signal Type Managed
#-------------------------------------------------

PYDUINO_SIGNAL_ANALOGIC             =  (0x00)
PYDUINO_SIGNAL_DIGITAL              =  (0x01)
PYDUINO_SIGNAL_NB                   =  (0x02)
#-------------------------------------------------
# Arduino Value Mnged
#-------------------------------------------------
PYDUINO_ASSIGN_VALUE_LOW  =  (0x0)
PYDUINO_ASSIGN_VALUE_HIGH =  (0x1)

PYDUINO_ASSIGN_VALUE_NB = (0x02)

#-------------------------------------------------
# All Arduino card take in charged in this library
#-------------------------------------------------
PYDUINO_ARDUINO_UNO_REV3    =  (0x00)
PYDUINO_ARDUINO_UNO_R3      =  (0x01)
PYDUINO_ARDUINO_UNO_R4      =  (0x02)
PYDUINO_ARDUINO_ATMEGA328P  =  (0x03)
PYDUINO_ARDUINO_ATMEGA32    =  (0x04)
PYDUINO_ARDUINO_ATMEGA32U4  =  (0x05)
PYDUINO_ARDUINO_NANO_V3     =  (0x06)
PYDUINO_ARDUINO_MEGA2560    =  (0x07)

#-------------------------------------------------------------
# START PARAMETER FOR DIFFERENT ARDUINO PARAMETER
#-------------------------------------------------------------
#----------------------------------------
# START Parameter for Arduino UNO R3
#----------------------------------------

UNO_R3_PIN_ANA_A0 =  (0x00)
UNO_R3_PIN_ANA_A1 =  (0x01)
UNO_R3_PIN_ANA_A2 =  (0x02)
UNO_R3_PIN_ANA_A3 =  (0x03)
UNO_R3_PIN_ANA_A4 =  (0x04)
UNO_R3_PIN_ANA_A5 =  (0x05)

UNO_R3_ANA_NB =  (0x06)


UNO_R3_DIG_RX_D0 =  (0x00)
UNO_R3_DIG_TX_D1 =  (0x01)
UNO_R3_DIG__D2   =  (0x02)
UNO_R3_DIG__D3   =  (0x03)
UNO_R3_DIG__D4   =  (0x04)
UNO_R3_DIG__D5   =  (0x05)
UNO_R3_DIG__D6   =  (0x06)
UNO_R3_DIG__D7   =  (0x07)
UNO_R3_DIG__D8   =  (0x08)
UNO_R3_DIG__D9   =  (0x09)
UNO_R3_DIG__D10  =  (0x0A)
UNO_R3_DIG__D11  =  (0x0B)
UNO_R3_DIG__D12  =  (0x0C)
UNO_R3_DIG__D13  =  (0x0D)

UNO_R3_DIG_NB    =  (0x0E)
#-------------------------------------------------
# END Parameter for Arduino UNO R3
#-------------------------------------------------
#----------------------------------------
# START Parameter for Arduino MEGA 2560
#----------------------------------------
UNO_MEGA_2560_PIN_ANA_A0  =  (0x00)
UNO_MEGA_2560_PIN_ANA_A1  =  (0x01)
UNO_MEGA_2560_PIN_ANA_A2  =  (0x02)
UNO_MEGA_2560_PIN_ANA_A3  =  (0x03)
UNO_MEGA_2560_PIN_ANA_A4  =  (0x04)
UNO_MEGA_2560_PIN_ANA_A5  =  (0x05)
UNO_MEGA_2560_PIN_ANA_A6  =  (0x06)
UNO_MEGA_2560_PIN_ANA_A7  =  (0x07)
UNO_MEGA_2560_PIN_ANA_A8  =  (0x08)
UNO_MEGA_2560_PIN_ANA_A9  =  (0x09)
UNO_MEGA_2560_PIN_ANA_A10 =  (0x0A)
UNO_MEGA_2560_PIN_ANA_A11 =  (0x0B)
UNO_MEGA_2560_PIN_ANA_A12 =  (0x0C)
UNO_MEGA_2560_PIN_ANA_A13 =  (0x0D)
UNO_MEGA_2560_PIN_ANA_A14 =  (0x0E)
UNO_MEGA_2560_PIN_ANA_A15 =  (0x0F)

UNO_MEGA_2560_ANA_NB     =  (0x10)

UNO_MEGA_2560_PIN_DIG_RX0_D0  =  (0x00)
UNO_MEGA_2560_PIN_DIG_TX0_D1  =  (0x01)
UNO_MEGA_2560_PIN_DIG_PWM_D2  =  (0x02)
UNO_MEGA_2560_PIN_DIG_PWM_D3  =  (0x03)
UNO_MEGA_2560_PIN_DIG_PWM_D4  =  (0x04)
UNO_MEGA_2560_PIN_DIG_PWM_D5  =  (0x05)
UNO_MEGA_2560_PIN_DIG_PWM_D6  =  (0x06)
UNO_MEGA_2560_PIN_DIG_PWM_D7  =  (0x07)
UNO_MEGA_2560_PIN_DIG_PWM_D8  =  (0x08)
UNO_MEGA_2560_PIN_DIG_PWM_D9  =  (0x09)
UNO_MEGA_2560_PIN_DIG_PWM_D10 =  (0x0A)
UNO_MEGA_2560_PIN_DIG_PWM_D11 =  (0x0B)
UNO_MEGA_2560_PIN_DIG_PWM_D12 =  (0x0C)
UNO_MEGA_2560_PIN_DIG_PWM_D13 =  (0x0D)
UNO_MEGA_2560_PIN_DIG_TX3_D14 =  (0x0E)
UNO_MEGA_2560_PIN_DIG_RX3_D15 =  (0x0F)
UNO_MEGA_2560_PIN_DIG_TX2_D16 =  (0x10)
UNO_MEGA_2560_PIN_DIG_RX2_D17 =  (0x11)
UNO_MEGA_2560_PIN_DIG_TX1_D18 =  (0x12)
UNO_MEGA_2560_PIN_DIG_RX1_D19 =  (0x13)
UNO_MEGA_2560_PIN_DIG_SDA_D20 =  (0x14)
UNO_MEGA_2560_PIN_DIG_SCL_D21 =  (0x15)
UNO_MEGA_2560_PIN_DIG_D22     =  (0x16)
UNO_MEGA_2560_PIN_DIG_D23     =  (0x17)
UNO_MEGA_2560_PIN_DIG_D24     =  (0x18)
UNO_MEGA_2560_PIN_DIG_D25     =  (0x19)
UNO_MEGA_2560_PIN_DIG_D26     =  (0x1A)
UNO_MEGA_2560_PIN_DIG_D27     =  (0x1B)
UNO_MEGA_2560_PIN_DIG_D28     =  (0x1C)
UNO_MEGA_2560_PIN_DIG_D29     =  (0x1D)
UNO_MEGA_2560_PIN_DIG_D30     =  (0x1E)
UNO_MEGA_2560_PIN_DIG_D31     =  (0x1F)


UNO_MEGA_2560_DIG_NB          =  (0x20)
#----------------------------------------
# END Parameter for Arduino MEGA 2560
#----------------------------------------
#-------------------------------------------------------------
# END PARAMETER FOR DIFFERENT ARDUINO PARAMETER
#-------------------------------------------------------------


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

