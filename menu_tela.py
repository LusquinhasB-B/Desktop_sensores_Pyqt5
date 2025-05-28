import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from telas.enviar_dados import EnvioDados
from telas.telaCadastrarPlanta import CadastroPlantas
from telas.tabela_view import VizualizarPlantas

class Menu(QWidget):
    def __init__(self):
        super().__init__()

#-------------------Cria a janela da tela-----------------------------#

        self.setStyleSheet("""
            QWidget {
                background-color: #e3f2fd;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #333;
                border-radius: 6px;
            }

            QLabel {
                font-weight: bold;
                color: #1565c0;
                font-size: 18px;
                margin-bottom: 10px;
            }

            QPushButton {
                background-color: #64b5f6;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                margin-bottom: 15px;
                width: 200px;
                align-self: center;
            }

            QPushButton:hover {
                background-color: #42a5f5;
            }

            QPushButton:focus {
                outline: none;
            }

            QVBoxLayout {
                spacing: 20px;
                align-items: center;
            }
        """)

        # Ajustando o layout para um tamanho fixo e centralizado dos elementos
        self.setWindowTitle("Menu Principal")
        self.setGeometry(600, 250, 300, 300)
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()

        # Título centralizado
        self.titulo = QLabel("MENU", self)
        self.titulo.setAlignment(Qt.AlignCenter)

        # Botões com clique para outras telas
        self.botao_cadastro = QPushButton("Cadastro de Plantas")
        self.botao_cadastro.clicked.connect(self.abrir_cadastro)

        self.botao_envio_dados = QPushButton("Dados Sensores")
        self.botao_envio_dados.clicked.connect(self.abrir_envio_dados)

        self.botao_tabela = QPushButton("Visualizar Tabelas")
        self.botao_tabela.clicked.connect(self.abrir_tabela)

        # Adicionando os botões ao layout com o título
        layout.addWidget(self.titulo)
        layout.addWidget(self.botao_cadastro)
        layout.addWidget(self.botao_envio_dados)
        layout.addWidget(self.botao_tabela)

        self.setLayout(layout)
#-----------------------Funções para abrir as telas------------------------#

    def abrir_cadastro(self):
        self.hide()
        self.cadastro = CadastroPlantas()
        self.cadastro.show()

    def abrir_envio_dados(self):
        self.hide()
        self.envio_dados = EnvioDados()
        self.envio_dados.show()

    def abrir_tabela(self):
        self.hide()
        self.tabela = VizualizarPlantas()
        self.tabela.show()
        
#-------------------------Main------------------------------------#

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())
