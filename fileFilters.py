import re
import os


def __mp3filter__(file):
    result = re.search("mp3$", file)
    # result is set if there was a hit
    return result is not None

def __nonmp3filter__(file):
    result = re.search("mp3$", file)
    return result is None


class FileFilter:
    def __init__(self, directory):
        self.directory = directory
    
    def __getUnfilteredFiles__(self):
        return [os.path.join(root, file) for root, dirs, files in os.walk(self.directory) 
                for file in files]

class Mp3FileFilter(FileFilter):
    def getFiles(self):
        return filter(__mp3filter__, self.__getUnfilteredFiles__())

class NonMp3FileFilter(FileFilter):
    def getFiles(self):
        return filter(__nonmp3filter__, self.__getUnfilteredFiles__())
