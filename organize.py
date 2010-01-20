import eyeD3
import uuid
import sys
import os
from errors import *
from fileFilters import *
from fileMover import *
from organizer import *
from views.consoleView import ConsoleView

def Main():

    view = ConsoleView()
    if len(sys.argv) != 2:
        view.displayUsage()
        return

    directory = sys.argv[1]

    if not os.path.isdir(directory):
        view.displayLine("Directory not found")
        view.displayUsage()
        return

    view.displayLine("Directory to organize is %s" % directory)
    view.displayMessage("Retrieving all MP3 files...")
    
    fileSource = FileSource(directory)
    filter = Mp3FileFilter(fileSource)
    mp3files = filter.getFiles()

    view.displayDone()
    view.displayLine("Directory contains %s MP3 files" % len(mp3files))
    
    tempFolder = os.path.join(directory, str(uuid.uuid4()))
    view.displayMessage("Moving files to temporary location %s..." % tempFolder)

    mover = FileMover(mp3files, tempFolder)
    tempFiles = mover.move()

    view.displayDone()
    view.displayMessage("Finding non MP3 files...")

    nonMp3FilesFilter = NonMp3FileFilter(fileSource)
    nonMp3Files = nonMp3FilesFilter.getFiles()

    for file in nonMp3Files:
        os.remove(file)

    view.displayDone()

    view.displayMessage("Directory contains ")
    view.displayMessage("\033[1;31m" + str(len(nonMp3Files)) + "\033[1;m")
    view.displayMessage(" non-MP3 files. Deleting...")

    view.displayDone()

    view.displayMessage("Organizing files...")

    organizer = Organizer(tempFiles, directory)
    organizer.organize()

    view.displayDone()

if __name__ == "__main__":
    Main()


