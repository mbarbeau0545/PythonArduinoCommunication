#################################################################################
#  @file        ModuleLog.py
#  @brief       Manage to create log file and complete them.\n
#  @details     This module allows the client to :
#               - Init one or more files
#               - Send a msg into a particular file
#               - Create a filter to print only error critical etc
#               - Create a file for only put data in it
#               - excel File ?
#               - HTML file ?
#
#  @author      AUDMBA
#  @date        10/01/2024
#  @version     1.0
################################################################################
#                                       IMPORT
################################################################################
import logging as log
from datetime import datetime
from TypeCommon import*

################################################################################
#                                       DEFINE
################################################################################
IsModuleOn_b:bool = False
###################
#constant to use 
###################
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}
################################################################################
#                                       CLASS
################################################################################
##########################
# Start Class MngLogFile
##########################
class MngLogFile():
    def __init__(self, f_folder_path:str, f_fileName, f_level:int, f_PurposeFile:str)-> t_eReturnCode:
        RC = t_eReturnCode()
        global IsModuleOn_b
        Ret_e = RC.OK
        if(isinstance(f_folder_path,str) != True 
           and isinstance(f_level,int) != True 
           and isinstance(f_fileName,str) != True
           and isinstance(f_PurposeFile,str) != True           
           ):
            
            Ret_e = RC.ERROR_MODULE_NOT_INITIALIZED
            IsModuleOn_b = False

        if(Ret_e == RC.OK):

            self.FolderPath = f_folder_path
            self.FileName = f_fileName
            self.LevelInfo = f_level
            self.Purpose = f_PurposeFile
            Ret_e = self._LCF_IniParamCfg()
            if(Ret_e != RC.OK):
                print(f"File not initialized as it should be : {Ret_e}")
            if(Ret_e == RC.OK):
                IsModuleOn_b = True
        return 
    ######################################################
    #                 _LCF_InitFileTmpl
    # @brief    Make the file look prettier
    #           
    # @details  
    #
    #
    #
    # @params[in] f_path : the path to the folder log 
    # @params[in] f_fileName : the log file name 
    # @params[in] f_level : the level of log information
    # @params[in] f_msg : the msg to put in file
    # @params[in] f_data : the data selected, set as None
    # @params[out] 
    # @retval
    #
    #####################################################
    def _LCF_InitFileTmpl(self)->t_eReturnCode: ...
    ######################################################
    #                 LCF_IniParamCfg
    # @brief    This function config file_log
    # @details  This function thanks to loggerd library 
    #           create a log file
    #           Several file can be initialize
    #
    #
    #
    # @params[in] f_path : the path to the folder log 
    # @params[in] f_fileName : the log file name 
    # @params[in] f_level : the level of log information
    # @params[out]
    # @retval
    #
    #####################################################
    def _LCF_IniParamCfg(self) -> t_eReturnCode: ...
    ######################################################
    #                 LCF_SetMsgLog
    # @brief    This function allow to print msg 
    #           and data in log file.\n
    # @details  
    #
    #
    #
    # @params[in] f_path : the path to the folder log 
    # @params[in] f_fileName : the log file name 
    # @params[in] f_level : the level of log information
    # @params[in] f_msg : the msg to put in file
    # @params[in] f_data : the data selected, set as None
    # @params[out] 
    # @retval
    #
    #####################################################
    def LCF_SetMsgLog(f_level: int, f_fileName: str, f_msg,f_data=None)-> t_eReturnCode: ...
    #####################################################
    #                 LCF_GetInformationFromFile()
    # @brief    This function config file_log
    # @details  This function thanks to loggerd library 
    #           create a log file
    #           Several file can be initialize
    #
    #
    #
    # @param[in] f_path : the path to the folder log 
    # @param[in] f_fileName : the log file name 
    # @param[in] f_level : the level of log information
    # @param[out]
    # @retval
    #
    def LCF_GetInformationFromFile(f_folder_path:str,f_fileName:str, f_level:log)->t_eReturnCode:...
    ##########################
    # _LCF_InitFileTmpl
    ##########################
    def _LCF_InitFileTmpl(self)->t_eReturnCode: 
        #verify entry
        RC = t_eReturnCode()
        Ret_e = RC.OK
        actual_time = datetime.now()
        formated_date = actual_time.strftime("%Y-%m-%d")
        startFile = ("##########################################################################\n"
                    f"#  @file              {self.FileName}\n"
                    f"#  @brief             This document purpose is for {self.Purpose} .\n"
                    "#  @author            AUDMBA\n"
                    f"#  @Last Update       {formated_date}\n"
                    "############################################################################\n\n")

        log_file_path = self.FolderPath + "//" + self.FileName
        # Ouvrez le fichier en mode écriture et écrivez l'en-tête
        with open(log_file_path, 'w') as file:
            file.write(startFile)

        return Ret_e
    ##########################
    # LCF_IniParamCfg
    ##########################
    def _LCF_IniParamCfg(self) -> t_eReturnCode:
        global IsModuleOn_b
        RC = t_eReturnCode()
        Ret_e = RC.OK
        Ret_e = self._LCF_InitFileTmpl()
        if(Ret_e != RC.OK and IsModuleOn_b == True):
            Ret_e = RC.ERROR_MODULE_NOT_INITIALIZED
        return Ret_e
    ##########################
    # LCF_SetMsgLog
    ##########################
    def LCF_SetMsgLog(self, f_level:int, f_msg, f_data=None):
        
        RC = t_eReturnCode()
        Ret_e = RC.OK
        log_file_path:str
        level_str:str = " "
        if isinstance(f_level, int) != True and isinstance(self.FileName, str) != True:
            Ret_e = RC.ERROR_PARAM_INVALID
        if(IsModuleOn_b != True):
            Ret_e = RC.ERROR_MODULE_NOT_INITIALIZED
        if(Ret_e == RC.OK):
            log_file_path = self.FolderPath + "//" + self.FileName
            actual_time = datetime.now()
            formated_date = actual_time.strftime("%Y-%m-%d %H:%M:%S")

            if(f_level in _levelToName):
                level_str = _levelToName[f_level]
            
            if(level_str == " "):
                print(f"LCF_SetMsgLog, cannot find a level on base for {f_level}")
                Ret_e = RC.ERROR_PARAM_INVALID
            if(Ret_e == RC.OK):
                msg_to_write_str = formated_date + " "+ f"[{level_str}]" + " " + f_msg

                if(f_data != None):
                    msg_to_write_str += f": {f_data}\n"
                else:
                    msg_to_write_str += "\n"
                # Ouvrez le fichier en mode écriture
                with open(log_file_path, 'a+') as file:
                    file.write(msg_to_write_str)
        return Ret_e
    ##############################
    # LCF_SortPerLevel
    ##############################
    def LCF_SortPerLevel(self,f_NewfileName:str, f_level:log)->t_eReturnCode:
        RC = t_eReturnCode()
        Ret_e = RC.OK
        level_str:str = None
        if isinstance(f_level, int) != True and isinstance(f_NewfileName, str) != True:

            Ret_e = RC.ERROR_PARAM_INVALID
        if(IsModuleOn_b != True):
            Ret_e = RC.ERROR_MODULE_NOT_INITIALIZED
        if(Ret_e == RC.OK):

            #change log:int into an str 
            if(f_level in _levelToName):

                level_str = _levelToName[f_level]

            if(level_str == None):

                Ret_e = RC.ERROR_MISSING_CONFIG

            if(Ret_e == RC.OK):

                actual_time = datetime.now()
                formated_date = actual_time.strftime("%Y-%m-%d")
                startFile = ("##########################################################################\n"
                            f"#  @file              {f_NewfileName}\n"
                            f"#  @brief             This document purpose is for {level_str} category.\n"
                            "#  @author            AUDMBA\n"
                            f"#  @Last Update       {formated_date}\n"
                            "############################################################################\n\n")

                log_file_path = self.FolderPath + "//" + self.FileName
                with open(f"{self.FolderPath}/log_{level_str}.log", "w") as file_writing:
                    file_writing.write(startFile)

                with open(f"{self.FolderPath}/{self.FileName}", "r") as file_extraction:
                            for line in file_extraction:
                                if(f"{level_str}" in line):
                                    with open(f"{self.FolderPath}/log_{level_str}.log", "a+") as file_writing:
                                        file_writing.write(line )
        return Ret_e
##########################
# END Class MngLogFile
##########################
################################################################################
#                                 FUNCTION DECLARATION
################################################################################



################################################################################
#                             FUNCTION IMPLEMENTATION
################################################################################







################################################################################
#			                    EXAMPLE
################################################################################

"""PrintLog = MngLogFile("Doc//Log","filey.log",log.DEBUG,"print things")
PrintLog.LCF_SetMsgLog(log.DEBUG,"Je suis un msg",8)
PrintLog.LCF_SetMsgLog(log.ERROR,"Je suis un msg sans data")
PrintLog.LCF_SortPerLevel("LogERROR.log",log.ERROR)"""


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






