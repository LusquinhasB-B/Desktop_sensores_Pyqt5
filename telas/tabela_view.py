from PyQt5.QtWidgets import *
from controller.PlantaController import PlantaController
from telas.EditarPlanta import EditarPlanta
from telas.EditarSensores import EditarSensores
from controller.DadosController import DadosController

#=---------------Cria a classe principal da aplicação-------------------#

class VizualizarPlantas(QWidget):
    def __init__(self):
        super().__init__()
        self.varPlantaController = PlantaController()
        self.VarDados_controller = DadosController()
        self.initUI()
        
#---------------------------Cria o visual da tela--------------------#

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

#----------------------------Cria a janela e o titulo----------------#

        self.setWindowTitle("Plantas e dados cadastrados")
        self.setGeometry(500, 100, 400, 500)
        self.setFixedSize(400, 500)

#-----------------------Cria a tabela de plantas cadastradas----------------#

        self.tabelaPlanta = QTableWidget(self)
        self.tabelaPlanta.setColumnCount(3)
        self.tabelaPlanta.setHorizontalHeaderLabels(["ID", "Nome popular", "Nome Científico"])
        self.tabelaPlanta.setStyleSheet("""
            QWidget {
                background-color: #e3f2fd;
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: #333;
            }
            QLabel {
                font-weight: bold;
            }
            QLineEdit, QTableWidget {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 4px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 6px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton#cancelar {
                background-color: #d9534f;
            }
            QPushButton#cancelar:hover {
                background-color: #c9302c;
            }

""")
        self.tabelaPlanta.setGeometry(0, 0, 360, 200)

#----------------------------Cria a tabela de dados dos sensores----------------#

        self.tabelaDados = QTableWidget(self)
        self.tabelaDados.setColumnCount(4)
        self.tabelaDados.setHorizontalHeaderLabels(["ID", "Temperatura", "Umidade", "Luminosidade"])
        self.tabelaDados.setGeometry(500, 100, 400, 300)

#-----------------------Cria o botão de atualizar os dados----------------#
        self.textoAtualiza = QLabel("ATUALIZAR os dados da tabela: ", self)
        self.botao_atualizar = QPushButton("Atualizar dados", self)
        self.botao_atualizar.clicked.connect(self.atualizar_tabelas)
        self.botao_atualizar.setGeometry(120, 140, 90, 30)##arrumar a posição do botão

#-----------------------Cria o botão de editar os dados existents na tabela----------------#
        self.textoEditar = QLabel("EDITAR os dados da tabela: ")
        self.botaoEditarPlantas = QPushButton("Editar dados plantas", self)
        self.botaoEditarPlantas.clicked.connect(self.abrir_tela_edicao_plantas)

        self.botaoEditarDados = QPushButton("Editar dados sensores")
        self.botaoEditarDados.clicked.connect(self.abrir_tela_edicao_dados)

#-----------------------Cria o botão de deletar os dados existentes na tabelas ----------------#

        self.textoDeletar = QLabel("DELETAR dados das tabela", self)
        self.botaoDeletarPlanta = QPushButton("Deletar linha plantas", self)
        self.botaoDeletarPlanta.clicked.connect(self.deletar_planta)

        self.botaoDeletarSensor = QPushButton("Deletar linha sensores", self)
        self.botaoDeletarSensor.clicked.connect(self.deletar_sensor)



#-----------------------Crio botão de voltar para a home----------------#

        self.botaoHome = QPushButton("Voltar a Tela Home", self)

#-----------------------Adiciona os elementos ao layout da tela----------------#

        layout.addWidget(self.tabelaPlanta)
        layout.addWidget(self.tabelaDados)

        layout.addWidget(self.textoAtualiza)
        layout.addWidget(self.botao_atualizar)

        layout.addWidget(self.textoEditar)
        layout.addWidget(self.botaoEditarPlantas)
        layout.addWidget(self.botaoEditarDados)

        layout.addWidget(self.textoDeletar)
        layout.addWidget(self.botaoDeletarPlanta)
        layout.addWidget(self.botaoDeletarSensor)
        
        layout.addWidget(self.botaoHome)

