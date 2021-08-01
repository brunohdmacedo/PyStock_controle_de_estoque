# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmCadastroFornecedores.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadastroForncedores(object):
    def setupUi(self, CadastroForncedores):
        CadastroForncedores.setObjectName("CadastroForncedores")
        CadastroForncedores.resize(391, 299)
        CadastroForncedores.setMinimumSize(QtCore.QSize(391, 299))
        CadastroForncedores.setMaximumSize(QtCore.QSize(391, 299))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagens/P em png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CadastroForncedores.setWindowIcon(icon)
        CadastroForncedores.setStyleSheet("background-color: white;")
        CadastroForncedores.setIconSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(CadastroForncedores)
        self.centralwidget.setObjectName("centralwidget")
        self.line_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nome.setGeometry(QtCore.QRect(20, 20, 351, 51))
        self.line_nome.setStyleSheet("background-color: rgba(0, 0 , 0, 0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(159, 63, 250);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 10pt \"Montserrat\";")
        self.line_nome.setObjectName("line_nome")
        self.btn_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cadastrar.setGeometry(QtCore.QRect(20, 240, 351, 41))
        self.btn_cadastrar.setMinimumSize(QtCore.QSize(351, 41))
        self.btn_cadastrar.setMaximumSize(QtCore.QSize(351, 16777215))
        self.btn_cadastrar.setStyleSheet("QPushButton {\n"
"border: 2px;\n"
"background-color: rgb(159, 63, 250);\n"
"color: white;\n"
"border-radius: 5px;\n"
"font: 10pt \"Montserrat\";\n"
"outline: 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(197, 62, 255);\n"
"}\n"
"")
        self.btn_cadastrar.setObjectName("btn_cadastrar")
        self.line_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.line_endereco.setGeometry(QtCore.QRect(20, 90, 351, 51))
        self.line_endereco.setStyleSheet("background-color: rgba(0, 0 , 0, 0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(159, 63, 250);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 10pt \"Montserrat\";")
        self.line_endereco.setCursorPosition(0)
        self.line_endereco.setObjectName("line_endereco")
        self.line_contato = QtWidgets.QLineEdit(self.centralwidget)
        self.line_contato.setGeometry(QtCore.QRect(20, 160, 351, 51))
        self.line_contato.setStyleSheet("background-color: rgba(0, 0 , 0, 0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(159, 63, 250);\n"
"color: rgb(0,0,0);\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 10pt \"Montserrat\";")
        self.line_contato.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_contato.setInputMask("")
        self.line_contato.setDragEnabled(False)
        self.line_contato.setReadOnly(False)
        self.line_contato.setObjectName("line_contato")
        CadastroForncedores.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadastroForncedores)
        QtCore.QMetaObject.connectSlotsByName(CadastroForncedores)

    def retranslateUi(self, CadastroForncedores):
        _translate = QtCore.QCoreApplication.translate
        CadastroForncedores.setWindowTitle(_translate("CadastroForncedores", "Cadastrar Fornecedores"))
        self.line_nome.setPlaceholderText(_translate("CadastroForncedores", "Nome"))
        self.btn_cadastrar.setText(_translate("CadastroForncedores", "Finalizar Cadastro"))
        self.line_endereco.setPlaceholderText(_translate("CadastroForncedores", "Endereço"))
        self.line_contato.setPlaceholderText(_translate("CadastroForncedores", "(00) 0 0000-0000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadastroForncedores = QtWidgets.QMainWindow()
    ui = Ui_CadastroForncedores()
    ui.setupUi(CadastroForncedores)
    CadastroForncedores.show()
    sys.exit(app.exec_())
