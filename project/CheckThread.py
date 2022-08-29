from project.LinkChecker import checkProcess
from PyQt6.QtCore import QThread, pyqtSignal


class CheckThread(QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal()

    def __init__(self):
        super(CheckThread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        checkProcess()
        self._signal.emit()
