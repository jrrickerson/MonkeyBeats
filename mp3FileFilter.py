import re
import os


def __mp3filter__(file):
    result = re.search("mp3$", file)
    # result is set if there was a hit
    return result is not None

def __nonmp3filter__(file):
    result = re.search("mp3$", file)
    return result is None

class Mp3FileFilter:
    def __init__(self, directory):
        self.directory = directory

    def __getUnfilteredFiles__(self):
        return [root + '/' + file for root, dirs, files in os.walk(self.directory) 
                for file in files]

    def getFiles(self):
        allFiles = self.__getUnfilteredFiles__()
        return filter(__mp3filter__, allFiles)

class NonMp3FileFilter:
    def __init__(self, directory):
        self.directory = directory
    
    def __getUnfilteredFiles__(self):
        return [root + '/' + file for root, dirs, files in os.walk(self.directory)
                for file in files]

    def getFiles(self):
        allFiles = self.__getUnfilteredFiles__()
        return filter(__nonmp3filter__, allFiles)
