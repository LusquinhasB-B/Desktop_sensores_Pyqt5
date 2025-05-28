import mysql.connector

class ModelDados():
    def __init__(self):

        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas_db"
        )
        self.cursor = self.conexao.cursor()

    def inserir_dados(self, temperatura, umidade, luminosidade):
        sql = "INSERT INTO dados (temperatura, umidade, luminosidade) VALUES (%s, %s, %s)"
        valores = (temperatura, umidade, luminosidade)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        return self.cursor.lastrowid
    
    def editar_sensores(self, dados_id, temperatura, umidade, luminosidade ):
        sql = """
        UPDATE dados
        SET temperatura = %s, umidade = %s, luminosidade = %s
        WHERE id_dados = %s
        """
        valores = (temperatura, umidade, luminosidade, dados_id)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    def deletar_sensores(self, dados_id):
        sql = """
        DELETE FROM dados WHERE id_dados = %s
        """
        valores = (dados_id,)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
    
    def listar_dados(self):
        sql = "SELECT * FROM dados;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()  

        
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

    