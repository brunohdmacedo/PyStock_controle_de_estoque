import os
import sys
import mysql.connector


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from View.PY.FrmLogin import Ui_login
from View.PY.FrmAdmin import Ui_FrmAdmin
from View.PY.FrmColaborador import Ui_FrmColaborador

banco = mysql.connector.connect(
    host='localhost',
    port='3307',
    user='root',
    passwd='',
    database='banco_pystock'
)

cursor = banco.cursor()


class FrmLogin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(lambda: self.logar())

    def logar(self):

        global window

        cursor.execute("SELECT * FROM login")
        logins = cursor.fetchall()

        usuario = self.ui.lineEdit.text()
        senha = self.ui.lineEdit_2.text()

        print(f"Usuario inserido: {usuario}\n"
              f"Senha inserida: {senha}")

        for login in logins:

            if usuario != login[0]:
                self.ui.lineEdit.setStyleSheet('background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                                               'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                                               'border-radius: 0px;font: 10pt "Montserrat";')

            if senha != login[1]:
                self.ui.lineEdit_2.setStyleSheet('background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                                               'border-bottom-color: rgb(255, 17, 49);color: rgb(0,0,0);padding-bottom: 8px;'
                                               'border-radius: 0px;font: 10pt "Montserrat";')

            if usuario == login[0] and senha == login[1]:

                self.ui.lineEdit.setStyleSheet('background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                                               'border-bottom-color: rgb(159, 63, 250);color: rgb(0,0,0);padding-bottom: 8px;'
                                               'border-radius: 0px;font: 10pt "Montserrat";')

                self.ui.lineEdit_2.setStyleSheet('background-color: rgba(0, 0 , 0, 0);border: 2px solid rgba(0,0,0,0);'
                                                 'border-bottom-color: rgb(159, 63, 250);color: rgb(0,0,0);padding-bottom: 8px;'
                                                 'border-radius: 0px;font: 10pt "Montserrat";')
                if login[2] == 'admin':
                    print('Seu nivel de Login é: Admin')

                    window.close()
                    window = FrmAdmin()
                    window.show()

                if login[2] == 'colaborador':
                    window.close()
                    window = FrmColaborador()
                    window.show()
                break


