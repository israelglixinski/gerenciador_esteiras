import tinydb

# Cria um banco de dados
db = tinydb.TinyDB("database.json")

# Cria uma tabela
table = db.table("usuarios")

# Insere um registro
table.insert({"nome": "João", "idade": 25})

# Lista todos os registros
for registro in table:
    print(registro)