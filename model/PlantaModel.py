# Importa o módulo mysql.connector para conectar ao banco de dados MySQL
import mysql.connector

class PlantaModel:
    def __init__(self):
        """
        Inicializa a conexão com o banco de dados MySQL e cria um cursor para executar comandos SQL.
        """
        self.conexao = mysql.connector.connect(
            host="localhost",  # Endereço do servidor MySQL
            user="root",       # Usuário do banco de dados
            password="",       # Senha do banco de dados (nesse caso, vazia)
            database="plantas_db"  # Nome do banco de dados onde as plantas serão armazenadas
        )
        self.cursor = self.conexao.cursor()  # Cria um cursor para interagir com o banco de dados

    def inserir_planta(self, nome_popular, nome_cientifico, imagem_path):
        """
        Insere uma nova planta na tabela 'plantas' do banco de dados.

        Parâmetros:
        - nome_popular: Nome popular da planta
        - nome_cientifico: Nome científico da planta
        - imagem_path: Caminho da imagem associada à planta

        Retorna:
        - O ID da última planta inserida no banco de dados
        """

        sql = "INSERT INTO plantas_db (nome_popular, nome_científico, imagem_path) VALUES (%s, %s, %s)"
        valores = (nome_popular, nome_cientifico, imagem_path)
        self.cursor.execute(sql, valores)  # Executa a inserção no banco de dados
        self.conexao.commit()  # Confirma a transação
        return self.cursor.lastrowid  # Retorna o ID da planta recém-inserida
    
    def atualizar_planta(self, planta_id, nome_popular, nome_cientifico):
        sql = """
        UPDATE plantas_db
        SET nome_popular = %s, nome_científico = %s
        WHERE id = %s
        """

        valores = (nome_popular, nome_cientifico, planta_id)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    def deletar_planta(self, planta_id):
        sql = """
        DELETE FROM plantas_db WHERE id = %s
        """
        valores = (planta_id,)
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    
    def listar_plantas(self):
        sql = "SELECT * FROM plantas_db;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.cursor.close()  # Fecha o cursor
        self.conexao.close()  # Fecha a conexão com o banco de dados
    
