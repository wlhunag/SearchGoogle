# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan 13 12:09:55 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(932, 619)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/rock.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView_2 = QtWebKit.QWebView(self.centralwidget)
        self.webView_2.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView_2.setObjectName(_fromUtf8("webView_2"))
        self.gridLayout.addWidget(self.webView_2, 1, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_F = QtGui.QMenu(self.menubar)
        self.menu_F.setObjectName(_fromUtf8("menu_F"))
        self.menu_H = QtGui.QMenu(self.menubar)
        self.menu_H.setObjectName(_fromUtf8("menu_H"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setAcceptDrops(True)
        self.dockWidget.setWindowIcon(icon)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setKerning(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.QuestionText = QtGui.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QuestionText.setFont(font)
        self.QuestionText.setObjectName(_fromUtf8("QuestionText"))
        self.gridLayout_3.addWidget(self.QuestionText, 1, 0, 1, 3)
        self.examtitle = QtGui.QLineEdit(self.tab)
        self.examtitle.setDragEnabled(True)
        self.examtitle.setObjectName(_fromUtf8("examtitle"))
        self.gridLayout_3.addWidget(self.examtitle, 0, 1, 1, 2)
        self.pushButton_savefile = QtGui.QPushButton(self.tab)
        self.pushButton_savefile.setObjectName(_fromUtf8("pushButton_savefile"))
        self.gridLayout_3.addWidget(self.pushButton_savefile, 2, 0, 1, 1)
        self.pushButton_search = QtGui.QPushButton(self.tab)
        self.pushButton_search.setObjectName(_fromUtf8("pushButton_search"))
        self.gridLayout_3.addWidget(self.pushButton_search, 2, 1, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 235))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.radioButton100 = QtGui.QRadioButton(self.tab_2)
        self.radioButton100.setObjectName(_fromUtf8("radioButton100"))
        self.verticalLayout.addWidget(self.radioButton100)
        self.radioButtonall = QtGui.QRadioButton(self.tab_2)
        self.radioButtonall.setObjectName(_fromUtf8("radioButtonall"))
        self.verticalLayout.addWidget(self.radioButtonall)
        self.radioButton75 = QtGui.QRadioButton(self.tab_2)
        self.radioButton75.setObjectName(_fromUtf8("radioButton75"))
        self.verticalLayout.addWidget(self.radioButton75)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton_clear = QtGui.QPushButton(self.tab_2)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout_4.addWidget(self.pushButton_clear, 0, 1, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(False)
        self.gridLayout_4.addWidget(self.treeWidget, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.action_N = QtGui.QAction(MainWindow)
        self.action_N.setObjectName(_fromUtf8("action_N"))
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_A = QtGui.QAction(MainWindow)
        self.action_A.setObjectName(_fromUtf8("action_A"))
        self.action_H = QtGui.QAction(MainWindow)
        self.action_H.setObjectName(_fromUtf8("action_H"))
        self.action_X = QtGui.QAction(MainWindow)
        self.action_X.setObjectName(_fromUtf8("action_X"))
        self.menu_F.addAction(self.action_N)
        self.menu_F.addAction(self.action_X)
        self.menu_H.addAction(self.action_A)
        self.menu_H.addAction(self.action_H)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "查考題", None))
        self.menu_F.setTitle(_translate("MainWindow", "檔案(&F)", None))
        self.menu_H.setTitle(_translate("MainWindow", "說明(&H)", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Loosen 搜尋", None))
        self.label_2.setText(_translate("MainWindow", "考試名稱：", None))
        self.pushButton_savefile.setText(_translate("MainWindow", "儲存題目", None))
        self.pushButton_search.setText(_translate("MainWindow", "開始搜尋(&G)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "題目", None))
        self.label.setText(_translate("MainWindow", "符合程度", None))
        self.radioButton100.setText(_translate("MainWindow", "100%", None))
        self.radioButtonall.setText(_translate("MainWindow", "75%", None))
        self.radioButton75.setText(_translate("MainWindow", "All", None))
        self.pushButton_clear.setToolTip(_translate("MainWindow", "這將會清空資料庫!", None))
        self.pushButton_clear.setText(_translate("MainWindow", "清除所有結果", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "搜尋結果", None))
        self.action_N.setText(_translate("MainWindow", "開新檔案(&N)", None))
        self.action.setText(_translate("MainWindow", "開啟檔案", None))
        self.action_A.setText(_translate("MainWindow", "關於本程式(&A)", None))
        self.action_H.setText(_translate("MainWindow", "使用說明(&H)", None))
        self.action_X.setText(_translate("MainWindow", "離開(&X)", None))

from PyQt4 import QtWebKit
