#! /usr/bin/env python3
# coding=utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(500, 300)
    w.setWindowTitle(u'第一个例子')
    w.show()

    sys.exit(app.exec_())