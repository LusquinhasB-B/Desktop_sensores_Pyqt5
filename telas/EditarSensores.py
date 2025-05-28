from PyQt5.QtWidgets import * 

from controller.DadosController import DadosController

class EditarSensores(QWidget):
    def __init__(self, dados_id, temperatura, umidade, luminosidade, visualizacao):
        super().__init__()
        self.controller = DadosController()
        self.dados_id = dados_id
        self.visualizacao = visualizacao
        self.initUI(temperatura, umidade, luminosidade)

    def initUI(self, temperatura, umidade, luminosidade):
        self.setWindowTitle("Editar planta")
        self.setGeometry(550, 150, 300, 200)

        layout = QVBoxLayout()
        
        self.temperatura_texto = QLabel("Temperatura: ")
        self.temperatura_input = QLineEdit(temperatura)

        self.umidade_texto = QLabel("Umidade: ")
        self.umidade_input = QLineEdit(umidade)

        self.luminosidade_texto = QLabel("Luminosidade: ")
        self.luminosidade_input = QLineEdit(luminosidade)

        self.botao_salvar = QPushButton("Salvar alterações")
        self.botao_salvar.clicked.connect(self.salvar_alteracoes)

        layout.addWidget(self.temperatura_texto)
        layout.addWidget(self.temperatura_input)
        layout.addWidget(self.umidade_texto)
        layout.addWidget(self.umidade_input)
        layout.addWidget(self.luminosidade_texto)
        layout.addWidget(self.luminosidade_input)
        layout.addWidget(self.botao_salvar)
        
         


        self.setLayout(layout)
    
    def salvar_alteracoes(self):
        temperatura = self.temperatura_input.text()
        umidade = self.umidade_input.text()
        luminosidade = self.luminosidade_input.text()

        self.controller.atualizar_sensores(self.dados_id, temperatura, umidade, luminosidade)

        self.visualizacao.carregar_dados()

        self.close()