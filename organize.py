import uuid
import sys
import os

from errors import *
from fileFilters import *
from fileMover import *
from organizer import *
from emptyDirectoryRemover import *
from views.consoleView import ConsoleView
from views.formView import FormView
from options import OptionsLoader

def Main():
    # Parse command line arguments into program options
    optionsLoader = OptionsLoader()
    options = optionsLoader.loadFromArguments(sys.argv)

    view = ConsoleView()

    if options.startGuiMode:
        print "Gui mode not implemented yet."
        return
    
    directory = options.rootDirectory
    if not os.path.isdir(directory):
        view.displayLine("Directory not found")
        return

    view.displayLine("Directory to organize is {0}".format(directory))
    view.displayLine("Retrieving all MP3 files...")
    
    fileSource = FileSource(directory, options.followSymbolicLinks)
    filter = Mp3FileFilter(fileSource)
    mp3files = filter.getFiles()

    view.displayLine("Directory contains {0} MP3 files".format(len(mp3files)))
    
    tempFolder = os.path.join(directory, str(uuid.uuid4()))
    view.displayLine("Moving files to temporary location {0}...".format(tempFolder))

    mover = FileMover(mp3files, tempFolder)
    tempFiles = mover.move()

    view.displayLine("Finding non MP3 files...")

    nonMp3FilesFilter = NonMp3FileFilter(fileSource)
    nonMp3Files = nonMp3FilesFilter.getFiles()

    if options.backupLocation is not None and os.path.isdir(options.backupLocation):
        view.displayLine("Backing up {0} non-MP3 files to {1}".format(len(nonMp3Files), options.backupLocation))
        backupMover = FileMover(nonMp3Files, options.backupLocation)
        backupMover.move()
    else:
        view.displayLine("Directory contains {0} non-MP3 files. Deleting...".format(len(nonMp3Files)))
        for file in nonMp3Files:
            os.remove(file)

    view.displayLine("Organizing files...")

    organizer = Organizer(tempFiles, directory)
    organizer.organize()

    view.displayLine("Removing empty directories...")

    dirRemover = EmptyDirectoryRemover(directory)
    dirRemover.remove()

    view.displayLine("Done!")

if __name__ == "__main__":
    Main()


