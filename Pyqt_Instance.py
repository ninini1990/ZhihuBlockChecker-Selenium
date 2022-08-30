import sys
sys.path.append('./venv/Lib/site-packages')
import webbrowser

# Windows任务栏图标
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QTextCursor

from util.CommonUitl import convertPageName
from util.JsonUtil import getJsonUserOption, writeJsonUserOption
from ZhihuBlockChecker import Ui_MainWindow
from project.BrowserHandler import launchBrowser
from project.CheckThread import CheckThread

stdOutTemp = sys.stdout


class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))
        QApplication.processEvents()  # 实时刷新界面


class Pyqt_Instance(QMainWindow, Ui_MainWindow):

    # 帮助菜单中的“使用说明"
    @pyqtSlot()
    def on_action_help_doc_triggered(self):
        webbrowser.open('file://' + __file__ + '/../resource/doc/README.html')

    # 帮助菜单中的”关于“
    @pyqtSlot()
    def on_action_help_about_triggered(self):
        reply = QMessageBox()
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        reply.about(self, '关于', '作者：尼尼尼@知乎 <br><a href="https://www.zhihu.com/people/nidaye2">(个人主页)</a>')

    # 保存用户设置的slot
    def on_pushButton_saveConfig_pressed(self):
        reply = QMessageBox()
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        # 获取用户选择的检查项
        inputList = []
        if (self.checkBox_answers.isChecked() == True):
            opt1 = 'answers'
            inputList.append(opt1)
        if (self.checkBox_posts.isChecked() == True):
            opt2 = 'posts'
            inputList.append(opt2)
        if (self.checkBox_zvideos.isChecked() == True):
            opt3 = 'zvideos'
            inputList.append(opt3)
        if (self.checkBox_pins.isChecked() == True):
            opt4 = 'pins'
            inputList.append(opt4)

        if(len(inputList) == 0 ):
            raise (Exception, '错误：至少需要选择一个检查类型')

        selectedPageName = ''
        cnPageNameStr=''
        for item in inputList:
            if(inputList.index(item) == 0):
                selectedPageName = item
                cnPageNameStr = convertPageName(item)
            else:
                selectedPageName = selectedPageName + ',' + item
                cnPageNameStr = cnPageNameStr + '，' + convertPageName(item)


        optDict = getJsonUserOption()
        optDict['zhihuUserId'] = self.lineEdit_UserId.text()
        optDict['selectedPageName'] = selectedPageName
        optDict['minDelayTime'] = self.lineEdit_minInterval.text()
        optDict['maxDelayTime'] = self.lineEdit_maxInterval.text()
        optDict['browserPort'] = self.lineEdit_chromePort.text()

        try:
            for v in optDict.values():
                if (len(v) == 0):
                    raise(Exception, '用户设置有误，请检查！')
            writeJsonUserOption(optDict)
            print("用户设置保存成功, 待检查项为：{0}".format(cnPageNameStr))
            reply.information(self, "成功", "用户设置保存成功")
        except Exception as e:
            print(e)
            reply.critical(self, "错误", "用户设置有误，请检查！")

    # 从已保存设置中取值填充到用户界面
    def fillUiConfig(self):
        print('从已保存设置中取值填充到用户界面')
        optDict = getJsonUserOption()
        self.lineEdit_UserId.setText(optDict['zhihuUserId'])
        self.lineEdit_minInterval.setText(optDict['minDelayTime'])
        self.lineEdit_maxInterval.setText(optDict['maxDelayTime'])
        self.lineEdit_chromePort.setText(optDict['browserPort'])

        pageNameStr = optDict['selectedPageName']
        if ('answers' in pageNameStr):
            self.checkBox_answers.setChecked(True)
        if ('posts' in pageNameStr):
            self.checkBox_posts.setChecked(True)
        if ('zvideos' in pageNameStr):
            self.checkBox_zvideos.setChecked(True)
        if ('pins' in pageNameStr):
            self.checkBox_pins.setChecked(True)

    # 启动浏览器的slot
    def on_pushButton_launchBrowser_pressed(self):
        reply = QMessageBox()
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        try:
            launchBrowser()
            print("启动浏览器成功，请在浏览器中登录知乎账户。如已为登录状态，则点击“执行检查“按钮开始检查。")
            reply.information(self, "成功", "启动浏览器成功，请在浏览器中登录知乎账户。<br>如已为登录状态，则点击“执行检查“按钮开始检查。")
        except Exception as e:
            print(e)
            reply.critical(self, "错误", "启动浏览器错误，请检查！")

    # 检查结束后的处理
    def endCheck(self):
        reply = QMessageBox()
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        reply.information(self, "成功", "执行检查完毕，请查看桌面上的结果文件")
        self.pushButton_saveConfig.setEnabled(True)
        self.pushButton_launchBrowser.setEnabled(True)
        self.pushButton_doCheck.setEnabled(True)

    # 执行检查的slot
    def on_pushButton_doCheck_pressed(self):
        self.pushButton_saveConfig.setEnabled(False)
        self.pushButton_launchBrowser.setEnabled(False)
        self.pushButton_doCheck.setEnabled(False)
        reply = QMessageBox()
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        try:
            # checkProcess()
            self.t = CheckThread()
            self.t._signal.connect(self.endCheck)
            self.t.daemon = True
            self.t.start()
        except Exception as e:
            print(e)
            reply.critical(self, "错误", "执行检查错误，请检查日志中错误信息！")

    # 重写closeEvent
    def closeEvent(self, event):
        sys.stdout = stdOutTemp
        super().closeEvent(event)

    def onUpdateEdit(self, text):
        self.textBrowser_showLog.append(text)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height());
        sys.stdout = Stream(newText=self.onUpdateEdit)
        self.fillUiConfig()


# 定义程序入口函数
def main():
    app = QApplication(sys.argv)
    myForm = Pyqt_Instance()
    myForm.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()



