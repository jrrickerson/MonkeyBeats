import eyeD3
import uuid
import sys
import os
from errors import *
from fileFilters import *
from fileMover import *
from organizer import *

def printDone():
    print "\033[1;31mdone\033[1;m" # print red

def Main():
    usage = "Usage: %s <directory>" % sys.argv[0]

    if len(sys.argv) != 2:
        print usage
        return

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        print "Directory not found"
        print usage
        return

    print "Directory to organize is %s" % directory
    sys.stdout.write("Retrieving all MP3 files...")
    sys.stdout.flush()
    
    fileSource = FileSource(directory)
    filter = Mp3FileFilter(fileSource)
    mp3files = filter.getFiles()

    printDone()

    print "Directory contains %s MP3 files" % len(mp3files)
    
    tempFolder = os.path.join(directory, str(uuid.uuid4()))
    sys.stdout.write("Moving files to temporary location %s..." % tempFolder)
    sys.stdout.flush()
    mover = FileMover(mp3files, tempFolder)
    tempFiles = mover.move()

    printDone()
    sys.stdout.write("Finding non MP3 files...")

    nonMp3FilesFilter = NonMp3FileFilter(fileSource)
    nonMp3Files = nonMp3FilesFilter.getFiles()

    for file in nonMp3Files:
        os.remove(file)

    printDone()

    sys.stdout.write("Directory contains ")
    sys.stdout.write("\033[1;31m" + str(len(nonMp3Files)) + "\033[1;m")
    sys.stdout.write(" non-MP3 files. Deleting...")

    printDone()

    sys.stdout.write("Organizing files...")
    sys.stdout.flush()

    organizer = Organizer(tempFiles, directory)
    organizer.organize()

    printDone()

if __name__ == "__main__":
    Main()


