#!/usr/bin/env python

from PyQt4 import QtCore, QtGui


class FormView(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        browseButton = self.createButton("&Browse...", self.browse)

        goButton = self.createButton("&Go", self.browse)

        self.outputBrowser = QtGui.QTextBrowser()
        
        self.directoryComboBox = self.createComboBox(QtCore.QDir.currentPath())

        self.createFilesTable()


        mainLayout = QtGui.QGridLayout()

        mainLayout.addWidget(self.directoryComboBox, 2, 1)
        mainLayout.addWidget(browseButton, 2, 2)
        mainLayout.addWidget(goButton, 2, 3)
        mainLayout.addWidget(self.outputBrowser, 3, 0, 1, 4)
        mainLayout.addWidget(self.filesTable, 4, 0, 1, 4)

        self.setLayout(mainLayout)

        self.setWindowTitle("MonkeyBeats")
        self.resize(700, 300)

    def browse(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, "Find Files",
                QtCore.QDir.currentPath())

        if directory:
            if self.directoryComboBox.findText(directory) == -1:
                self.directoryComboBox.addItem(directory)

            self.directoryComboBox.setCurrentIndex(self.directoryComboBox.findText(directory))

    @staticmethod
    def updateComboBox(comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

    def createComboBox(self, text=""):
        comboBox = QtGui.QComboBox()
        comboBox.setEditable(True)
        comboBox.addItem(text)
        comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        return comboBox

    def createFilesTable(self):
        self.filesTable = QtGui.QTableWidget(0, 4)
        self.filesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        self.filesTable.setHorizontalHeaderLabels(("File", "Artist", "Album", "Title"))
        self.filesTable.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid(True)

        #self.filesTable.cellActivated.connect(self.openFile) 



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = FormView()
    window.show()
    sys.exit(app.exec_())
