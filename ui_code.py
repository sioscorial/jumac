# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sample.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Ju(object):
    def setupUi(self, Ju):
        if not Ju.objectName():
            Ju.setObjectName(u"Ju")
        Ju.resize(292, 352)
        self.verticalLayout = QVBoxLayout(Ju)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openGLWidget = QOpenGLWidget(Ju)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout.addWidget(self.openGLWidget)

        self.pushButton_4 = QPushButton(Ju)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(Ju)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(Ju)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(Ju)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(Ju)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.retranslateUi(Ju)

        QMetaObject.connectSlotsByName(Ju)
    # setupUi

    def retranslateUi(self, Ju):
        Ju.setWindowTitle(QCoreApplication.translate("Ju", u"Dialog", None))
        self.pushButton_4.setText(QCoreApplication.translate("Ju", u"\ubc18\ubcf5\uc885\ub8cc", None))
        self.pushButton_3.setText(QCoreApplication.translate("Ju", u"\ubc18\ubcf5\uc2e4\ud589", None))
        self.pushButton_2.setText(QCoreApplication.translate("Ju", u"\ub179\ud654\uc885\ub8cc", None))
        self.pushButton.setText(QCoreApplication.translate("Ju", u"\ub179\ud654", None))
        self.pushButton_5.setText(QCoreApplication.translate("Ju", u"\uc5f0\uacb0", None))
    # retranslateUi

