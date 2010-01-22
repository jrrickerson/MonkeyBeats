from optparse import OptionParser

class Options:
    def __init__(self):
        self.startGuiMode = False
        self.backupLocation = ""
        self.followSymbolicLinks = False
        self.rootDirectory = "."

class OptionsLoader:
    def loadFromArguments(self, argumentList):
        options = Options()
        self._intializeCommandLineParser()
        (options, args) = self._parser.parse_args(argumentList)
        return options

    def loadFromConfigurationFile(self, file):
        raise RuntimeException("Not yet implemented")

    def _intializeCommandLineParser(self):
        self._parser = OptionParser()
        self._parser.add_option("-g", "--gui", dest="startGuiMode",
            help="Start in GUI mode", action="store_true")
        self._parser.add_option("-f", "--followLinks", dest="followSymbolicLinks",
            help="Follow symbolic links to target directories", action="store_true")
        self._parser.add_option("-b", "--backup", dest="backupLocation",
            metavar="BACKUP_DIR", help="Backup unrelated files to BACKUP_DIR")
        self._parser.add_option("-d", "--directory", dest="rootDirectory",
            metavar="ROOT_DIR", help="Search for files starting in ROOT_DIR [default %default]")
        self._parser.set_defaults(startGuiMode=False, followSymbolicLinks=False, backupLocation="",
            rootDirectory=".")

