# coding:utf-8
# description ...
# jason.li@neobards.cn | 2019.08.01

import os
import sys
import lib
reload(lib)

from Qt import QtGui, QtWidgets, QtCore
# in maya2016 PySide, Chinese characters display in garbage characters
try:
    QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
except:
    pass

import xxx_ui as ui
reload(ui)

_ver = '2019.08.01.01'
########################################################################
class Win(QtWidgets.QWidget, ui.Ui_Form):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent = None):
        """Constructor"""
        super(Win, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(self.windowTitle() + _ver)
        if parent:
            self.setWindowFlags(parent.windowFlags())
        self.connect_actions()
            
    # ----------------------------------------------------------------------
    def connect_actions(self):
        """"""
        # self.btnCreateMat.clicked.connect(self.btnCreateMat_click)
        
    # ----------------------------------------------------------------------
    def btnCreateMat_click(self):
        """"""
        print('btnCreateMat_click')



# ----------------------------------------------------------------------
def main():
    """"""
    global win
    try:
        win.close()
    except:
        pass
    win = Win(lib.getMayaMainWindow())
    win.show()


if __name__ == '__main__':
    main()    
            
    
