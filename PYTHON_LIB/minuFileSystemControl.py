###############################################################################################
# Config Section
###############################################################################################

INTEGRATION_VERSION = "I070_01_01"

FBL_VERSION = "FD20"

FULL_FLASH_USE_STMIN = "Stmin0"

###############################################################################################
# Code Section
###############################################################################################

import binascii
import os, sys, stat
import re 
import shutil
import time

class MinuFileSystemControl(object):

    def __init__(self, arg):
        super(MinuFileSystemControl, self).__init__()
        self.arg = arg

    def checkIsFileExist(filePath):
        if os.path.exists(filePath):    
            return True
        return False

    def checkIsDirExist(dirPath):
        if os.path.exists(dirPath):    
            return True
        return False

    def checkIsFileWithin(filePath, withInDay = 0):
        fileCreatedTime = os.path.getcime(filePath);
        currentTime = time.gmtime();    
        if((currentTime.tm_year - fileCreatedTime.tm_year == 0) and (currentTime.tm_year - fileCreatedTime.tm_year <= withInDay)):
            return True
        return False

    def checkIsFileToday(filePath):
        return checkIsFileWithin(filePath, 0)

    def removeFile(filePath):
        if os.path.exists(filePath):
            os.chmod(filePath, stat.S_IRWXU)
            os.remove(filePath)
            return True
        return False

    def copyFile(src,dst,overWrite = False):
        if os.path.exists(src):
            if os.path.exists(dst):
                if overwrite == False or not removeFile(dst):
                    return False
                shutil.copy2(src, dst)
                return True
        return False

    def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IRWXU)

    def copyDir(src,dst,overWrite = False):
        if os.path.exists(src):
            if os.path.exists(dst):
                if overwrite == False or not shutil.rmtree(dst, onerror = on_rm_error):
                    return False
            shutil.copytree(src,dst)
            return True
        return False