class FrmAdmin(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_FrmAdmin()
        self.ui.setupUi(self)

        # Configurando páginas e os botões do menu

        # Home
        self.ui.btn_home.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_home))

        # Colaboradores

        self.ui.btn_colaboradores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_colaboradores))
        self.ui.btn_cadastrar_colaboradores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastro_colaboradores))
        self.ui.btn_alterar_colaboradores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.alterar_colaboradores))

        # Tabela pg_colaboradores
        self.ui.tabela_colaboradores.setColumnWidth(0, 260)
        self.ui.tabela_colaboradores.setColumnWidth(1, 260)
        self.ui.tabela_colaboradores.setColumnWidth(2, 260)

        # Tabela alterar_colaboradores
        self.ui.tabela_alterar_colaboradores.setColumnWidth(0, 330)
        self.ui.tabela_alterar_colaboradores.setColumnWidth(1, 330)
        self.ui.tabela_alterar_colaboradores.setColumnWidth(2, 330)

        # Monitoramento
        self.ui.btn_monitoramento.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.monitoramento))

        # Tabela Monitoramento
        self.ui.tabela_monitoramento.setColumnWidth(0, 156)
        self.ui.tabela_monitoramento.setColumnWidth(1, 156)
        self.ui.tabela_monitoramento.setColumnWidth(2, 156)
        self.ui.tabela_monitoramento.setColumnWidth(3, 156)
        self.ui.tabela_monitoramento.setColumnWidth(4, 156)

        # Clientes
        self.ui.btn_clientes.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_clientes))
        self.ui.btn_cadastrar_clientes.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastrar_clientes))
        self.ui.btn_alterar_clientes.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_clientes))

        # Tabela Clientes
        self.ui.tabela_clientes.setColumnWidth(0, 192)
        self.ui.tabela_clientes.setColumnWidth(1, 192)
        self.ui.tabela_clientes.setColumnWidth(2, 192)
        self.ui.tabela_clientes.setColumnWidth(3, 194)

        # Tabela Cadastrar Clientes
        self.ui.tabela_cadastrar_clientes.setColumnWidth(0, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(1, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(2, 247)
        self.ui.tabela_cadastrar_clientes.setColumnWidth(3, 249)

        # Tabela Alterar Clientes
        self.ui.tabela_alterar_clientes.setColumnWidth(0, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(1, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(2, 247)
        self.ui.tabela_alterar_clientes.setColumnWidth(3, 249)

        # Vendas
        self.ui.btn_Vendas.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_vendas))

        # Fornecedores
        self.ui.btn_fornecedores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_fornecedores))
        self.ui.btn_adicionar_forncedores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastrar_fornecedores))
        self.ui.btn_editar_fornecedores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_fornecedores))


        # Tabela Fornecedores
        self.ui.tabela_fornecedores.setColumnWidth(0, 257)
        self.ui.tabela_fornecedores.setColumnWidth(1, 257)
        self.ui.tabela_fornecedores.setColumnWidth(2, 257)

        # Tabela Cadastrar Fornecedores
        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(0, 330)
        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(1, 330)
        self.ui.tabela_cadastrar_fornecedores.setColumnWidth(2, 330)

        # Tabela Alterar Fornecedores
        self.ui.tabela_alterar_fornecedores.setColumnWidth(0, 330)
        self.ui.tabela_alterar_fornecedores.setColumnWidth(1, 330)
        self.ui.tabela_alterar_fornecedores.setColumnWidth(2, 330)

        # Produtos
        self.ui.btn_produtos.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_produtos))
        self.ui.btn_cadastrar_produto.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_cadastar_produtos))
        self.ui.btn_alterar_produto.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_alterar_produtos))

        # Tabela Produtos
        self.ui.tabela_produto.setColumnWidth(0, 50)
        self.ui.tabela_produto.setColumnWidth(1, 131)
        self.ui.tabela_produto.setColumnWidth(2, 250)
        self.ui.tabela_produto.setColumnWidth(3, 131)
        self.ui.tabela_produto.setColumnWidth(4, 75)
        self.ui.tabela_produto.setColumnWidth(5, 155)

        # Tabela Cadastrar Produtos
        self.ui.tabela_cadastro.setColumnWidth(0, 50)
        self.ui.tabela_cadastro.setColumnWidth(1, 165)
        self.ui.tabela_cadastro.setColumnWidth(2, 300)
        self.ui.tabela_cadastro.setColumnWidth(3, 165)
        self.ui.tabela_cadastro.setColumnWidth(4, 75)
        self.ui.tabela_cadastro.setColumnWidth(5, 250)

        # Tabela Alterar Produtos
        self.ui.tabela_alterar_produto.setColumnWidth(0, 50)
        self.ui.tabela_alterar_produto.setColumnWidth(1, 165)
        self.ui.tabela_alterar_produto.setColumnWidth(2, 300)
        self.ui.tabela_alterar_produto.setColumnWidth(3, 165)
        self.ui.tabela_alterar_produto.setColumnWidth(4, 75)
        self.ui.tabela_alterar_produto.setColumnWidth(5, 250)

        # Configurações
        self.ui.btn_configs.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_configuracoes))


class FrmColaborador(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_FrmColaborador()
        self.ui.setupUi(self)

        # Iniciando na página inicial
        self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_home)

        ## Clique dos botões

        # Home
        self.ui.btn_home.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_home))

        # Fornecedores
        self.ui.btn_fornecedores.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_fornecedores))

        # Vendas
        self.ui.btn_vendas.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_vendas))

        # Produtos
        self.ui.btn_produtos.clicked.connect(lambda: self.ui.Telas_do_menu.setCurrentWidget(self.ui.pg_produtos))

        # Voltar
        self.ui.btn_voltar.clicked.connect(self.Voltar)

        ## Ajustando Tabelas

        # Ajustando Largura das Colunas da Tabela Vendas

        self.ui.tabela_vendas.setColumnWidth(0, 45)
        self.ui.tabela_vendas.setColumnWidth(1, 125)
        self.ui.tabela_vendas.setColumnWidth(2, 250)
        self.ui.tabela_vendas.setColumnWidth(3, 150)
        self.ui.tabela_vendas.setColumnWidth(4, 45)
        self.ui.tabela_vendas.setColumnWidth(5, 175)

        # Ajustando Largura das Colunas da Tabela Produtos

        self.ui.tabela_produto.setColumnWidth(0, 45)
        self.ui.tabela_produto.setColumnWidth(1, 125)
        self.ui.tabela_produto.setColumnWidth(2, 250)
        self.ui.tabela_produto.setColumnWidth(3, 150)
        self.ui.tabela_produto.setColumnWidth(4, 45)
        self.ui.tabela_produto.setColumnWidth(5, 175)

        # Ajustando Largura das Colunas da Tabela Produtos

        self.ui.tabela_fornecedores.setColumnWidth(0, 330)
        self.ui.tabela_fornecedores.setColumnWidth(1, 330)
        self.ui.tabela_fornecedores.setColumnWidth(2, 331)

    def Voltar(self):
        global window

        window.close()
        window = FrmLogin()
        window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FrmLogin()
    window.show()
    sys.exit(app.exec_())
