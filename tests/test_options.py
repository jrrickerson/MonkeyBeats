import unittest
import nose

from options import OptionsLoader

# Fixture setup and teardown
def setUpModule():
    pass
def tearDownModule():
    pass

class OptionsLoaderTestFixture(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def verifyOptionsAreDefaultValues(self, options):
        defaultRootDirectory = "."
        defaultBackupLocation = ""
        defaultFollowSymbolicLinksFlag = False
        defaultGuiModeFlag = False

        self.assertEqual(defaultRootDirectory, options.rootDirectory, "Root directory doesn't match default")
        self.assertEqual(defaultBackupLocation, options.backupLocation, "Backup directory doesn't match default")
        self.assertEqual(defaultFollowSymbolicLinksFlag, options.followSymbolicLinks, 
            "Follow links flag doesn't match default")
        self.assertEqual(defaultGuiModeFlag, options.startGuiMode, "Gui mode flag doesn't match default")

    def testDirectoryOption(self):
        expectedDirectoryValue = "~/music/"
        shortArguments = ["organize", "-d", expectedDirectoryValue]
        longArguments = ["organize", "--directory", expectedDirectoryValue]
        loader = OptionsLoader()

        options = loader.loadFromArguments(shortArguments)
        self.assertEqual(expectedDirectoryValue, options.rootDirectory, "Root directory option value mismatch")

        options = loader.loadFromArguments(longArguments)
        self.assertEqual(expectedDirectoryValue, options.rootDirectory, "Root directory option value mismatch")

    def testBackupOption(self):
        expectedDirectoryValue = "~/backups/"
        shortArguments = ["organize", "-b", expectedDirectoryValue]
        longArguments = ["organize", "--backup", expectedDirectoryValue]
        loader = OptionsLoader()

        options = loader.loadFromArguments(shortArguments)
        self.assertEqual(expectedDirectoryValue, options.backupLocation, "Backup directory option value mismatch")

        options = loader.loadFromArguments(longArguments)
        self.assertEqual(expectedDirectoryValue, options.backupLocation, "Backup directory option value mismatch")

    def testFollowLinksOption(self):
        expectedFlagValue = True
        shortArguments = ["organize", "-f"]
        longArguments = ["organize", "--followLinks"]
        loader = OptionsLoader()

        options = loader.loadFromArguments(shortArguments)
        self.assertEqual(expectedFlagValue, options.followSymbolicLinks, "Follow Symbolic Links flag not activated")

        options = loader.loadFromArguments(longArguments)
        self.assertEqual(expectedFlagValue, options.followSymbolicLinks, "Follow Symbolic Links flag not activated")

    def testGuiModeOption(self):
        expectedFlagValue = True
        shortArguments = ["organize", "-g"]
        longArguments = ["organize", "--gui"]
        loader = OptionsLoader()

        options = loader.loadFromArguments(shortArguments)
        self.assertEqual(expectedFlagValue, options.startGuiMode, "Gui Mode flag not activated")

        options = loader.loadFromArguments(longArguments)
        self.assertEqual(expectedFlagValue, options.startGuiMode, "Gui Mode flag not activated")
        
    def testNoOptionsSpecified(self):
        argumentsList = ["organize"]

        loader = OptionsLoader()
        options = loader.loadFromArguments(argumentsList)
        
        self.verifyOptionsAreDefaultValues(options)

    def testAllOptionsSpecified(self):
        expectedDirectory = "~/downloads/music"
        expectedBackupDirectory = "~/backups"
        expectedGuiModeFlag = True
        expectedFollowLinksFlag = True

        argumentsList = ["organize", "-gf", "-d", expectedDirectory, "-b", expectedBackupDirectory]

        loader = OptionsLoader()
        options = loader.loadFromArguments(argumentsList)

        self.assertEqual(expectedGuiModeFlag, options.startGuiMode, "Gui Mode flag not activated")
        self.assertEqual(expectedFollowLinksFlag, options.followSymbolicLinks, "Follow Symbolic Links flag not activated")
        self.assertEqual(expectedDirectory, options.rootDirectory, "Root directory option value mismatch")
        self.assertEqual(expectedBackupDirectory, options.backupLocation, "Backup directory option value mismatch")
