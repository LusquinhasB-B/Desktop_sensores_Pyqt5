import sys
from PyQt5.QtWidgets import *

from controller.PlantaController import PlantaController
from controller.DadosController import DadosController

def carregarDados():
    dadosPlantas = PlantaController.obter_plantas
    dadosSensores = DadosController.obter_dados

    tabelaPlantas.setItem(len(dadosPlantas))
    tabelaSensor.setItem(len(dadosSensores))

    for linha, planta in enumerate(dadosPlantas):
        tabelaPlantas.setItem(linha, 0, QTableWidgetItem(str(planta[0])))
        tabelaPlantas.setItem(linha, 1, QTableWidgetItem(planta[1]))
        tabelaPlantas.setItem(linha, 2, QTableWidgetItem(planta[2]))
    
    for linha, dados in enumerate(dadosSensores):
        tabelaSensor.setItem(linha, 0, QTableWidgetItem(str(dados[0])))
        tabelaSensor.setItem(linha, 1, QTableWidgetItem(str(dados[1])))
        tabelaSensor.setItem(linha, 2, QTableWidgetItem(str(dados[2])))
        tabelaSensor.setItem(linha, 3, QTableWidgetItem(str(dados[3])))

app = QApplication(sys.argv)

janelaTabela = QWidget()
janelaTabela.setWindowTitle("Tabelas")
janelaTabela.setGeometry(500, 30, 480, 720)

layout = QVBoxLayout()
janelaTabela.setLayout(layout)

tabelaPlantas = QTableWidget()
tabelaPlantas.setColumnCount(3)
tabelaPlantas.setHorizontalHeaderLabels(["ID", "Nome Científico", "Nome Popular"])

tabelaSensor = QTableWidget()
tabelaSensor.setColumnCount(4)
tabelaSensor.setHorizontalHeaderLabels(["ID", "Temperatura", "Humidade", "Luminosidade"])

Atualizar = QPushButton("Atualizar dados")
Atualizar.clicked.connect(carregarDados())

layout.addWidget(tabelaPlantas)
layout.addWidget(tabelaSensor)
layout.addWidget(Atualizar)

janelaTabela.show()
sys.exit(app.exec_())

