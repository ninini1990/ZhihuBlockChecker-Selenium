# Form implementation generated from reading ui file 'ZhihuBlockChecker.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/img/logo.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_UserId = QtWidgets.QLabel(self.centralwidget)
        self.label_UserId.setGeometry(QtCore.QRect(10, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_UserId.setFont(font)
        self.label_UserId.setObjectName("label_UserId")
        self.lineEdit_UserId = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_UserId.setGeometry(QtCore.QRect(80, 20, 151, 20))
        self.lineEdit_UserId.setObjectName("lineEdit_UserId")
        self.label_ResultPath = QtWidgets.QLabel(self.centralwidget)
        self.label_ResultPath.setGeometry(QtCore.QRect(10, 50, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_ResultPath.setFont(font)
        self.label_ResultPath.setObjectName("label_ResultPath")
        self.lineEdit_ResultPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ResultPath.setGeometry(QtCore.QRect(80, 50, 151, 20))
        self.lineEdit_ResultPath.setReadOnly(True)
        self.lineEdit_ResultPath.setObjectName("lineEdit_ResultPath")
        self.label_SelectPage = QtWidgets.QLabel(self.centralwidget)
        self.label_SelectPage.setGeometry(QtCore.QRect(10, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_SelectPage.setFont(font)
        self.label_SelectPage.setObjectName("label_SelectPage")
        self.checkBox_answers = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_answers.setGeometry(QtCore.QRect(80, 90, 70, 18))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.checkBox_answers.setFont(font)
        self.checkBox_answers.setChecked(False)
        self.checkBox_answers.setObjectName("checkBox_answers")
        self.checkBox_posts = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_posts.setGeometry(QtCore.QRect(140, 90, 70, 18))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.checkBox_posts.setFont(font)
        self.checkBox_posts.setObjectName("checkBox_posts")
        self.checkBox_zvideos = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_zvideos.setGeometry(QtCore.QRect(80, 120, 70, 18))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.checkBox_zvideos.setFont(font)
        self.checkBox_zvideos.setObjectName("checkBox_zvideos")
        self.label_interval = QtWidgets.QLabel(self.centralwidget)
        self.label_interval.setGeometry(QtCore.QRect(10, 160, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_interval.setFont(font)
        self.label_interval.setObjectName("label_interval")
        self.label_minInterval = QtWidgets.QLabel(self.centralwidget)
        self.label_minInterval.setGeometry(QtCore.QRect(40, 190, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_minInterval.setFont(font)
        self.label_minInterval.setObjectName("label_minInterval")
        self.lineEdit_minInterval = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_minInterval.setGeometry(QtCore.QRect(80, 190, 31, 20))
        self.lineEdit_minInterval.setReadOnly(True)
        self.lineEdit_minInterval.setPlaceholderText("")
        self.lineEdit_minInterval.setObjectName("lineEdit_minInterval")
        self.label_maxInterval = QtWidgets.QLabel(self.centralwidget)
        self.label_maxInterval.setGeometry(QtCore.QRect(140, 190, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_maxInterval.setFont(font)
        self.label_maxInterval.setObjectName("label_maxInterval")
        self.lineEdit_maxInterval = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_maxInterval.setGeometry(QtCore.QRect(180, 190, 31, 20))
        self.lineEdit_maxInterval.setObjectName("lineEdit_maxInterval")
        self.label_chromePath = QtWidgets.QLabel(self.centralwidget)
        self.label_chromePath.setGeometry(QtCore.QRect(10, 230, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_chromePath.setFont(font)
        self.label_chromePath.setObjectName("label_chromePath")
        self.lineEdit_chromePath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_chromePath.setGeometry(QtCore.QRect(10, 250, 221, 20))
        self.lineEdit_chromePath.setReadOnly(True)
        self.lineEdit_chromePath.setObjectName("lineEdit_chromePath")
        self.label_chromeIpPort = QtWidgets.QLabel(self.centralwidget)
        self.label_chromeIpPort.setGeometry(QtCore.QRect(10, 280, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.label_chromeIpPort.setFont(font)
        self.label_chromeIpPort.setObjectName("label_chromeIpPort")
        self.label_chromeIp = QtWidgets.QLabel(self.centralwidget)
        self.label_chromeIp.setGeometry(QtCore.QRect(10, 300, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_chromeIp.setFont(font)
        self.label_chromeIp.setObjectName("label_chromeIp")
        self.lineEdit_chromeIp = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_chromeIp.setGeometry(QtCore.QRect(30, 300, 101, 20))
        self.lineEdit_chromeIp.setReadOnly(True)
        self.lineEdit_chromeIp.setObjectName("lineEdit_chromeIp")
        self.label_chromePort = QtWidgets.QLabel(self.centralwidget)
        self.label_chromePort.setGeometry(QtCore.QRect(140, 300, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.label_chromePort.setFont(font)
        self.label_chromePort.setObjectName("label_chromePort")
        self.lineEdit_chromePort = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_chromePort.setGeometry(QtCore.QRect(180, 300, 51, 20))
        self.lineEdit_chromePort.setPlaceholderText("")
        self.lineEdit_chromePort.setObjectName("lineEdit_chromePort")
        self.pushButton_saveConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveConfig.setEnabled(True)
        self.pushButton_saveConfig.setGeometry(QtCore.QRect(130, 340, 91, 23))
        self.pushButton_saveConfig.setObjectName("pushButton_saveConfig")
        self.pushButton_launchBrowser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_launchBrowser.setGeometry(QtCore.QRect(130, 390, 91, 23))
        self.pushButton_launchBrowser.setObjectName("pushButton_launchBrowser")
        self.pushButton_doCheck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_doCheck.setGeometry(QtCore.QRect(130, 440, 91, 23))
        self.pushButton_doCheck.setObjectName("pushButton_doCheck")
        self.checkBox_pins = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_pins.setGeometry(QtCore.QRect(140, 120, 91, 18))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.checkBox_pins.setFont(font)
        self.checkBox_pins.setObjectName("checkBox_pins")
        self.textBrowser_showLog = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_showLog.setGeometry(QtCore.QRect(250, 10, 471, 481))
        self.textBrowser_showLog.setObjectName("textBrowser_showLog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_help_doc = QtGui.QAction(MainWindow)
        self.action_help_doc.setObjectName("action_help_doc")
        self.action_help_about = QtGui.QAction(MainWindow)
        self.action_help_about.setObjectName("action_help_about")
        self.menu.addAction(self.action_help_doc)
        self.menu.addAction(self.action_help_about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " 知乎屏蔽检查工具（by 尼尼尼@知乎)"))
        self.label_UserId.setText(_translate("MainWindow", "知乎用户ID"))
        self.lineEdit_UserId.setPlaceholderText(_translate("MainWindow", "输入个人主页链接中的用户ID"))
        self.label_ResultPath.setText(_translate("MainWindow", "结果路径"))
        self.lineEdit_ResultPath.setPlaceholderText(_translate("MainWindow", "保存到桌面"))
        self.label_SelectPage.setText(_translate("MainWindow", "选择检查项"))
        self.checkBox_answers.setText(_translate("MainWindow", "回答"))
        self.checkBox_posts.setText(_translate("MainWindow", "文章"))
        self.checkBox_zvideos.setText(_translate("MainWindow", "视频"))
        self.label_interval.setText(_translate("MainWindow", "检查间隔(最小一秒)"))
        self.label_minInterval.setText(_translate("MainWindow", "最小值"))
        self.lineEdit_minInterval.setText(_translate("MainWindow", "1"))
        self.label_maxInterval.setText(_translate("MainWindow", "最大值"))
        self.lineEdit_maxInterval.setText(_translate("MainWindow", "3"))
        self.lineEdit_maxInterval.setPlaceholderText(_translate("MainWindow", "3"))
        self.label_chromePath.setText(_translate("MainWindow", "Chorme安装地址"))
        self.lineEdit_chromePath.setPlaceholderText(_translate("MainWindow", "C:\\Program Files (x86)\\Google\\Chrome\\Application"))
        self.label_chromeIpPort.setText(_translate("MainWindow", "Chrome监听地址/端口"))
        self.label_chromeIp.setText(_translate("MainWindow", "IP"))
        self.lineEdit_chromeIp.setPlaceholderText(_translate("MainWindow", "127.0.0.1"))
        self.label_chromePort.setText(_translate("MainWindow", "端口"))
        self.lineEdit_chromePort.setText(_translate("MainWindow", "8888"))
        self.pushButton_saveConfig.setText(_translate("MainWindow", "1. 保存设置"))
        self.pushButton_launchBrowser.setText(_translate("MainWindow", "2. 启动浏览器"))
        self.pushButton_doCheck.setText(_translate("MainWindow", "3. 执行检查"))
        self.checkBox_pins.setText(_translate("MainWindow", "想法(不建议)"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.action_help_doc.setText(_translate("MainWindow", "使用说明"))
        self.action_help_about.setText(_translate("MainWindow", "关于"))
