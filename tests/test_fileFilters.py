import unittest
import nose

from fileFilters import *

# Fixture setup and teardown
def setUpModule():
    pass
def tearDownModule():
    pass

class Mp3FileFilterTestFixture(unittest.TestCase):
    def setUp(self):
        self._initialFileList = []
        self._expectedFileList = []
        self._filteredList = []

    def tearDown(self):
        self.assertEquals(self._expectedFileList, self._filteredList, "Filtered list does not match expected list")

    def applyFilter(self):
        fileSource = MockFileSource(self._initialFileList)
        mp3Filter = Mp3FileFilter(fileSource)
        self._filteredList = mp3Filter.getFiles()

    def testAllSourceFilesMatchFilter(self):
        self._initialFileList = ["happy.mp3", "sad.mp3", "fun.mp3", "goofy.mp3"]
        self._expectedFileList = self._initialFileList
        self.applyFilter()

    def testNoSourceFilesMatchFilter(self):
        self._initialFileList = ["happy.ogg", "sad.txt", "fun.wav", "goofy"]
        self._expectedFileList = []
        self.applyFilter()

class MockFileSource:
    def __init__(self, mockFileList):
        self._fileList = mockFileList

    def files(self):
        return self._fileList

