import sys
# Importação dos módulos necessários do PyQt5 para criação da interface gráfica
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
# Importa o controlador responsável por gerenciar a lógica do cadastro de plantas
from controller.PlantaController import PlantaController

# Definição da classe CadastroPlantas, que representa a interface gráfica do cadastro de plantas
class CadastroPlantas(QWidget):
    def __init__(self):
        super().__init__()  # Inicializa a classe pai QWidget
        self.controller = PlantaController()  # Instancia o controlador para manipular os dados das plantas
        self.imagem_path = ""  # Variável para armazenar o caminho da imagem selecionada
        self.initUI()  # Chama o método para inicializar a interface gráfica

#--------------------------------------------------------------------------------- #
    
    def botao_clicado(self): # Método acionado ao clicar no botão "Cadastrar"
        # Obtém os valores dos campos de entrada e remove espaços extras
        nome_popular = self.input_nome_popular.text().strip()
        nome_cientifico = self.input_nome_cientifico.text().strip()

        # Verifica se os campos estão preenchidos
        if not nome_popular or not nome_cientifico:
            QMessageBox.critical(self, "Erro", "Preencha todos os campos!")  # Exibe um alerta caso algum campo esteja vazio
            return  # Retorna sem continuar o cadastro

        # Chama o método do controlador para salvar a planta no banco de dados
        planta_id = self.controller.salvar_planta(nome_popular, nome_cientifico, self.imagem_path)

        # Verifica se o cadastro foi bem-sucedido
        if planta_id:
            QMessageBox.information(self, "Sucesso", "Planta cadastrada com sucesso!")  # Exibe mensagem de sucesso
            # Limpa os campos de entrada e a área da imagem
            self.input_nome_popular.clear()
            self.input_nome_cientifico.clear()
            self.area_imagem.clear()
            self.imagem_path = ""  # Reseta o caminho da imagem
        else:
            QMessageBox.critical(self, "Erro", "Erro ao cadastrar a planta.")  # Exibe mensagem de erro

#-----------Método responsável por configurar os elementos da interface gráfica------------#

    def initUI(self):
        self.setWindowTitle("Cadastro de Plantas")  # Define o título da janela
        self.setGeometry(100, 100, 300, 300)  # Define a posição e o tamanho da janela
        self.setStyleSheet("background-color: #95e7f3;")  # Define a cor de fundo da janela

        layout = QVBoxLayout()  # Cria um layout vertical para organizar os elementos
        
        # Criação do título da tela
        titulo = QLabel("CADASTRO")
        titulo.setFont(QFont("Calibri", 14, QFont.Bold))  # Define a fonte e o tamanho do texto
        titulo.setStyleSheet("color: black; background-color: #81c9fa")  # Define a cor do texto

        # Campo de entrada para o nome popular da planta
        self.input_nome_popular = QLineEdit()
        self.input_nome_popular.setPlaceholderText("Nome Popular")  # Texto de dica no campo
        self.input_nome_popular.setStyleSheet("background-color: white;padding: 1px;border-radius: 5px; background-color: #778899;border-style: solid; border-width: 1px;border-color: #000000;") 
                
         # Define a cor de fundo
        self.input_nome_popular.setObjectName("inserir")

        # Campo de entrada para o nome científico da planta
        self.input_nome_cientifico = QLineEdit()
        self.input_nome_cientifico.setPlaceholderText("Nome Científico")
        self.input_nome_cientifico.setStyleSheet("background-color: white;padding: 1px;border-radius: 5px; background-color: #778899;border-style: solid; border-width: 1px;border-color: #000000")
        self.input_nome_cientifico.setObjectName("inserir")

        # Botão para selecionar uma imagem da planta
        self.botao_imagem = QPushButton("Insira uma Imagem")
        self.botao_imagem.setStyleSheet("background-color: gray; color: white;")  # Define o estilo do botão
        self.botao_imagem.clicked.connect(self.abrir_arquivo)  # Conecta o clique do botão ao método abrir_arquivo
    
        # Área onde a imagem selecionada será exibida
        self.area_imagem = QLabel()
        self.area_imagem.setAlignment(Qt.AlignCenter)  # Centraliza a imagem
        self.area_imagem.setStyleSheet("border: 1px solid black; border-radius: 7px; min-height: 100px; background-color: #b0ffff;")  # Define estilo da borda e fundo

        # Botão de cancelar
        botao_cancelar = QPushButton("Cancelar")
        botao_cancelar.setStyleSheet("background-color: gray; color: white;")  # Define o estilo do botão
        botao_cancelar.clicked.connect(self.cancelar)
        # Botão para cadastrar a planta
        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.setStyleSheet("background-color: gray; color: white;")  # Define o estilo do botão
        botao_cadastrar.clicked.connect(self.botao_clicado)  # Conecta o clique do botão ao método botao_clicado

        # Adiciona os elementos ao layout
        layout.addWidget(titulo)
        layout.addWidget(self.input_nome_popular)
        layout.addWidget(self.input_nome_cientifico)
        layout.addWidget(self.botao_imagem)
        layout.addWidget(self.area_imagem)
        layout.addWidget(botao_cancelar)
        layout.addWidget(botao_cadastrar)

        self.setLayout(layout)  # Define o layout da janela

#-------------------Método para abrir um seletor de arquivos para escolher uma imagem---------------#

    def abrir_arquivo(self):
        options = QFileDialog.Options()  # Configurações do seletor de arquivosss
        # Abre a janela para selecionar a imagem, permitindo vários formatos
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Abrir Arquivo", "", "Imagens (*.png *.jpg *.jpeg *.bmp *.gif);;Todos os Arquivos (*)", options=options
        )
        if file_name:  # Se um arquivo for selecionado
            self.imagem_path = file_name  # Armazena o caminho da imagem escolhida
            pixmap = QPixmap(file_name)  # Carrega a imagem
            self.area_imagem.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))  # Exibe a imagem redimensionada

    def cancelar(self):
        self.close()

#----------------------------Bloco principal para rodar o programa---------------------------------#

