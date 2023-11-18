import sqlite3

# Abre uma conexão com o banco de dados
conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()



def create_table_pids():
    cursor.execute("CREATE TABLE pids (proj TEXT, branch TEXT, pid BIGINT)")

def insert_pid():
    cursor.execute("INSERT INTO pids (proj, branch, pid) VALUES ('sac', 'master', 9927000)")
    conexao.commit()

def select_pid():
    cursor.execute("select * from pids")
    print(cursor.fetchall())

# create_table_pids()
# insert_pid()
select_pid()



conexao.close()







