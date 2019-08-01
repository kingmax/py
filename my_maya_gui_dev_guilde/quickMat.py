# coding:utf-8
# quick mat for Escape
# jason.li@neobards.cn | 2019.08.01

import os
import sys
import lib
reload(lib)

from Qt import QtGui, QtWidgets, QtCore, QtCompat
# in maya2016 PySide, Chinese characters display in garbage characters
try:
    QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("UTF-8"))
except:
    pass

import quickMat_ui
reload(quickMat_ui)

_ver = '2019.08.01.01'
########################################################################
class Win(QtWidgets.QWidget, quickMat_ui.Ui_Form):
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
            
        # super(Win, self).__init__(parent)
        # ui = __file__.rsplit('.', 1)[0] + '.ui'
        # QtCompat.loadUi(ui, self)
        # if parent:
            # self.setWindowFlags(parent.windowFlags())
            
    # ----------------------------------------------------------------------
    def connect_actions(self):
        """"""
        self.btnUseObjectName.clicked.connect(self.btnUseObjectName_click)
        self.btnUseSceneName.clicked.connect(self.btnUseSceneName_click)
        self.btnUseRootName.clicked.connect(self.btnUseRootName_click)
        self.btnRemoveSuffix.clicked.connect(self.btnRemoveSuffix_click)
        self.btnCreateMat.clicked.connect(self.btnCreateMat_click)
        
    # ----------------------------------------------------------------------
    def btnUseObjectName_click(self):
        """"""
        print('btnUseObjectName_click')

    # ----------------------------------------------------------------------
    def btnUseSceneName_click(self):
        """"""
        print('btnUseSceneName_click')

    # ----------------------------------------------------------------------
    def btnUseRootName_click(self):
        """"""
        print('btnUseRootName_click')

    # ----------------------------------------------------------------------
    def btnRemoveSuffix_click(self):
        """"""
        print('btnRemoveSuffix_click')

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
            
    
    