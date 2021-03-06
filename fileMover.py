import os
import shutil
import uuid
import re

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
        result = re.search("\.[^\.]*$", src)
        extension = ""
        if result is not None:
            extension = result.group(0)
        return str(uuid.uuid4()) + extension
