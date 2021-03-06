# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ProgressDialog
                                 A QGIS plugin
 demo toshow progress bar
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-01-06
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Zoltan Siki
        email                : siki1958@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import time

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'progress_dialog_base.ui'))


class ProgressDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ProgressDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.startButton.clicked.connect(self.proc)

    def proc(self):
        self.progressBar.reset()
        for i in range(101):
            self.progressBar.setValue(i)
            # do something useful here instead of sleep
            time.sleep(0.2)
