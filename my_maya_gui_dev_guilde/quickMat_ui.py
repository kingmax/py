# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\NBTATOOLS\Maya\all\python\NB2\quickMat.ui'
#
# Created: Thu Aug  1 18:36:17 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCompat, QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(430, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnUseObjectName = QtWidgets.QPushButton(Form)
        self.btnUseObjectName.setObjectName("btnUseObjectName")
        self.horizontalLayout_3.addWidget(self.btnUseObjectName)
        self.btnUseSceneName = QtWidgets.QPushButton(Form)
        self.btnUseSceneName.setObjectName("btnUseSceneName")
        self.horizontalLayout_3.addWidget(self.btnUseSceneName)
        self.btnUseRootName = QtWidgets.QPushButton(Form)
        self.btnUseRootName.setObjectName("btnUseRootName")
        self.horizontalLayout_3.addWidget(self.btnUseRootName)
        self.btnRemoveSuffix = QtWidgets.QPushButton(Form)
        self.btnRemoveSuffix.setObjectName("btnRemoveSuffix")
        self.horizontalLayout_3.addWidget(self.btnRemoveSuffix)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblMatName = QtWidgets.QLabel(Form)
        self.lblMatName.setObjectName("lblMatName")
        self.horizontalLayout.addWidget(self.lblMatName)
        self.txtMatName = QtWidgets.QLineEdit(Form)
        self.txtMatName.setObjectName("txtMatName")
        self.horizontalLayout.addWidget(self.txtMatName)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblPreset = QtWidgets.QLabel(Form)
        self.lblPreset.setObjectName("lblPreset")
        self.horizontalLayout_2.addWidget(self.lblPreset)
        self.cbPreset = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbPreset.sizePolicy().hasHeightForWidth())
        self.cbPreset.setSizePolicy(sizePolicy)
        self.cbPreset.setObjectName("cbPreset")
        self.horizontalLayout_2.addWidget(self.cbPreset)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.txtUsage = QtWidgets.QPlainTextEdit(Form)
        self.txtUsage.setEnabled(False)
        self.txtUsage.setReadOnly(True)
        self.txtUsage.setObjectName("txtUsage")
        self.gridLayout.addWidget(self.txtUsage, 6, 0, 1, 1)
        self.btnCreateMat = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCreateMat.sizePolicy().hasHeightForWidth())
        self.btnCreateMat.setSizePolicy(sizePolicy)
        self.btnCreateMat.setMinimumSize(QtCore.QSize(0, 50))
        self.btnCreateMat.setObjectName("btnCreateMat")
        self.gridLayout.addWidget(self.btnCreateMat, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCompat.translate("Form", "快速创建材质", None, -1))
        self.btnUseObjectName.setText(QtCompat.translate("Form", "使用物体名", None, -1))
        self.btnUseSceneName.setText(QtCompat.translate("Form", "使用场景名", None, -1))
        self.btnUseRootName.setToolTip(QtCompat.translate("Form", "使用当前物体的最顶层父级名", None, -1))
        self.btnUseRootName.setText(QtCompat.translate("Form", "使用顶级名", None, -1))
        self.btnRemoveSuffix.setToolTip(QtCompat.translate("Form", "移除名称中最后以_或__开始部分", None, -1))
        self.btnRemoveSuffix.setText(QtCompat.translate("Form", "移除_后缀", None, -1))
        self.lblMatName.setText(QtCompat.translate("Form", "材质名称：", None, -1))
        self.lblPreset.setText(QtCompat.translate("Form", "材质预设：", None, -1))
        self.txtUsage.setPlainText(QtCompat.translate("Form", "使用说明:\n"
"0.正确命名需要指定材质的物体\n"
"1.选中该物体(仅1个,默认材质名将使用物件名字)\n"
"2.确认材质名称正确,根据需要进行修改\n"
"3.根据需要选择引擎对应的材质预设\n"
"4.创建材质,会根据名称自动连接需要的各种贴图,\n"
"同时设置RE材质预设数据", None, -1))
        self.btnCreateMat.setText(QtCompat.translate("Form", "创建材质,连接贴图", None, -1))

