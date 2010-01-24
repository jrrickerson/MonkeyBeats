import os
import shutil
import uuid

class FileMover:
    def __init__(self, files, location):
        self.files = files
        self.location = location

    def move(self):
        if not os.path.exists(self.location):
            os.makedirs(self.location)
        tempFileLocations = []
        for file in self.files:
            tempFileName = str(uuid.uuid4()) + '.mp3'
            tempFileLocation = os.path.join(self.location, tempFileName)
            shutil.move(file, tempFileLocation)
            tempFileLocations.append(tempFileLocation)
        return tempFileLocations
