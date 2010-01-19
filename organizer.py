import eyeD3
import os
import shutil

class Metadata:
    def __init__(self, name):
        self.files = set()
        self.name = name
        self.children = set()

    def addFile(self, file):
        self.files.add(file)

    def addFiles(self, files):
        self.files = files

    def addChild(self, childMetadata):
        self.children.add(childMetadata)

    def __str__(self):
        return self.name

class Organizer:
    def __init__(self, files, location):
        self.files = files
        self.location = location
        self.fileMetadatas = []

    def organize(self):
        tag = eyeD3.Tag()
        for file in self.files:
            try:
                tag.link(file)
            except eyeD3.TagException:
                print file + " has issue with tags"

