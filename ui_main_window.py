# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(600, 520)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_btn.sizePolicy().hasHeightForWidth())
        self.exit_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.exit_btn)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.save_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.key_8 = QPushButton(self.centralwidget)
        self.key_8.setObjectName(u"key_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.key_8.sizePolicy().hasHeightForWidth())
        self.key_8.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_8, 1, 2, 1, 1)

        self.key_10 = QPushButton(self.centralwidget)
        self.key_10.setObjectName(u"key_10")
        sizePolicy1.setHeightForWidth(self.key_10.sizePolicy().hasHeightForWidth())
        self.key_10.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_10, 1, 4, 1, 1)

        self.key_17 = QPushButton(self.centralwidget)
        self.key_17.setObjectName(u"key_17")
        sizePolicy1.setHeightForWidth(self.key_17.sizePolicy().hasHeightForWidth())
        self.key_17.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_17, 3, 1, 1, 1)

        self.key_19 = QPushButton(self.centralwidget)
        self.key_19.setObjectName(u"key_19")
        sizePolicy1.setHeightForWidth(self.key_19.sizePolicy().hasHeightForWidth())
        self.key_19.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_19, 3, 3, 1, 1)

        self.key_3 = QPushButton(self.centralwidget)
        self.key_3.setObjectName(u"key_3")
        sizePolicy1.setHeightForWidth(self.key_3.sizePolicy().hasHeightForWidth())
        self.key_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_3, 0, 2, 1, 1)

        self.key_12 = QPushButton(self.centralwidget)
        self.key_12.setObjectName(u"key_12")
        sizePolicy1.setHeightForWidth(self.key_12.sizePolicy().hasHeightForWidth())
        self.key_12.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_12, 2, 1, 1, 1)

        self.key_18 = QPushButton(self.centralwidget)
        self.key_18.setObjectName(u"key_18")
        sizePolicy1.setHeightForWidth(self.key_18.sizePolicy().hasHeightForWidth())
        self.key_18.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_18, 3, 2, 1, 1)

        self.key_13 = QPushButton(self.centralwidget)
        self.key_13.setObjectName(u"key_13")
        sizePolicy1.setHeightForWidth(self.key_13.sizePolicy().hasHeightForWidth())
        self.key_13.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_13, 2, 2, 1, 1)

        self.key_2 = QPushButton(self.centralwidget)
        self.key_2.setObjectName(u"key_2")
        sizePolicy1.setHeightForWidth(self.key_2.sizePolicy().hasHeightForWidth())
        self.key_2.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_2, 0, 1, 1, 1)

        self.key_4 = QPushButton(self.centralwidget)
        self.key_4.setObjectName(u"key_4")
        sizePolicy1.setHeightForWidth(self.key_4.sizePolicy().hasHeightForWidth())
        self.key_4.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_4, 0, 3, 1, 1)

        self.key_11 = QPushButton(self.centralwidget)
        self.key_11.setObjectName(u"key_11")
        sizePolicy1.setHeightForWidth(self.key_11.sizePolicy().hasHeightForWidth())
        self.key_11.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_11, 2, 0, 1, 1)

        self.key_7 = QPushButton(self.centralwidget)
        self.key_7.setObjectName(u"key_7")
        sizePolicy1.setHeightForWidth(self.key_7.sizePolicy().hasHeightForWidth())
        self.key_7.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_7, 1, 1, 1, 1)

        self.key_14 = QPushButton(self.centralwidget)
        self.key_14.setObjectName(u"key_14")
        sizePolicy1.setHeightForWidth(self.key_14.sizePolicy().hasHeightForWidth())
        self.key_14.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_14, 2, 3, 1, 1)

        self.key_1 = QPushButton(self.centralwidget)
        self.key_1.setObjectName(u"key_1")
        sizePolicy1.setHeightForWidth(self.key_1.sizePolicy().hasHeightForWidth())
        self.key_1.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_1, 0, 0, 1, 1)

        self.key_5 = QPushButton(self.centralwidget)
        self.key_5.setObjectName(u"key_5")
        sizePolicy1.setHeightForWidth(self.key_5.sizePolicy().hasHeightForWidth())
        self.key_5.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_5, 0, 4, 1, 1)

        self.key_15 = QPushButton(self.centralwidget)
        self.key_15.setObjectName(u"key_15")
        sizePolicy1.setHeightForWidth(self.key_15.sizePolicy().hasHeightForWidth())
        self.key_15.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_15, 2, 4, 1, 1)

        self.key_20 = QPushButton(self.centralwidget)
        self.key_20.setObjectName(u"key_20")
        sizePolicy1.setHeightForWidth(self.key_20.sizePolicy().hasHeightForWidth())
        self.key_20.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_20, 3, 4, 1, 1)

        self.key_9 = QPushButton(self.centralwidget)
        self.key_9.setObjectName(u"key_9")
        sizePolicy1.setHeightForWidth(self.key_9.sizePolicy().hasHeightForWidth())
        self.key_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_9, 1, 3, 1, 1)

        self.key_16 = QPushButton(self.centralwidget)
        self.key_16.setObjectName(u"key_16")
        sizePolicy1.setHeightForWidth(self.key_16.sizePolicy().hasHeightForWidth())
        self.key_16.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_16, 3, 0, 1, 1)

        self.key_6 = QPushButton(self.centralwidget)
        self.key_6.setObjectName(u"key_6")
        sizePolicy1.setHeightForWidth(self.key_6.sizePolicy().hasHeightForWidth())
        self.key_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.key_6, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Sel'tso Technologies Macro Keypad", None))
        self.exit_btn.setText(QCoreApplication.translate("mainWindow", u"exit app", None))
        self.cancel_btn.setText(QCoreApplication.translate("mainWindow", u"cancel", None))
        self.save_btn.setText(QCoreApplication.translate("mainWindow", u"save", None))
        self.key_8.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_10.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_17.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_19.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_3.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_12.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_18.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_13.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_2.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_4.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_11.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_7.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_14.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_1.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_5.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_15.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_20.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_9.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_16.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.key_6.setText(QCoreApplication.translate("mainWindow", u"", None))
    # retranslateUi

