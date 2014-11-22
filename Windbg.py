from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import phonon
from PyQt4.phonon import *
import PyQt4.QtWebKit
from PyQt4.QtWebKit import QWebView

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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.setEnabled(True)
        TabWidget.resize(1099, 741)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("8514oem"))
        TabWidget.setFont(font)
        TabWidget.setToolTip(_fromUtf8(""))
        TabWidget.setStyleSheet(_fromUtf8("\n"
" \n"
"bottomFrame {\n"
"border: none;\n"
"background: white;\n"
"}\n"
"QLabel {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QLabel:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QLabel:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"#topFrame {\n"
"border: none;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #a6a6a6, stop: 0.08 #7f7f7f,\n"
"stop: 0.39999 #717171, stop: 0.4 #626262,\n"
"stop: 0.9 #4c4c4c, stop: 1 #333333);\n"
"}\n"
" \n"
"#bottomFrame {\n"
"border: none;\n"
"background: white;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 5px; /* move to the right by 5px */\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }\n"
"\n"
" /* make use of negative margins for overlapping tabs */\n"
" QTabBar::tab:selected {\n"
"     /* expand/overlap to the left and right by 4px */\n"
"     margin-left: -4px;\n"
"     margin-right: -4px;\n"
" }\n"
"\n"
" QTabBar::tab:first:selected {\n"
"     margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
" }\n"
"\n"
" QTabBar::tab:last:selected {\n"
"     margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
" }\n"
"\n"
" QTabBar::tab:only-one {\n"
"     margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
" }"))
        TabWidget.setTabPosition(QtGui.QTabWidget.North)
        TabWidget.setDocumentMode(False)
        TabWidget.setTabsClosable(False)
        TabWidget.setMovable(False)
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_14)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.tab_14)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_22 = QtGui.QLabel(self.frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 3, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.frame)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.frame)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame)
        self.label_23.setStyleSheet(_fromUtf8("QLabel {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QLabel:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QLabel:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.frame)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout.addWidget(self.label_31, 3, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.frame)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout.addWidget(self.label_28, 0, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.frame)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout.addWidget(self.label_33, 1, 4, 1, 1)
        self.label_36 = QtGui.QLabel(self.frame)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout.addWidget(self.label_36, 4, 4, 1, 1)
        self.label_30 = QtGui.QLabel(self.frame)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout.addWidget(self.label_30, 4, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.frame)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 1, 2, 1, 1)
        self.label_38 = QtGui.QLabel(self.frame)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout.addWidget(self.label_38, 5, 4, 1, 1)
        self.label_32 = QtGui.QLabel(self.frame)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout.addWidget(self.label_32, 5, 2, 1, 1)
        self.label_35 = QtGui.QLabel(self.frame)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout.addWidget(self.label_35, 2, 4, 1, 1)
        self.label_29 = QtGui.QLabel(self.frame)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.label_29, 2, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 5, 1, 1, 1)
        self.label_37 = QtGui.QLabel(self.frame)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 3, 4, 1, 1)
        self.label_24 = QtGui.QLabel(self.frame)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 4, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.frame)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout.addWidget(self.label_34, 0, 4, 1, 1)
        self.label_17 = QtGui.QLabel(self.frame)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        TabWidget.addTab(self.tab_14, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.ld_1 = QtGui.QPushButton(self.tab_2)
        self.ld_1.setGeometry(QtCore.QRect(0, 10, 481, 51))
        self.ld_1.setObjectName(_fromUtf8("ld_1"))
        self.ld_2 = QtGui.QPushButton(self.tab_2)
        self.ld_2.setGeometry(QtCore.QRect(0, 70, 481, 51))
        self.ld_2.setObjectName(_fromUtf8("ld_2"))
        self.sym_2 = QtGui.QPushButton(self.tab_2)
        self.sym_2.setGeometry(QtCore.QRect(0, 190, 481, 51))
        self.sym_2.setObjectName(_fromUtf8("sym_2"))
        self.sym_1 = QtGui.QPushButton(self.tab_2)
        self.sym_1.setGeometry(QtCore.QRect(0, 130, 481, 61))
        self.sym_1.setObjectName(_fromUtf8("sym_1"))
        self.sym_3 = QtGui.QPushButton(self.tab_2)
        self.sym_3.setGeometry(QtCore.QRect(0, 240, 481, 41))
        self.sym_3.setObjectName(_fromUtf8("sym_3"))
        self.textEdit = Qsci.QsciScintilla(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 630, 971, 81))
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(992, 627, 161, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        TabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        TabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        TabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        TabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        TabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        TabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        TabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        TabWidget.addTab(self.tab_10, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        TabWidget.addTab(self.tab_11, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        TabWidget.addTab(self.tab_12, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        TabWidget.addTab(self.tab_16, _fromUtf8(""))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        TabWidget.addTab(self.tab_15, _fromUtf8(""))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        TabWidget.addTab(self.tab_17, _fromUtf8(""))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        TabWidget.addTab(self.tab_18, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        TabWidget.addTab(self.tab_19, _fromUtf8(""))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        TabWidget.addTab(self.tab_20, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        TabWidget.addTab(self.tab_21, _fromUtf8(""))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        TabWidget.addTab(self.tab_22, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        TabWidget.addTab(self.tab_23, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        TabWidget.addTab(self.tab_24, _fromUtf8(""))
        self.tab_25 = QtGui.QWidget()
        self.tab_25.setObjectName(_fromUtf8("tab_25"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_25)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        TabWidget.addTab(self.tab_25, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.label_22.setText(_translate("TabWidget", "7) Symbols", None))
        self.label_25.setText(_translate("TabWidget", "11) Process related information", None))
        self.label_19.setText(_translate("TabWidget", "4) Expressions and commands", None))
        self.label_18.setToolTip(_translate("TabWidget", "<html><head/><body><p>Starting with the 6.6.07 version of the debugger a new mechanism for enhancing output from the debugger and extensions was included: DML. <br/>DML allows output to include directives and extra non-display information in the form of tags. <br/>Debugger user interfaces parse out the extra information to provide new behaviors. <br/><br/>DML is primarily intended to address two issues: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Linking of related information </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Discoverability of debugger and extension functionality</li></ul></body></html>", None))
        self.label_18.setText(_translate("TabWidget", "5) Debugger markup language (DML) ", None))
        self.label_21.setText(_translate("TabWidget", "8) Sources", None))
        self.label_16.setToolTip(_translate("TabWidget", "<html><head/><body><p>(show version, clear screen, etc.)</p></body></html>", None))
        self.label_16.setText(_translate("TabWidget", "2) General WinDbg\'s commands", None))
        self.label_23.setText(_translate("TabWidget", "10) Loaded modules\n"
" and image information", None))
        self.label_20.setText(_translate("TabWidget", "6) Main extensions", None))
        self.label_10.setToolTip(_translate("TabWidget", "<html><head/><body><p>(attach, detach, ..)</p></body></html>", None))
        self.label_10.setText(_translate("TabWidget", "3) Debugging sessions", None))
        self.label_31.setText(_translate("TabWidget", "17) Information about variables", None))
        self.label_28.setToolTip(_translate("TabWidget", "<html><head/><body><p>Each step executes either a single assembly instruction or a single source line, depending on whether the debugger is in assembly mode or source mode. <br/>Use the l+t and l-t commands or the buttons on the WinDbg toolbar to switch between these modes.</p></body></html>", None))
        self.label_28.setText(_translate("TabWidget", "14) Tracing and stepping (F10, F11) ", None))
        self.label_33.setToolTip(_translate("TabWidget", "<html><head/><body><p>Application Verifier profiles and tracks Microsoft Win32 APIs (heap, handles, locks, threads, DLL load/unload, and more), Exceptions, Kernel objects, Registry, File system. With the !avrf extension we get access to this tracking information!</p></body></html>", None))
        self.label_33.setText(_translate("TabWidget", "21) Application Verifier ", None))
        self.label_36.setText(_translate("TabWidget", "Credits", None))
        self.label_30.setText(_translate("TabWidget", "18) Memory", None))
        self.label_27.setText(_translate("TabWidget", "15) Call stack", None))
        self.label_38.setText(_translate("TabWidget", "Website Auther", None))
        self.label_32.setText(_translate("TabWidget", "19) Manipulating memory ranges", None))
        self.label_35.setToolTip(_translate("TabWidget", "<html><head/><body><p>You must enable the following options for you image in GFlags: <br/>-&gt; &quot;Create user mode stack trace database&quot; <br/>-&gt; &quot;Stack Backtrace: (Megs)&quot; -&gt; 10 <br/>-&gt; It seems that you sometimes also need to check and specify the &quot;Debugger&quot; field in GFlags</p></body></html>", None))
        self.label_35.setText(_translate("TabWidget", "22) Logging extension (logexts.dll) ", None))
        self.label_29.setText(_translate("TabWidget", "16) Registers", None))
        self.label_26.setText(_translate("TabWidget", "13) Breakpoints", None))
        self.label_37.setText(_translate("TabWidget", "Ekstra", None))
        self.label_24.setText(_translate("TabWidget", "12) Thread related information", None))
        self.label_34.setText(_translate("TabWidget", "20) Memory: Heap", None))
        self.label_17.setText(_translate("TabWidget", "1.Built-in help commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_14), _translate("TabWidget", "Overview", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "1. Built-in help commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "2. General WinDbg\'s commands", None))
        self.ld_1.setText(_translate("TabWidget", "Command ld\n"
"Load symbols for Module", None))
        self.ld_2.setText(_translate("TabWidget", "Command ld\n"
"Load symbols for all Modules", None))
        self.sym_2.setText(_translate("TabWidget", "!sym noisy", None))
        self.sym_1.setText(_translate("TabWidget", "Command !sym \n"
"Get state of symbol loading ", None))
        self.sym_3.setText(_translate("TabWidget", "!sym quiet ", None))
        self.pushButton.setText(_translate("TabWidget", "Run own command \n"
" to iDA Pro", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "3. Expressions and commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", " 4. Debugger markup language (DML) ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "5. Main extensions", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_5), _translate("TabWidget", "6. Symbols", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_6), _translate("TabWidget", "7. Sources", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_7), _translate("TabWidget", "8 Exceptions, events, and crash analysis", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_8), _translate("TabWidget", "9. Loaded modules and image information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_9), _translate("TabWidget", "10. Process related information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_10), _translate("TabWidget", "11. Thread related information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_11), _translate("TabWidget", "12.Breakpoints", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_12), _translate("TabWidget", "13.Tracing and stepping (F10, F11) ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_16), _translate("TabWidget", "14.Call stack", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_15), _translate("TabWidget", "15. Registers", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_17), _translate("TabWidget", "16.Information about variables", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_18), _translate("TabWidget", "17.Memory", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_19), _translate("TabWidget", "18.Manipulating memory ranges", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_20), _translate("TabWidget", "19.Memory: Heap", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_21), _translate("TabWidget", "20.Application Verifier ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_22), _translate("TabWidget", "21.Logging extension", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_23), _translate("TabWidget", "Extra", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_24), _translate("TabWidget", "Credits", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_25), _translate("TabWidget", "Authers Website", None))
from PyQt4 import QtCore, QtGui
from PyQt4 import Qsci
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import phonon
from PyQt4.phonon import *
import PyQt4.QtWebKit
from PyQt4.QtWebKit import QWebView



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

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.setEnabled(True)
        TabWidget.resize(1165, 751)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("8514oem"))
        TabWidget.setFont(font)
        TabWidget.setToolTip(_fromUtf8(""))
        TabWidget.setStyleSheet(_fromUtf8("\n"
" \n"
"bottomFrame {\n"
"border: none;\n"
"background: white;\n"
"}\n"
"QLabel {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QLabel:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QLabel:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}\n"
"\n"
"#topFrame {\n"
"border: none;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #a6a6a6, stop: 0.08 #7f7f7f,\n"
"stop: 0.39999 #717171, stop: 0.4 #626262,\n"
"stop: 0.9 #4c4c4c, stop: 1 #333333);\n"
"}\n"
" \n"
"#bottomFrame {\n"
"border: none;\n"
"background: white;\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px solid #C2C7CB;\n"
" }\n"
"\n"
" QTabWidget::tab-bar {\n"
"     left: 5px; /* move to the right by 5px */\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 2px solid #C4C4C3;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                 stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: #9B9B9B;\n"
"     border-bottom-color: #C2C7CB; /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }\n"
"\n"
" /* make use of negative margins for overlapping tabs */\n"
" QTabBar::tab:selected {\n"
"     /* expand/overlap to the left and right by 4px */\n"
"     margin-left: -4px;\n"
"     margin-right: -4px;\n"
" }\n"
"\n"
" QTabBar::tab:first:selected {\n"
"     margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
" }\n"
"\n"
" QTabBar::tab:last:selected {\n"
"     margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
" }\n"
"\n"
" QTabBar::tab:only-one {\n"
"     margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
" }"))
        TabWidget.setTabPosition(QtGui.QTabWidget.North)
        TabWidget.setDocumentMode(False)
        TabWidget.setTabsClosable(False)
        TabWidget.setMovable(False)
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_14)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.tab_14)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_22 = QtGui.QLabel(self.frame)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout.addWidget(self.label_22, 0, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.frame)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout.addWidget(self.label_25, 3, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.frame)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.frame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout.addWidget(self.label_18, 4, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.frame)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.frame)
        self.label_23.setStyleSheet(_fromUtf8("QLabel {\n"
"color: #333;\n"
"border: 2px solid #555;\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
"min-width: 80px;\n"
"}\n"
" \n"
"QLabel:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb);\n"
"}\n"
" \n"
"QLabel:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd);\n"
"}"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout.addWidget(self.label_23, 2, 1, 1, 1)
        self.label_20 = QtGui.QLabel(self.frame)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout.addWidget(self.label_20, 5, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_31 = QtGui.QLabel(self.frame)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout.addWidget(self.label_31, 3, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.frame)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout.addWidget(self.label_28, 0, 2, 1, 1)
        self.label_33 = QtGui.QLabel(self.frame)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout.addWidget(self.label_33, 1, 4, 1, 1)
        self.label_36 = QtGui.QLabel(self.frame)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout.addWidget(self.label_36, 4, 4, 1, 1)
        self.label_30 = QtGui.QLabel(self.frame)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout.addWidget(self.label_30, 4, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.frame)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout.addWidget(self.label_27, 1, 2, 1, 1)
        self.label_38 = QtGui.QLabel(self.frame)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout.addWidget(self.label_38, 5, 4, 1, 1)
        self.label_32 = QtGui.QLabel(self.frame)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout.addWidget(self.label_32, 5, 2, 1, 1)
        self.label_35 = QtGui.QLabel(self.frame)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout.addWidget(self.label_35, 2, 4, 1, 1)
        self.label_29 = QtGui.QLabel(self.frame)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.label_29, 2, 2, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 5, 1, 1, 1)
        self.label_37 = QtGui.QLabel(self.frame)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout.addWidget(self.label_37, 3, 4, 1, 1)
        self.label_24 = QtGui.QLabel(self.frame)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout.addWidget(self.label_24, 4, 1, 1, 1)
        self.label_34 = QtGui.QLabel(self.frame)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout.addWidget(self.label_34, 0, 4, 1, 1)
        self.label_17 = QtGui.QLabel(self.frame)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        TabWidget.addTab(self.tab_14, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.ld_1 = QtGui.QPushButton(self.tab_2)
        self.ld_1.setGeometry(QtCore.QRect(0, 10, 481, 51))
        self.ld_1.setObjectName(_fromUtf8("ld_1"))
        self.ld_2 = QtGui.QPushButton(self.tab_2)
        self.ld_2.setGeometry(QtCore.QRect(0, 70, 481, 51))
        self.ld_2.setObjectName(_fromUtf8("ld_2"))
        self.sym_2 = QtGui.QPushButton(self.tab_2)
        self.sym_2.setGeometry(QtCore.QRect(0, 190, 481, 51))
        self.sym_2.setObjectName(_fromUtf8("sym_2"))
        self.sym_1 = QtGui.QPushButton(self.tab_2)
        self.sym_1.setGeometry(QtCore.QRect(0, 130, 481, 61))
        self.sym_1.setObjectName(_fromUtf8("sym_1"))
        self.sym_3 = QtGui.QPushButton(self.tab_2)
        self.sym_3.setGeometry(QtCore.QRect(0, 240, 481, 41))
        self.sym_3.setObjectName(_fromUtf8("sym_3"))
        self.textEdit = Qsci.QsciScintilla(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 630, 971, 81))
        self.textEdit.setToolTip(_fromUtf8(""))
        self.textEdit.setWhatsThis(_fromUtf8(""))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(992, 627, 161, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        TabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        TabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        TabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        TabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        TabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        TabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        TabWidget.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        TabWidget.addTab(self.tab_10, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        TabWidget.addTab(self.tab_11, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        TabWidget.addTab(self.tab_12, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        TabWidget.addTab(self.tab_16, _fromUtf8(""))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        TabWidget.addTab(self.tab_15, _fromUtf8(""))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        TabWidget.addTab(self.tab_17, _fromUtf8(""))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        TabWidget.addTab(self.tab_18, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        TabWidget.addTab(self.tab_19, _fromUtf8(""))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        TabWidget.addTab(self.tab_20, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        TabWidget.addTab(self.tab_21, _fromUtf8(""))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        TabWidget.addTab(self.tab_22, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        TabWidget.addTab(self.tab_23, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        TabWidget.addTab(self.tab_24, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(23)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.label_22.setText(_translate("TabWidget", "7) Symbols", None))
        self.label_25.setText(_translate("TabWidget", "11) Process related information", None))
        self.label_19.setText(_translate("TabWidget", "4) Expressions and commands", None))
        self.label_18.setToolTip(_translate("TabWidget", "<html><head/><body><p>Starting with the 6.6.07 version of the debugger a new mechanism for enhancing output from the debugger and extensions was included: DML. <br/>DML allows output to include directives and extra non-display information in the form of tags. <br/>Debugger user interfaces parse out the extra information to provide new behaviors. <br/><br/>DML is primarily intended to address two issues: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Linking of related information </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Discoverability of debugger and extension functionality</li></ul></body></html>", None))
        self.label_18.setText(_translate("TabWidget", "5) Debugger markup language (DML) ", None))
        self.label_21.setText(_translate("TabWidget", "8) Sources", None))
        self.label_16.setToolTip(_translate("TabWidget", "<html><head/><body><p>(show version, clear screen, etc.)</p></body></html>", None))
        self.label_16.setText(_translate("TabWidget", "2) General WinDbg\'s commands", None))
        self.label_23.setText(_translate("TabWidget", "10) Loaded modules\n"
" and image information", None))
        self.label_20.setText(_translate("TabWidget", "6) Main extensions", None))
        self.label_10.setToolTip(_translate("TabWidget", "<html><head/><body><p>(attach, detach, ..)</p></body></html>", None))
        self.label_10.setText(_translate("TabWidget", "3) Debugging sessions", None))
        self.label_31.setText(_translate("TabWidget", "17) Information about variables", None))
        self.label_28.setToolTip(_translate("TabWidget", "<html><head/><body><p>Each step executes either a single assembly instruction or a single source line, depending on whether the debugger is in assembly mode or source mode. <br/>Use the l+t and l-t commands or the buttons on the WinDbg toolbar to switch between these modes.</p></body></html>", None))
        self.label_28.setText(_translate("TabWidget", "14) Tracing and stepping (F10, F11) ", None))
        self.label_33.setToolTip(_translate("TabWidget", "<html><head/><body><p>Application Verifier profiles and tracks Microsoft Win32 APIs (heap, handles, locks, threads, DLL load/unload, and more), Exceptions, Kernel objects, Registry, File system. With the !avrf extension we get access to this tracking information!</p></body></html>", None))
        self.label_33.setText(_translate("TabWidget", "21) Application Verifier ", None))
        self.label_36.setText(_translate("TabWidget", "Credits", None))
        self.label_30.setText(_translate("TabWidget", "18) Memory", None))
        self.label_27.setText(_translate("TabWidget", "15) Call stack", None))
        self.label_38.setText(_translate("TabWidget", "Website Auther", None))
        self.label_32.setText(_translate("TabWidget", "19) Manipulating memory ranges", None))
        self.label_35.setToolTip(_translate("TabWidget", "<html><head/><body><p>You must enable the following options for you image in GFlags: <br/>-&gt; &quot;Create user mode stack trace database&quot; <br/>-&gt; &quot;Stack Backtrace: (Megs)&quot; -&gt; 10 <br/>-&gt; It seems that you sometimes also need to check and specify the &quot;Debugger&quot; field in GFlags</p></body></html>", None))
        self.label_35.setText(_translate("TabWidget", "22) Logging extension (logexts.dll) ", None))
        self.label_29.setText(_translate("TabWidget", "16) Registers", None))
        self.label_26.setText(_translate("TabWidget", "13) Breakpoints", None))
        self.label_37.setText(_translate("TabWidget", "Ekstra", None))
        self.label_24.setText(_translate("TabWidget", "12) Thread related information", None))
        self.label_34.setText(_translate("TabWidget", "20) Memory: Heap", None))
        self.label_17.setText(_translate("TabWidget", "1.Built-in help commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_14), _translate("TabWidget", "Overview", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "1. Built-in help commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "2. General WinDbg\'s commands", None))
        self.ld_1.setText(_translate("TabWidget", "Command ld\n"
"Load symbols for Module", None))
        self.ld_2.setText(_translate("TabWidget", "Command ld\n"
"Load symbols for all Modules", None))
        self.sym_2.setText(_translate("TabWidget", "!sym noisy", None))
        self.sym_1.setText(_translate("TabWidget", "Command !sym \n"
"Get state of symbol loading ", None))
        self.sym_3.setText(_translate("TabWidget", "!sym quiet ", None))
        self.pushButton.setText(_translate("TabWidget", "Run own command \n"
" to iDA Pro", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "3. Expressions and commands", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", " 4. Debugger markup language (DML) ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "5. Main extensions", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_5), _translate("TabWidget", "6. Symbols", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_6), _translate("TabWidget", "7. Sources", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_7), _translate("TabWidget", "8 Exceptions, events, and crash analysis", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_8), _translate("TabWidget", "9. Loaded modules and image information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_9), _translate("TabWidget", "10. Process related information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_10), _translate("TabWidget", "11. Thread related information", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_11), _translate("TabWidget", "12.Breakpoints", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_12), _translate("TabWidget", "13.Tracing and stepping (F10, F11) ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_16), _translate("TabWidget", "14.Call stack", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_15), _translate("TabWidget", "15. Registers", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_17), _translate("TabWidget", "16.Information about variables", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_18), _translate("TabWidget", "17.Memory", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_19), _translate("TabWidget", "18.Manipulating memory ranges", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_20), _translate("TabWidget", "19.Memory: Heap", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_21), _translate("TabWidget", "20.Application Verifier ", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_22), _translate("TabWidget", "21.Logging extension", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_23), _translate("TabWidget", "Extra", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_24), _translate("TabWidget", "Credits", None))



        '''commands'''
        self.ld_1.clicked.connect(self.Ld1)
        self.ld_2.clicked.connect(self.Ld2)
        #self.sym_2.clicked.connect(self.Sym2)
        #self.sym_1.clicked.connect(self.Sym1)
        #self.sym_3.clicked.connect(self.Sym3)


        '''define commands'''
    def Ld1(self):
        Message(SendDbgCommand("ld *"))

    def Ld2(self):
        Message(SendDbgCommand("!sym"))


from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    app.exec_()


