# coding:utf-8
# get App MainWindow for Max2019, Maya2017, Houdini14.0.598
# WeChat: WendyAndAndy (TAsThinking, iJasonLee)

import os
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMayaUI as mui

os.environ['QT_PREFERRED_BINDING'] = 'PySide'
#default_order = ("PySide2", "PyQt5", "PySide", "PyQt4")

try:
    mayaVersion = int(cmds.about(v=True)[:4])
    if mayaVersion < 2014:
        os.environ['QT_PREFERRED_BINDING'] = 'PyQt4'
    elif mayaVersion >= 2014 and mayaVersion < 2017:
        os.environ['QT_PREFERRED_BINDING'] = 'PySide'
    else:
        os.environ['QT_PREFERRED_BINDING'] = 'PySide2'
except:
    pass


def getMaxMainWindow():
    import MaxPlus
    return MaxPlus.GetQMaxMainWindow()


def getMayaMainWindow():
    mayaMainWindow = None
    mayaVersion = int(cmds.about(v=True)[:4])
    if 2011 <= mayaVersion < 2014:
        import sip
        from PyQt4.QtGui import QWidget
        mayaMainWindow = sip.wrapinstance(long(mui.MQtUtil.mainWindow()), QWidget)
    elif 2014 <= mayaVersion < 2017:
        import shiboken
        from PySide.QtGui import QWidget
        mayaMainWindow = shiboken.wrapInstance(long(mui.MQtUtil.mainWindow()), QWidget)
    elif mayaVersion >= 2017:
        import shiboken2
        from PySide2.QtWidgets import QWidget
        mayaMainWindow = shiboken2.wrapInstance(long(mui.MQtUtil.mainWindow()), QWidget)
    return mayaMainWindow


def getHoudiniMainWindow():
    from PySide import QtGui
    app = QtGui.QApplication.instance()
    if app:
        parent = app.topLevelAt(QtGui.QCursor().pos())
        if parent:
            return parent
        else:
            # root = app.desktop()
            ws = [w for w in app.topLevelWidgets() if w.windowTitle().count('Houdini') and w.windowType().name == 'Window']
            if ws:
                return ws[0]