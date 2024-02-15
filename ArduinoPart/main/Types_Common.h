/* ******************************************************************
 * Copyright (C) 2019 - KUHN SA - Electronics
 *
 * This document is KUHN SA property.
 * It should not be reproduced in any medium or used in any way
 * without prior written consent of KUHN SA
 * ******************************************************************/
/**
 * @file        Types_Common.h
 * @brief       Global type definitions.
 * @details     Defines the function prototypes, variables, types, etc. that are
 *              global to the KED projects.\n
 *              All functions return an Return Code (RC) type ::t_eReturnCode.\n
 *              It should be RC_OK in case no error occurs (see below).\n
 *              In case of error, the returned code is the
 *              corresponding error code.\n
 *
 * @author      buejr
 * @date        26-02-2013
 * @version 1.0
 */

#ifndef _TYPES_COMMON_H
#define _TYPES_COMMON_H

    // ********************************************************************
    // *                      Includes
    // ********************************************************************
    
    // ********************************************************************
    // *                      Defines
    // ********************************************************************
    #ifndef NULL
        #define NULL    ((void *) 0) /**< NULL value for a pointer. */
    #endif

    #ifndef NULL_FUNCTION
        #define NULL_FUNCTION   (0)   /**< NULL value for a function pointer. Shall be casted in the corresponding function type. */
    #endif

    #ifndef TRUE
        #define TRUE    1       /**< TRUE value for a boolean. */
    #endif

    #ifndef FALSE
        #define FALSE   0       /**< FALSE value for a boolean. */
    #endif

    #ifndef false
        #define false   0       /**< FALSE value for a boolean. */
    #endif

    #ifndef true
        #define true    1       /**< TRUE value for a boolean. */
    #endif

    #define ASSERTION(Debug_u16) (Coord_AssertionFail((Debug_u16), (t_uint8 *)(__FILE__), __LINE__))
#ifndef M_TRUE
#define M_TRUE          1		        //!< TRUE value for precompilator directive. */
#endif

#ifndef M_FALSE
#define M_FALSE         0		        //!< FALSE value for precompilator directive. */
#endif

/** Macro to avoid the "unused variable" warning */
#ifndef UNUSED
    #define UNUSED(p) { (p) = (p); }
    // #ifdef KEIL_C166 
        // #define UNUSED(p) { (p) = (p); }
    // #else
        // #define UNUSED(x) ((void)x)
    // #endif
