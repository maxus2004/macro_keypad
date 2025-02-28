# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_action_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ButtonConfigDialog(object):
    def setupUi(self, ButtonConfigDialog):
        if not ButtonConfigDialog.objectName():
            ButtonConfigDialog.setObjectName(u"ButtonConfigDialog")
        ButtonConfigDialog.resize(300, 200)
        self.gridLayout = QGridLayout(ButtonConfigDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.KeyCationTextEdit = QPlainTextEdit(ButtonConfigDialog)
        self.KeyCationTextEdit.setObjectName(u"KeyCationTextEdit")

        self.verticalLayout.addWidget(self.KeyCationTextEdit)

        self.buttonBox = QDialogButtonBox(ButtonConfigDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ButtonConfigDialog)
        self.buttonBox.accepted.connect(ButtonConfigDialog.accept)
        self.buttonBox.rejected.connect(ButtonConfigDialog.reject)

        QMetaObject.connectSlotsByName(ButtonConfigDialog)
    # setupUi

    def retranslateUi(self, ButtonConfigDialog):
        ButtonConfigDialog.setWindowTitle(QCoreApplication.translate("ButtonConfigDialog", u"Key Actions", None))
    # retranslateUi

