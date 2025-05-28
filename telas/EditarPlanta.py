from PyQt5.QtWidgets import * 

from controller.PlantaController import PlantaController

class EditarPlanta(QWidget):
    def __init__(self, planta_id, nome_popular, nome_cientifico, visualizacao):
        super().__init__()
        self.controller = PlantaController()
        self.planta_id = planta_id
        self.visualizacao = visualizacao
        self.initUI(nome_popular, nome_cientifico)

    def initUI(self, nome_popular, nome_cientifico):
        self.setWindowTitle("Editar planta")
        self.setGeometry(550, 150, 300, 200)

        layout = QVBoxLayout()

        self.nome_popular_texto = QLabel("Nome popular: ")
        self.nome_popular_input = QLineEdit(nome_popular)

        self.nome_cientifico_texto = QLabel("Nome científico: ")
        self.nome_cientifico_input = QLineEdit(nome_cientifico)

        self.botao_salvar = QPushButton("Salvar alterações")
        self.botao_salvar.clicked.connect(self.salvar_alteracoes)

        layout.addWidget(self.nome_popular_texto)
        layout.addWidget(self.nome_popular_input)

        layout.addWidget(self.nome_cientifico_texto)
        layout.addWidget(self.nome_cientifico_input)
        
        layout.addWidget(self.botao_salvar)

        self.setLayout(layout)
    
    def salvar_alteracoes(self):
        nome_popular = self.nome_popular_input.text()
        nome_cientifico = self.nome_cientifico_input.text()

        self.controller.atualizar_planta(self.planta_id, nome_popular, nome_cientifico)
        self.visualizacao.carregar_dados()
        self.close()