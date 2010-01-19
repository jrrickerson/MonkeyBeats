import eyeD3
import os
import shutil

def __retrieveMetadata__(tag):
    return { 'title' : tag.getTitle(), 
             'artist' : tag.getArtist(), 
             'album' : tag.getAlbum() }

def __nullMetadata__(metadata):
    return metadata['title'] is None or \
        metadata['album'] is None or \
        metadata['artist'] is None

def __stripMetadata__(metadata):
    metadata['title'] = metadata['title'].strip()
    metadata['album'] = metadata['album'].strip()
    metadata['artist'] = metadata['artist'].strip()

def __emptyMetadata__(metadata):
    return len(metadata['title']) == 0 or \
        len(metadata['album']) == 0 or \
        len(metadata['artist']) == 0

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

    def organize(self):
        tag = eyeD3.Tag()
        for file in self.files:
            try:
                tag.link(file)
                metadata = __retrieveMetadata__(tag)
                if not __nullMetadata__(metadata):
                    __stripMetadata__(metadata)
                    if not __emptyMetadata__(metadata):
                        print metadata
            except eyeD3.TagException:
                print file + " has issue with tags"


