from model.DadosModel import ModelDados

class DadosController:
    def __init__(self):
        self.model = ModelDados()
  

    def salvar_dados(self, temperatura, umidade, luminosidade):

        if temperatura and umidade and luminosidade:
            return self.model.inserir_dados(temperatura, umidade, luminosidade)
        return None
    
    def atualizar_sensores(self, dados_id, temperatura, umidade, luminosidade):
        """
        Atualiza os dados de uma planta no banco de dados.
        """
        if temperatura and umidade and luminosidade:
            return self.model.editar_sensores(dados_id, temperatura, umidade, luminosidade)
        return None
    
    def deletar_sensores(self, dados_id):
        if dados_id:
            return self.model.deletar_sensores(dados_id)
    
    def obter_dados(self):
        return self.model.listar_dados()
    