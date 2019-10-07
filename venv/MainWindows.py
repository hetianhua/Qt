# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from testing import Ui_MainWindow  # 主窗口
from config_diag import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def __get_config(self):
        # name = self.deviceEdit.text()  # 获取text控件内容 #
        # if name:
        #     self.deviceEdit.clear()  # 清除控件内容 #
        # else:
        #     print("device can't be NULL ")
        pass

    def sstartbutton_clock(self):
        print("go!")

    def saveButton_click(self):
        print("go!")

    def setButton_click(self):
        print("go!")

    def newfileButton_click(self):
        self.newfile = FileDiag()
        self.newfile.setDocumentMode(False)
        self.newfile.show()


class FileDiag(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def accept(self):
        name = self.deviceEdit.text()  # 获取text控件内容 #
        if name:
            # 如果有的话就把变量存下来 #
            self.deviceEdit.clear()  # 清除控件内容 #
        else:
            QMessageBox.warning(self, "警告QQQ", "device can't be NULL")
            # self.close()

    def reject(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
