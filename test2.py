# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(365, 389)
        MainWindow2.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.prof_lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prof_lineEdit_2.setGeometry(QtCore.QRect(120, 120, 201, 20))
        self.prof_lineEdit_2.setObjectName("prof_lineEdit_2")
        self.s_label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.s_label_1.setGeometry(QtCore.QRect(120, 80, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.s_label_1.setFont(font)
        self.s_label_1.setStyleSheet("background-color: rgb(178, 203, 229);\n"
"\n"
"")
        self.s_label_1.setText("")
        self.s_label_1.setObjectName("s_label_1")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.changeopen_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeopen_pushButton.setGeometry(QtCore.QRect(90, 250, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.changeopen_pushButton.setFont(font)
        self.changeopen_pushButton.setObjectName("changeopen_pushButton")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.changesave_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changesave_pushButton.setGeometry(QtCore.QRect(90, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.changesave_pushButton.setFont(font)
        self.changesave_pushButton.setObjectName("changesave_pushButton")
        self.prof_lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prof_lineEdit_3.setGeometry(QtCore.QRect(120, 160, 201, 20))
        self.prof_lineEdit_3.setObjectName("prof_lineEdit_3")
        self.s_label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.s_label_3.setGeometry(QtCore.QRect(120, 160, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.s_label_3.setFont(font)
        self.s_label_3.setStyleSheet("background-color: rgb(178, 203, 229);\n"
"\n"
"")
        self.s_label_3.setText("")
        self.s_label_3.setObjectName("s_label_3")
        self.errorprofile_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.errorprofile_2.setGeometry(QtCore.QRect(40, 250, 291, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.errorprofile_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.errorprofile_2.setFont(font)
        self.errorprofile_2.setStyleSheet("color: rgb(202, 0, 0);")
        self.errorprofile_2.setObjectName("errorprofile_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.prof_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prof_lineEdit.setGeometry(QtCore.QRect(120, 80, 201, 20))
        self.prof_lineEdit.setObjectName("prof_lineEdit")
        self.s_label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.s_label_4.setGeometry(QtCore.QRect(120, 200, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.s_label_4.setFont(font)
        self.s_label_4.setStyleSheet("background-color: rgb(178, 203, 229);\n"
"\n"
"")
        self.s_label_4.setText("")
        self.s_label_4.setObjectName("s_label_4")
        self.prof_lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prof_lineEdit_4.setGeometry(QtCore.QRect(120, 200, 201, 20))
        self.prof_lineEdit_4.setObjectName("prof_lineEdit_4")
        self.errorprofile_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.errorprofile_1.setGeometry(QtCore.QRect(120, 250, 131, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(202, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.errorprofile_1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.errorprofile_1.setFont(font)
        self.errorprofile_1.setStyleSheet("color: rgb(202, 0, 0);")
        self.errorprofile_1.setObjectName("errorprofile_1")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.profile_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.profile_label.setGeometry(QtCore.QRect(80, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.profile_label.setFont(font)
        self.profile_label.setObjectName("profile_label")
        self.s_label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.s_label_2.setGeometry(QtCore.QRect(120, 120, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.s_label_2.setFont(font)
        self.s_label_2.setStyleSheet("background-color: rgb(178, 203, 229);\n"
"\n"
"")
        self.s_label_2.setText("")
        self.s_label_2.setObjectName("s_label_2")
        self.home_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.home_pushButton.setGeometry(QtCore.QRect(90, 280, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.home_pushButton.setFont(font)
        self.home_pushButton.setObjectName("home_pushButton")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 365, 21))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label_2.setText(_translate("MainWindow2", "Пароль"))
        self.changeopen_pushButton.setText(_translate("MainWindow2", "Изменить данные"))
        self.label.setText(_translate("MainWindow2", "Логин"))
        self.changesave_pushButton.setText(_translate("MainWindow2", "Сохранить изменения"))
        self.errorprofile_2.setText(_translate("MainWindow2", "Данный номер телефона уже зарегистрирован"))
        self.label_4.setText(_translate("MainWindow2", "Должность"))
        self.errorprofile_1.setText(_translate("MainWindow2", "Данный логин занят"))
        self.label_3.setText(_translate("MainWindow2", "Телефон"))
        self.profile_label.setText(_translate("MainWindow2", "❊ Мой профиль ❊"))
        self.home_pushButton.setText(_translate("MainWindow2", "На главную"))
