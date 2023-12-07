# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'macro.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)
from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QMainWindow
from PySide6.QtCore import QRect

class Ui_Jumac(object):
    def setupUi(self, Jumac):
        if not Jumac.objectName():
            Jumac.setObjectName(u"Jumac")
        Jumac.resize(354, 187)

        self.log_label = QLabel(Jumac)  # 새 레이블 생성
        self.log_label.setGeometry(QRect(10, 100, 331, 51))  # 위치 및 크기 설정
        self.log_label.setObjectName(u"log_label")

        self.pushButton = QPushButton(Jumac)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 10, 93, 28))

        self.pushButton_2 = QPushButton(Jumac)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 10, 93, 28))

        self.pushButton_3 = QPushButton(Jumac)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 50, 93, 28))

        self.pushButton_4 = QPushButton(Jumac)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 50, 93, 28))

        self.pushButton_5 = QPushButton(Jumac)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 10, 93, 28))

        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)

        QMetaObject.connectSlotsByName(Jumac)
    # setupUi

    def retranslateUi(self, Jumac):
        Jumac.setWindowTitle(QCoreApplication.translate("Jumac", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Jumac", u"\ub179\ud654", None))
        self.pushButton_2.setText(QCoreApplication.translate("Jumac", u"\ub179\ud654\uc885\ub8cc", None))
        self.pushButton_3.setText(QCoreApplication.translate("Jumac", u"\ubc18\ubcf5\uc2e4\ud589", None))
        self.pushButton_4.setText(QCoreApplication.translate("Jumac", u"\ubc18\ubcf5\uc885\ub8cc", None))
        self.pushButton_5.setText(QCoreApplication.translate("Jumac", u"\uc5f0\uacb0", None))
    # retranslateUi

