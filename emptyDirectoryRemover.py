class EmptyDirectoryRemover:
    """ Removes the empty directories within the specified location."""
    def __init__(self, location):
        self.location = location

    def remove(self):
        for path, dirs, files in os.walk(location):
            if len(files) == 0:
                shutil.rmtree(path, ignore_errors=True)
        
