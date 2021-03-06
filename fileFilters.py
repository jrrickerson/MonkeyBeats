import re
import os

class FileSource:
    def __init__(self, directory, followSymbolicLinks):
        self._initialDirectory = directory
        self._followSymbolicLinks = followSymbolicLinks
    
    def files(self):
        return [os.path.join(root, file) 
            for root, dirs, files in os.walk(self._initialDirectory, followlinks=self._followSymbolicLinks) 
                for file in files]

class FileFilter:
    def __init__(self, fileSource):
        self._fileSource = fileSource
        self._filterPattern = ".*"

    def _getFilter(self):
        return lambda file : re.search(self._filterPattern, file)

    def getFiles(self):
        return filter(self._getFilter(), self._fileSource.files())

class Mp3FileFilter(FileFilter):
    def __init__(self, fileSource):
        FileFilter.__init__(self, fileSource)
        self._filterPattern = "mp3$"

class NonMp3FileFilter(FileFilter):
    def __init__(self, fileSource):
        FileFilter.__init__(self, fileSource)
        self._filterPattern = "(?<!mp3)$"
