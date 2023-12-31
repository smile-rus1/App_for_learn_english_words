# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\correct_write_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CorrectWrite_Window(object):
    def setupUi(self, CorrectWrite_Window):
        CorrectWrite_Window.setObjectName("CorrectWrite_Window")
        CorrectWrite_Window.resize(800, 435)
        CorrectWrite_Window.setStyleSheet("background-color: rgb(252, 252, 189);")
        self.centralwidget = QtWidgets.QWidget(CorrectWrite_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_to_out = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_to_out.setGeometry(QtCore.QRect(170, 260, 401, 51))
        self.edit_to_out.setStyleSheet("font: italic 20pt \"Times New Roman\";")
        self.edit_to_out.setText("")
        self.edit_to_out.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_to_out.setDragEnabled(False)
        self.edit_to_out.setReadOnly(True)
        self.edit_to_out.setObjectName("edit_to_out")
        self.btn_accept = QtWidgets.QPushButton(self.centralwidget)
        self.btn_accept.setGeometry(QtCore.QRect(610, 340, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_accept.setFont(font)
        self.btn_accept.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_accept.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_accept.setStyleSheet("QPushButton {\n"
"    background-color: rgb(153, 153, 153);\n"
"    border: none;\n"
"    color: #0000;\n"
"    padding: 8px 16px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: rgb(0, 170, 0);\n"
"    padding-left: 14px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.btn_accept.setAutoRepeatInterval(100)
        self.btn_accept.setObjectName("btn_accept")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 191, 41))
        self.label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(161, 161, 161);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radio_on_total = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_on_total.setGeometry(QtCore.QRect(10, 110, 371, 31))
        self.radio_on_total.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.radio_on_total.setObjectName("radio_on_total")
        self.edit_to_input = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_to_input.setGeometry(QtCore.QRect(170, 340, 401, 51))
        self.edit_to_input.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.edit_to_input.setAlignment(QtCore.Qt.AlignCenter)
        self.edit_to_input.setDragEnabled(False)
        self.edit_to_input.setReadOnly(True)
        self.edit_to_input.setObjectName("edit_to_input")
        self.btn_skip_word = QtWidgets.QPushButton(self.centralwidget)
        self.btn_skip_word.setGeometry(QtCore.QRect(610, 260, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_skip_word.setFont(font)
        self.btn_skip_word.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_skip_word.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_skip_word.setStyleSheet("QPushButton {\n"
"    background-color: rgb(153, 153, 153);\n"
"    border: none;\n"
"    color: #0000;\n"
"    padding: 8px 16px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: rgb(0, 170, 0);\n"
"    padding-left: 14px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.btn_skip_word.setAutoRepeatInterval(100)
        self.btn_skip_word.setObjectName("btn_skip_word")
        self.btn_start_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_end.setGeometry(QtCore.QRect(510, 0, 261, 191))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_start_end.setFont(font)
        self.btn_start_end.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_start_end.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_start_end.setStyleSheet("QPushButton {\n"
"    background-color: rgb(153, 153, 153);\n"
"    border: none;\n"
"    color: #0000;\n"
"    padding: 8px 16px;\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: rgb(0, 170, 0);\n"
"    padding-left: 14px;\n"
"    padding-top: 10px;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.btn_start_end.setAutoRepeatInterval(100)
        self.btn_start_end.setObjectName("btn_start_end")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 210, 801, 31))
        self.line.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.radio_basic = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_basic.setGeometry(QtCore.QRect(10, 60, 381, 31))
        self.radio_basic.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.radio_basic.setChecked(True)
        self.radio_basic.setObjectName("radio_basic")
        CorrectWrite_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(CorrectWrite_Window)
        QtCore.QMetaObject.connectSlotsByName(CorrectWrite_Window)

    def retranslateUi(self, CorrectWrite_Window):
        _translate = QtCore.QCoreApplication.translate
        CorrectWrite_Window.setWindowTitle(_translate("CorrectWrite_Window", "MainWindow"))
        self.edit_to_out.setPlaceholderText(_translate("CorrectWrite_Window", "Слово на русском"))
        self.btn_accept.setText(_translate("CorrectWrite_Window", "Отправить"))
        self.label.setText(_translate("CorrectWrite_Window", "Режимы"))
        self.radio_on_total.setText(_translate("CorrectWrite_Window", "Вывести определенное количество"))
        self.edit_to_input.setPlaceholderText(_translate("CorrectWrite_Window", "Введите слово на английском"))
        self.btn_skip_word.setText(_translate("CorrectWrite_Window", "Пропустить\n"
"слово"))
        self.btn_start_end.setText(_translate("CorrectWrite_Window", "Начать"))
        self.radio_basic.setText(_translate("CorrectWrite_Window", "Обычный"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CorrectWrite_Window = QtWidgets.QMainWindow()
    ui = Ui_CorrectWrite_Window()
    ui.setupUi(CorrectWrite_Window)
    CorrectWrite_Window.show()
    sys.exit(app.exec_())
