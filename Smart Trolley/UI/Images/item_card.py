# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ItemCard(object):
    def setupUi(self, ItemCard):
        ItemCard.setObjectName("ItemCard")
        ItemCard.resize(220, 126)
        self.verticalLayout = QtWidgets.QVBoxLayout(ItemCard)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.foodItemCard_2 = QtWidgets.QFrame(ItemCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.foodItemCard_2.sizePolicy().hasHeightForWidth())
        self.foodItemCard_2.setSizePolicy(sizePolicy)
        self.foodItemCard_2.setMinimumSize(QtCore.QSize(220, 126))
        self.foodItemCard_2.setMaximumSize(QtCore.QSize(220, 126))
        self.foodItemCard_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.foodItemCard_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.foodItemCard_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foodItemCard_2.setObjectName("foodItemCard_2")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.foodItemCard_2)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.label_68 = QtWidgets.QLabel(self.foodItemCard_2)
        self.label_68.setMaximumSize(QtCore.QSize(100, 70))
        self.label_68.setText("")
        self.label_68.setPixmap(QtGui.QPixmap(":/food/food and drinks/coca cola.jpeg"))
        self.label_68.setScaledContents(True)
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_44.addWidget(self.label_68)
        self.label_69 = QtWidgets.QLabel(self.foodItemCard_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setTextFormat(QtCore.Qt.RichText)
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_44.addWidget(self.label_69)
        self.verticalLayout.addWidget(self.foodItemCard_2)

        self.retranslateUi(ItemCard)
        QtCore.QMetaObject.connectSlotsByName(ItemCard)

    def retranslateUi(self, ItemCard):
        _translate = QtCore.QCoreApplication.translate
        ItemCard.setWindowTitle(_translate("ItemCard", "Form"))
        self.label_69.setText(_translate("ItemCard", "<html><head/><body><p><span style=\" font-size:10pt;\">Canned Coca-Cola</span></p><p><span style=\" font-size:10pt;\">GHS 12</span></p></body></html>"))
import resources_rc
