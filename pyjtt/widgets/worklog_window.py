# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worklog_window.ui'
#
# Created: Fri Jun 13 14:59:45 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WorklogWindow(object):
    def setupUi(self, WorklogWindow):
        WorklogWindow.setObjectName("WorklogWindow")
        WorklogWindow.resize(430, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WorklogWindow.sizePolicy().hasHeightForWidth())
        WorklogWindow.setSizePolicy(sizePolicy)
        WorklogWindow.setMinimumSize(QtCore.QSize(430, 360))
        WorklogWindow.setMaximumSize(QtCore.QSize(600, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icons/clock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WorklogWindow.setWindowIcon(icon)
        WorklogWindow.setWhatsThis("")
        self.gridLayout = QtWidgets.QGridLayout(WorklogWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelIssue = QtWidgets.QLabel(WorklogWindow)
        self.labelIssue.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelIssue.setObjectName("labelIssue")
        self.verticalLayout.addWidget(self.labelIssue)
        self.line = QtWidgets.QFrame(WorklogWindow)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(3, -1, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelDate = QtWidgets.QLabel(WorklogWindow)
        self.labelDate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDate.setObjectName("labelDate")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelDate)
        self.dateEdit = QtWidgets.QDateEdit(WorklogWindow)
        self.dateEdit.setWrapping(False)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setContentsMargins(-1, -1, 3, -1)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.labelStart = QtWidgets.QLabel(WorklogWindow)
        self.labelStart.setObjectName("labelStart")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelStart)
        self.timeStartEdit = QtWidgets.QTimeEdit(WorklogWindow)
        self.timeStartEdit.setWrapping(True)
        self.timeStartEdit.setCalendarPopup(False)
        self.timeStartEdit.setObjectName("timeStartEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.timeStartEdit)
        self.labelEnd = QtWidgets.QLabel(WorklogWindow)
        self.labelEnd.setObjectName("labelEnd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEnd)
        self.timeEndEdit = QtWidgets.QTimeEdit(WorklogWindow)
        self.timeEndEdit.setEnabled(True)
        self.timeEndEdit.setWrapping(True)
        self.timeEndEdit.setObjectName("timeEndEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.timeEndEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelComment = QtWidgets.QLabel(WorklogWindow)
        self.labelComment.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelComment.setObjectName("labelComment")
        self.verticalLayout_3.addWidget(self.labelComment)
        self.plainTextCommentEdit = QtWidgets.QPlainTextEdit(WorklogWindow)
        self.plainTextCommentEdit.setObjectName("plainTextCommentEdit")
        self.verticalLayout_3.addWidget(self.plainTextCommentEdit)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.labelSpent = QtWidgets.QLabel(WorklogWindow)
        self.labelSpent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSpent.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.labelSpent.setObjectName("labelSpent")
        self.gridLayout.addWidget(self.labelSpent, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(WorklogWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(WorklogWindow)
        QtCore.QMetaObject.connectSlotsByName(WorklogWindow)

    def retranslateUi(self, WorklogWindow):
        _translate = QtCore.QCoreApplication.translate
        WorklogWindow.setWindowTitle(_translate("WorklogWindow", "Some Worklog"))
        self.labelIssue.setText(_translate("WorklogWindow", "ISSUE: SUMMARY"))
        self.labelDate.setText(_translate("WorklogWindow", "Date:"))
        self.dateEdit.setDisplayFormat(_translate("WorklogWindow", "MM/dd/yyyy"))
        self.labelStart.setText(_translate("WorklogWindow", "Start time"))
        self.timeStartEdit.setDisplayFormat(_translate("WorklogWindow", "hh:mm"))
        self.labelEnd.setText(_translate("WorklogWindow", "End time"))
        self.timeEndEdit.setDisplayFormat(_translate("WorklogWindow", "hh:mm"))
        self.labelComment.setText(_translate("WorklogWindow", "Comment:"))
        self.labelSpent.setText(_translate("WorklogWindow", "Time Spent :"))

from . import pyjtt_res_rc
