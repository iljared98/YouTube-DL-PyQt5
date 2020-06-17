import youtube_dl
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object): # Generator code from PyQt 5 generator and Qt Designer
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 296)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.urlBox = QtWidgets.QTextEdit(self.centralwidget)
        self.urlBox.setGeometry(QtCore.QRect(10, 40, 571, 91))
        self.urlBox.setObjectName("urlBox")

        self.entryLabel = QtWidgets.QLabel(self.centralwidget)
        self.entryLabel.setGeometry(QtCore.QRect(-10, 10, 191, 31))
        self.entryLabel.setObjectName("entryLabel")

        self.selectLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectLabel.setGeometry(QtCore.QRect(610, 20, 121, 20))
        self.selectLabel.setObjectName("selectLabel")

        '''
        self.downloadBar = QtWidgets.QProgressBar(self.centralwidget)
        self.downloadBar.setGeometry(QtCore.QRect(10, 200, 571, 23))
        self.downloadBar.setProperty("value", 0)
        self.downloadBar.setOrientation(QtCore.Qt.Horizontal)
        self.downloadBar.setInvertedAppearance(False)
        self.downloadBar.setObjectName("downloadBar")
        '''

        self.folderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.folderBtn.setGeometry(QtCore.QRect(620, 140, 101, 51))
        self.folderBtn.setObjectName("folderBtn")
        self.folderBtn.clicked.connect(lambda: self.selectDir())

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(590, 10, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.currentLbl = QtWidgets.QLabel(self.centralwidget)
        self.currentLbl.setGeometry(QtCore.QRect(10, 160, 151, 31))
        self.currentLbl.setObjectName("currentLbl")

        self.downloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downloadBtn.setGeometry(QtCore.QRect(620, 200, 101, 51))
        self.downloadBtn.setObjectName("downloadBtn")
        self.downloadBtn.clicked.connect(lambda: self.downFunc())

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(620, 40, 101, 91))
        self.widget.setObjectName("widget")

        self.selectLayout = QtWidgets.QVBoxLayout(self.widget)
        self.selectLayout.setContentsMargins(0, 0, 0, 0)
        self.selectLayout.setObjectName("selectLayout")

        self.mp3Select = QtWidgets.QRadioButton(self.widget)
        self.mp3Select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mp3Select.setObjectName("mp3Select")

        self.selectLayout.addWidget(self.mp3Select)
        self.mp4Select = QtWidgets.QRadioButton(self.widget)
        self.mp4Select.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mp4Select.setObjectName("mp4Select")
        self.selectLayout.addWidget(self.mp4Select)

        self.webmSelect = QtWidgets.QRadioButton(self.widget)
        self.webmSelect.setObjectName("webmSelect")
        self.selectLayout.addWidget(self.webmSelect)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout_Help = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Help.setObjectName("menuAbout_Help")
        MainWindow.setMenuBar(self.menubar)
        self.actionh = QtWidgets.QAction(MainWindow)
        self.actionh.setObjectName("actionh")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_ = QtWidgets.QAction(MainWindow)
        self.actionExit_.setObjectName("actionExit_")
        self.actionExit_.triggered.connect(lambda: self.exitFunc())
        self.menuFile.addAction(self.actionExit_)
        self.menuAbout_Help.addAction(self.actionHelp)
        self.menuAbout_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout_Help.menuAction())
        self.actionHelp.triggered.connect(lambda: self.helpFunc())
        self.actionAbout.triggered.connect(lambda: self.aboutFunc())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.entryLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Enter Youtube URLs</span></p></body></html>"))
        self.selectLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Select Format</span></p></body></html>"))
        self.folderBtn.setText(_translate("MainWindow", "Select\n"
"Destination"))
        self.currentLbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\"></span></p></body></html>"))
        self.downloadBtn.setText(_translate("MainWindow", "Download\n"
"Videos"))
        self.mp3Select.setText(_translate("MainWindow", "  .mp3"))
        self.mp4Select.setText(_translate("MainWindow", "  .mp4"))
        self.webmSelect.setText(_translate("MainWindow", ".webm"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout_Help.setTitle(_translate("MainWindow", "Help"))
        self.actionh.setText(_translate("MainWindow", "h"))
        self.actionExit.setText(_translate("MainWindow", "About & Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About "))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_.setText(_translate("MainWindow", "Exit"))

    def exitFunc(self):
        exit(0)

    def helpFunc(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Instructions")
        msg.setInformativeText("1. Copy-paste your YouTube URLs into the text box (one URL per line)\n2. Select your desired download format (video: mp4/webm, audio: mp3)\n3. Select the directory where you want the program to download your files.\n4. Click the download button and wait until the task completes! Depending on the length of the video the process may take awhile.")
        msg.setWindowTitle("Help")
        msg.exec_()

    def aboutFunc(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("YouTube Downloader PyQt5")
        msg.setInformativeText('Author : https://github.com/iljared98\nGUI YouTube Downloader program built using the PyQt5 and Youtube-dl libraries.')
        msg.setWindowTitle("About")
        msg.exec_()

    def selectDir(self):
        dialog = QFileDialog()
        self.downDir = dialog.getExistingDirectory(None, "Select Folder")
        return str(self.downDir)

    def downFunc(self):
        try:
            ytURLs = self.urlBox.toPlainText()
            urlList = ytURLs.split('\n')

            if ytURLs != '':

                if self.mp3Select.isChecked() == True:

                    ydl_opts = {
                        'noplaylist': True,
                        'outtmpl': f'{self.downDir}/%(title)s.%(ext)s',
                        'nocheckcertificate': True,
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }

                    self.currentLbl.setText(f'<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Download in progess, please wait...</span></p></body></html>')
                    self.currentLbl.adjustSize()
                    for url in range(len(urlList)):
                        urlString = str(urlList[url])
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([urlString])

                    self.currentLbl.setText('')
                    self.currentLbl.adjustSize()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Task Finished")
                    msg.setInformativeText('The YouTube download is complete!')
                    msg.setWindowTitle("Download Complete")
                    msg.exec_()

                elif self.mp4Select.isChecked():

                    ydl_opts = {
                        'noplaylist': True,
                        'outtmpl': f'{self.downDir}/%(title)s.%(ext)s',
                        'nocheckcertificate': True,
                        'postprocessors': [{
                            'key': 'FFmpegVideoConvertor',
                            'preferedformat': 'mp4'
                        }],
                    }

                    self.currentLbl.setText(f'<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Download in progess, please wait...</span></p></body></html>')
                    self.currentLbl.adjustSize()
                    for url in range(len(urlList)):
                        urlString = str(urlList[url])
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([urlString])

                    self.currentLbl.setText('')
                    self.currentLbl.adjustSize()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Task Finished")
                    msg.setInformativeText('The YouTube download is complete!')
                    msg.setWindowTitle("Download Complete")
                    msg.exec_()

                elif self.webmSelect.isChecked():
                    ydl_opts = {
                        'noplaylist': True,
                        'outtmpl': f'{self.downDir}/%(title)s.%(ext)s',
                        'nocheckcertificate': True,
                        'postprocessors': [{
                            'key': 'FFmpegVideoConvertor',
                            'preferedformat': 'webm'
                        }],
                    }

                    self.currentLbl.setText(f'<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Download in progess, please wait...</span></p></body></html>')
                    self.currentLbl.adjustSize()
                    for url in range(len(urlList)):
                        urlString = str(urlList[url])
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([urlString])

                    self.currentLbl.setText('')
                    self.currentLbl.adjustSize()
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Task Finished")
                    msg.setInformativeText('The YouTube download is complete!')
                    msg.setWindowTitle("Download Complete")
                    msg.exec_()

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Invalid Input")
                    msg.setInformativeText('Please check a media format, and try again.')
                    msg.setWindowTitle("ERROR")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Invalid Input")
                msg.setInformativeText('Please enter at least one Youtube URL into the text field.')
                msg.setWindowTitle("ERROR")
                msg.exec_()


        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Invalid Input")
            msg.setInformativeText('Please check your input (one Youtube URL per line), provide a valid directory, and try again.')
            msg.setWindowTitle("ERROR")
            msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
