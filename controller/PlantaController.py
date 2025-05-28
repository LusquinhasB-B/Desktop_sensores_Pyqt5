# Importa a classe PlantaModel do módulo model
from model.PlantaModel import PlantaModel
from menu_tela import Menu

class PlantaController:
    def __init__(self):
        # Cria uma instância do modelo de planta para interagir com o banco de dados
        self.model = PlantaModel()

    def salvar_planta(self, nome_popular, nome_cientifico, imagem_path):

        """
        Salva uma nova planta no banco de dados.

        Parâmetros:
        - nome_popular: Nome popular da planta
        - nome_cientifico: Nome científico da planta
        - imagem_path: Caminho da imagem associada à planta

        Retorna:
        - O ID da planta inserida no banco de dados, se os dados forem válidos
        - None se os campos obrigatórios não forem preenchidos
        """
        if nome_popular and nome_cientifico:
            return self.model.inserir_planta(nome_popular, nome_cientifico, imagem_path)
        return None
    
    def atualizar_planta(self, planta_id, nome_popular, nome_cientifico):
        """  
        Atualiza os dados de uma planta no banco de dados.
        """
        if nome_popular and nome_cientifico:
            return self.model.atualizar_planta(planta_id, nome_popular, nome_cientifico)
        return None
    
    def deletar_planta(self, planta_id):
        """
        Serve para deletar uma linha da tabela 'plantas_db'
        """
        if planta_id:
            return self.model.deletar_planta(planta_id)
    
    def voltar_home(self):
        return self.



    def obter_plantas(self):
        return self.model.listar_plantas()