#endif
/** Macro to check that the return code is not an error */
#define CHECK_RC_NO_ERROR(eReturnCode)		(((t_sint16)eReturnCode) >= 0)
/** Macro to check that the return code is an error */
#define CHECK_RC_ERROR(eReturnCode)			(((t_sint16)eReturnCode) < 0)
    
    /** Redefine MucExtractXXX of BSP Lib_Type with correct type ( codesonar )*/
    #define Mu8ExtractByte0FromU16( Mu16Value )     (t_uint8)((t_uint16)(Mu16Value))
    #define Mu8ExtractByte1FromU16( Mu16Value )     (t_uint8)(((t_uint16)Mu16Value) >> 8)

    #define Mu8ExtractByte0FromU32( Mu32Value )     (t_uint8)((t_uint32)(Mu32Value))
    #define Mu8ExtractByte1FromU32( Mu32Value )     (t_uint8)(((t_uint32)Mu32Value) >> 8)
    #define Mu8ExtractByte2FromU32( Mu32Value )     (t_uint8)(((t_uint32)Mu32Value) >> 16)
    #define Mu8ExtractByte3FromU32( Mu32Value )     (t_uint8)(((t_uint32)Mu32Value) >> 24)

    /** Redefine MxBuildXXX of BSP Lib_Type with correct type ( codesonar )*/
    #define Mu16BuildWordFromByte(Mu8ValueB0, Mu8ValueB1)\
            (((t_uint16)(Mu8ValueB0)       /*& 0x00FF*/) | \
            (((t_uint16)(Mu8ValueB1) << 8) /*& 0xFF00*/) )

    #define Mu32BuildLongFromByte(Mu8ValueB0, Mu8ValueB1, Mu8ValueB2, Mu8ValueB3)\
            ((((t_uint32)(Mu8ValueB0))          /*& 0x000000FFUL*/) | \
            ((((t_uint32)(Mu8ValueB1)) << 8)    /*& 0x0000FF00UL*/) | \
            ((((t_uint32)(Mu8ValueB2)) << 16)   /*& 0x00FF0000UL*/) | \
            ((((t_uint32)(Mu8ValueB3)) << 24)   /*& 0xFF000000UL*/) )

    // ********************************************************************
    // *                      Types
    // ********************************************************************
    typedef unsigned char t_bool;               /**< Boolean type. */

    typedef unsigned char t_uint8;              /**< Unsigned 8-bit type. */
    typedef signed char t_sint8;                /**< Signed 8-bit type. */
    typedef unsigned short t_uint16;            /**< Unsigned 16-bit type. */
    typedef signed short t_sint16;              /**< Signed 16-bit type. */
    typedef unsigned long t_uint32;             /**< Unsigned 32-bit type. */
    typedef signed long t_sint32;               /**< Signed 32-bit type. */
    typedef float t_float32;                    /**< 32-bit float type. */
    //typedef unsigned long long t_uint64;        /**< Unsigned 64-bit type. */
    //typedef signed long long t_sint64;          /**< Signed 64-bit type. */
    typedef char t_char;                        /**< Plain char type (for strings). */

    /** Return code used in all interfaces. */
    /** Not compatible for 8-Bits targets. */
    typedef enum
    {
        // Errors
        RC_ERROR_PARAM_INVALID = -14,                   /**< At least one of the parameters is not in the allowed range. */
        RC_ERROR_PARAM_NOT_SUPPORTED = -13,             /**< At lest one of the parameters is not supported. */
        RC_ERROR_WRONG_STATE = -12,                     /**< The function cannot succeed in the current state. */
        RC_ERROR_MODULE_NOT_INITIALIZED = -11,          /**< The module must be initialized before calling the function. */
        RC_ERROR_MISSING_CONFIG = -10,                  /**< Some configuration is missing. */
        RC_ERROR_WRONG_CONFIG = -9,                     /**< The configuration is not consistent. */
        RC_ERROR_UNDEFINED = -8,                        /**< An undefined error has occurred. */
        RC_ERROR_NOT_SUPPORTED = -7,                    /**< The function is not supported. */
        RC_ERROR_BUSY = -6,                             /**< Process busy, task not accepted. */
        RC_ERROR_TIMEOUT = -5,                          /**< The operation timed out. */
        RC_ERROR_NOT_ALLOWED = -4,                      /**< Not allowed to perform the requested operation. */
        RC_ERROR_WRONG_RESULT = -3,                     /**< The operation has succeeded, but the result is incorrect. */
        RC_ERROR_LIMIT_REACHED = -2,                    /**< The operation cannot be done because a limit has been reached. */
        RC_ERROR_NOT_ENOUGH_MEMORY = -1,                /**< The operation cannot be done because there is not enough memory. */

        // OK
        RC_OK = 0,                                      /**< Process finished successfully. */

        // Warnings
        RC_WARNING_NO_OPERATION = 1,                    /**< No error occurred, but there was no operation to execute. */
        RC_WARNING_BUSY = 2,                            /**< The operation is accepted, but the process was already busy, */
                                                        /**< which means the previous operation has been stopped. */
        RC_WARNING_ALREADY_CONFIGURED = 3,              /**< The operation is accepted, but the user must be aware that */
                                                        /**< a previous configuration has been lost. */
        RC_WARNING_WRONG_CONFIG = 4,                     /**< The configuration is not consistent. */
        RC_WARNING_MISSING_CONFIG = 5,                  /**< Some configuration is missing. */
        RC_WARNING_INIT_PROBLEM = 6,                    /**< No initialization done, process performed as default mode. */
        RC_WARNING_PENDING = 7,                         /**< Operation accepted and started, but the result is not immediate. */
        RC_WARNING_NOT_ALLOWED = 8,                     /**< Not allowed to perform the requested operation. */
        RC_WARNING_LIMIT_REACHED = 9,                   /**< The operation cannot be done because a limit has been reached. */
        RC_WARNING_WRONG_RESULT = 10                    /**< The operation has succeeded, but the result is incorrect. */
    } t_eReturnCode;

    // ********************************************************************
    // *                      Prototypes
    // ********************************************************************
    /**
    * @brief        ASSERTION function .
    * @details      Call when a critical error occurs.\n
    *               Save debug information related to the error:\n
    *               - File address.\n
    *               - File Line.\n
    *               - Error Information.\n
    *               These information are used to set a DEEv.\n
    *
    */
    extern void Coord_AssertionFail(t_uint16 f_Debug_u16, t_uint8* f_File_pu8, t_uint32 f_Line_u32);

#endif                   /* _TYPES_COMMON_H */
//****************************************************************************
// End of File
//****************************************************************************
