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
        destFileLocations = []
        for file in self.files:
            filename = self._generate_unique_filename(file)
            destFileLocation = os.path.join(self.location, filename)
            shutil.move(file, destFileLocation)
            destFileLocations.append(destFileLocation)
        return destFileLocations

    def _generate_unique_filename(self, src):
        return str(uuid.uuid4()) + '.mp3'
