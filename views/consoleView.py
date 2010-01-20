import sys

class ConsoleView:
    def __init__(self):
        self.usage = "Usage: %s <directory>" % sys.argv[0]

    def displayUsage(self):
        print usage

    def displayDone(self):
        print "\033[1;31mdone\033[1;m" # print red

    def displayMessage(self, message):
        sys.stdout.write(message)
        sys.stdout.flush()

    def displayLine(self, line):
        print line
        
    