#---------------------Atualizando os dados das duas tabelas-------------------------------#

    def atualizar_tabelas(self):
        #Pegando os dados das plantas no banco de dados#
        self.tabelaPlanta.clearContents()
        self.tabelaPlanta.setRowCount(0)


        dados_plantas = self.varPlantaController.obter_plantas()
        self.tabelaPlanta.setRowCount(len(dados_plantas))

        for row, planta in enumerate(dados_plantas):
            self.tabelaPlanta.setItem(row, 0, QTableWidgetItem(str(planta[0])))
            self.tabelaPlanta.setItem(row, 1, QTableWidgetItem(planta[1]))
            self.tabelaPlanta.setItem(row, 2, QTableWidgetItem(planta[2]))

    #--------------------------------------#
    
        #Pegando os dados do banco de dados

        self.tabelaDados.clearContents()
        self.tabelaDados.setRowCount(0)

        dados_sensores = self.VarDados_controller.obter_dados()
        self.tabelaDados.setRowCount(len(dados_sensores))

        for row, sensor in enumerate(dados_sensores):
            self.tabelaDados.setItem(row, 0, QTableWidgetItem(str((sensor[0]))))
            self.tabelaDados.setItem(row, 1, QTableWidgetItem(str((sensor[1]))))
            self.tabelaDados.setItem(row, 2, QTableWidgetItem(str((sensor[2]))))
            self.tabelaDados.setItem(row, 3, QTableWidgetItem(str((sensor[3]))))

#-----------------------------DELETAR DADOS--------------------------#

    def deletar_planta(self):
        linha_selecionada = self.tabelaPlanta.currentRow()
        if linha_selecionada != -1:

            planta_id = int(self.tabelaPlanta.item(linha_selecionada, 0).text())

            resposta = QMessageBox.question(self, "Deletar planta", "Deseja EXCLUIR essa planta da tabela?")
            if resposta == QMessageBox.Yes:
                self.varPlantaController.deletar_planta(planta_id)
                self.atualizar_tabelas()

        else:
            QMessageBox.warning(self, "ERRO", "Selecione uma linha da tabela PLANTAS para DELETAR!")
    
    def deletar_sensor(self):
        linha_selecionada = self.tabelaDados.currentRow()

        if linha_selecionada != -1:
            sensores_id = int(self.tabelaDados.item(linha_selecionada, 0).text())

            resposta = QMessageBox.question (self, "Deletar dado sensor", "Deseja EXCLUIR essa linha da tabela sensores?")

            if resposta == QMessageBox.Yes:
                self.VarDados_controller.deletar_sensores(sensores_id)
                self.atualizar_tabelas()
        else:
            QMessageBox.warning(self, "ERRO", "Selecione uma linha da tabela SENSORES para DELETAR!")


    

#--------------------------------EDITAR DADOS---------------------------------#

    def abrir_tela_edicao_plantas(self):
        linha_selecionada = self.tabelaPlanta.currentRow()
        if linha_selecionada != -1:
            planta_id = int(self.tabelaPlanta.item(linha_selecionada, 0).text())
            nome_popular = self.tabelaPlanta.item(linha_selecionada, 1).text()
            nome_cientifico = self.tabelaPlanta.item(linha_selecionada, 2).text()

            self.tela_edicao = EditarPlanta(planta_id, nome_popular, nome_cientifico, self)
            self.tela_edicao.show()

        else:
            QMessageBox.warning(self, "ERRO", "Selecione uma linha da tabela PLANTAS para editar")

    def abrir_tela_edicao_dados(self):
        linha_selecionada = self.tabelaDados.currentRow()

        if linha_selecionada != -1:
            
            dados_id = int(self.tabelaDados.item(linha_selecionada, 0).text())
            temperatura = self.tabelaDados.item(linha_selecionada, 1).text()
            umidade = self.tabelaDados.item(linha_selecionada, 2).text()
            luminosidade = self.tabelaDados.item(linha_selecionada, 2).text()

            self.tela_edicao = EditarSensores(dados_id, temperatura, umidade, luminosidade, self)
            self.tela_edicao.show()
            
        else:
            QMessageBox.warning(self, "ERRO", "Selecione uma linha da tabela SENSORES para editar")

#---------------------ABRI MENU DE VOLTA---------------------#


   