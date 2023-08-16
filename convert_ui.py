# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(362, 206)
        font = QFont()
        font.setFamilies([u"Noto Sans"])
        Form.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.textEdit_path = QTextEdit(Form)
        self.textEdit_path.setObjectName(u"textEdit_path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_path.sizePolicy().hasHeightForWidth())
        self.textEdit_path.setSizePolicy(sizePolicy1)
        self.textEdit_path.setMaximumSize(QSize(16777215, 30))
        self.textEdit_path.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit_path)

        self.pushButton_openpath = QPushButton(Form)
        self.pushButton_openpath.setObjectName(u"pushButton_openpath")
        sizePolicy.setHeightForWidth(self.pushButton_openpath.sizePolicy().hasHeightForWidth())
        self.pushButton_openpath.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_openpath)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_edit = QRadioButton(self.groupBox)
        self.radioButton_edit.setObjectName(u"radioButton_edit")
        sizePolicy2.setHeightForWidth(self.radioButton_edit.sizePolicy().hasHeightForWidth())
        self.radioButton_edit.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.radioButton_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.spinBox_editfrom = QSpinBox(self.groupBox)
        self.spinBox_editfrom.setObjectName(u"spinBox_editfrom")
        sizePolicy2.setHeightForWidth(self.spinBox_editfrom.sizePolicy().hasHeightForWidth())
        self.spinBox_editfrom.setSizePolicy(sizePolicy2)
        self.spinBox_editfrom.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.spinBox_editfrom)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox_editto = QSpinBox(self.groupBox)
        self.spinBox_editto.setObjectName(u"spinBox_editto")
        sizePolicy2.setHeightForWidth(self.spinBox_editto.sizePolicy().hasHeightForWidth())
        self.spinBox_editto.setSizePolicy(sizePolicy2)
        self.spinBox_editto.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.spinBox_editto)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_delete = QRadioButton(self.groupBox)
        self.radioButton_delete.setObjectName(u"radioButton_delete")
        sizePolicy2.setHeightForWidth(self.radioButton_delete.sizePolicy().hasHeightForWidth())
        self.radioButton_delete.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.radioButton_delete)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.spinBox_deleteclass = QSpinBox(self.groupBox)
        self.spinBox_deleteclass.setObjectName(u"spinBox_deleteclass")
        sizePolicy2.setHeightForWidth(self.spinBox_deleteclass.sizePolicy().hasHeightForWidth())
        self.spinBox_deleteclass.setSizePolicy(sizePolicy2)
        self.spinBox_deleteclass.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.spinBox_deleteclass)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        sizePolicy2.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.pushButton_start)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Class Label Editor", None))
        self.label.setText(QCoreApplication.translate("Form", u"labels Path: ", None))
        self.pushButton_openpath.setText(QCoreApplication.translate("Form", u"Open Path", None))
        self.groupBox.setTitle("")
        self.radioButton_edit.setText(QCoreApplication.translate("Form", u"Edit Class", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<->", None))
        self.radioButton_delete.setText(QCoreApplication.translate("Form", u"Delete Class", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

