import psycopg2 as pg
#pip ijnstall psycopg2
#pip install dotenv
from dotenv import load_dotenv     
import os 

#carregar as variaveis de ambiente do arquivo .env
load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}
def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        print("Deu certo")
        return conexao, cursor
    except Exception as e:
        print("Erro de conexao {erro}")
        return None, None
    



                   

   




