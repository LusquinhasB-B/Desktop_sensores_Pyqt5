import sys
from PyQt5.QtWidgets import QTableWidgetItem, QPushButton, QWidget 
from controller.PlantaController import PlantaController


class VisualizarPlantas(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = PlantaController()
        self.initUI()

#---------------------------------------------------------------------------------
  
    def initUI(self):
        self
        
#---------------------------------------------------------------------------------
    
    def carregar_dados(self):
        dados = self.controller.obter_plantas()#Cria essa função lá na controller
        self.tabela.setRowCount(len(dados))
        for row, planta in enumerate(dados):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(planta[0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(planta[1]))
            self.tabela.setItem(row, 2, QTableWidgetItem(planta[2]))
