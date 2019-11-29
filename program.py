#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtCore import QObject, QUrl, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickView

if __name__ == "__main__":
    
    app = QApplication(sys.argv) # load app

    engine = QQmlApplicationEngine() # create qml engine

    engine.load("view.qml") # load qml desing
    win = engine.rootObjects()[0] # set root object

    win.show()
    sys.exit(app.exec_())