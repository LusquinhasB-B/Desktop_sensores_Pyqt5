import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from controller.DadosController import DadosController
#---------------------------------------------------------------------------------#

class EnvioDados(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = DadosController()
        self.initUI()

#---------------------------------------------------------------------------------#
    def botao_clicado(self):
        temperatura = self.inserir_temperatura.text().strip()
        umidade = self.inserir_umidade.text().strip()
        luminosidade = self.inserir_luminosidade.text().strip()
        if not temperatura or not umidade or not luminosidade:
            QMessageBox.critical(self, "Erro!", "Preencha todos os campos para prosseguir!")
            return
        
        dados_id = self.controller.salvar_dados(temperatura, umidade, luminosidade)
        if dados_id:
            QMessageBox.information(self, "Sucesso!", "Dados cadastrados com sucesso!")
            self.inserir_umidade.clear()
            self.inserir_temperatura.clear()
            self.inserir_temperatura.clear()
        else:
            QMessageBox.critical(self, "Erro", "Erro ao enviar os dados.")

#---------------------------------------------------------------------------------#
    def initUI(self):
        self.layout
        self.setWindowTitle("Enviar dados")
        self.setGeometry(470, 210, 340, 430)
        self.setFixedSize(340, 430)
        self.setStyleSheet("""
            QWidget{ 
                background-color:  #95e7f3;
                font-family: "Calibri";
                font-size: 18px;
                font-weight: bold;
            }
            QLabel#imagem{
                height: 300px;
            } 
            QLabel#titulo{
                font-size: 24px;
                color: black;
            }
            QLabel#icon_temp{
                width: 100px; 
                height: 20px;
            }
            QLabel#rotulos{
                background-color: #6eaa5e;
                border-radius: 8px;
                padding: 1px;
            }
            QLabel#luminosidade{
                background-color:  #ffff00; 
                border-radius: 8px;
                padding: 1px;
                border-style: solid;
                border-width: 1px;
                border-color:#b8b814;
            }
            QLabel#temperatura{
                background-color: #ee3a1f; 
                border-radius: 8px;
                padding: 1px;
                border-style: solid;
                border-width: 1px;
                border-color: #b81414;
            }
            QLabel#umidade{
                background-color:  #00b6ff;
                border-radius: 8px;
                padding: 1px;
            }
            QLineEdit#inserir{
                padding: 1px;
                border-radius: 5px;
                background-color: #778899;
                border-style: solid;
                border-width: 1px;
                border-color: #000000;
            }
            QLineEdit#inserir:hover{
                background-color: #dcdcdc;
            }
            QPushButton#botao{
                color:rgb(0, 0, 0);
                background-color: #949494; 
                padding: 5px;
                border-radius: 5px;
                border-style: solid;
                border-width: 2px;
                border-color:rgb(0, 0, 0);
            }
            QPushButton#botao:hover{
                background-color: #bdbebd;
            }
            QPushButton#botao:pressed{
                background-color: #3f3f3f;
            } """)

        titulo = QLabel("Receber e enviar\n           dados")
        titulo.move(50, 20)
        titulo.setObjectName("titulo")
        titulo.setStyleSheet("font-size: 24px")

        #Rotulo umidade
        self.umidade = QLabel("Umidade", self)
        self.umidade.move(10,100)
        self.umidade.setObjectName("rotulos")
        self.umidade.setObjectName("umidade")
        self.inserir_umidade = QLineEdit(self)
        self.inserir_umidade.move(10, 125)
        self.inserir_umidade.setObjectName("inserir")


        #Criar o rotulo da temperatura
        self.temperatura = QLabel("Temperatura", self)
        self.temperatura.move(10, 170)
        self.temperatura.setObjectName("rotulos")
        self.temperatura.setObjectName("temperatura")
        self.temperatura.setStyleSheet("background-color: #ee3a1f; border-radius: 8px; padding: 1px;border-style: solid; border-width: 1px; border-color: #b81414;")
        #Cria a caixa de texto da temperatura
        self.inserir_temperatura = QLineEdit(self)
        self.inserir_temperatura.move(10, 195)
        self.inserir_temperatura.setObjectName("inserir")

        #Rotulo luminosade
        self.luminosidade = QLabel("Luminosidade", self)
        self.luminosidade.move(10, 240)
        self.luminosidade.setObjectName("rotulos")
        self.luminosidade.setObjectName("luminosidade")
        self.luminosidade.setStyleSheet("background-color:  #ffff00; border-radius: 8px;padding: 1px;border-style: solid;border-width: 1px;border-color:#b8b814;")
        self.inserir_luminosidade = QLineEdit(self)
        self.inserir_luminosidade.move(10, 265)
        self.inserir_luminosidade.setObjectName("inserir")

        #botao para enviar os dados
        botao_enviar = QPushButton ("Enviar dados", self)
        botao_enviar.move(135, 330)
        botao_enviar.setObjectName("botao")
        botao_enviar.clicked.connect(self.botao_clicado)

#----------------------\-----------------------------------------------------------#
