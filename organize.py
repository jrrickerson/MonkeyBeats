import eyeD3
import uuid
import sys
import os
from errors import *
from fileFilters import *
from fileMover import *
from organizer import *
from views.consoleView import ConsoleView
from views.formView import FormView

def Main():
    usage = "Usage: %s (-g|<directory>)" % sys.argv[0]
    view = ConsoleView()

    if len(sys.argv) != 2:
        view.displayLine(usage)
        return
    directoryOrGui = sys.argv[1]
    if sys.argv[1] == "-g":
        print "Gui mode not implemented yet."
        return
    
    if not os.path.isdir(directory):
        view.displayLine("Directory not found")
        view.displayLine(usage)
        return

    view.displayLine("Directory to organize is %s" % directory)
    view.displayLine("Retrieving all MP3 files...")
    
    fileSource = FileSource(directory)
    filter = Mp3FileFilter(fileSource)
    mp3files = filter.getFiles()

    view.displayLine("Directory contains %s MP3 files" % len(mp3files))
    
    tempFolder = os.path.join(directory, str(uuid.uuid4()))
    view.displayLine("Moving files to temporary location %s..." % tempFolder)

    mover = FileMover(mp3files, tempFolder)
    tempFiles = mover.move()

    view.displayLine("Finding non MP3 files...")

    nonMp3FilesFilter = NonMp3FileFilter(fileSource)
    nonMp3Files = nonMp3FilesFilter.getFiles()

    for file in nonMp3Files:
        os.remove(file)

    view.displayLine("Directory contains %s non-MP3 files. Deleting..."
                     % len(nonMp3Files))
    view.displayLine("Organizing files...")

    organizer = Organizer(tempFiles, directory)
    organizer.organize()

    view.displayLine("Done!")

if __name__ == "__main__":
    Main()


