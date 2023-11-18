import tinydb

##### * Definição do banco de dados
db_tiny = tinydb.TinyDB("embedded_db_tinydb.json")

##### * Definição das tabelas
configs_projetos    = db_tiny.table("configs_projetos")
configs_geral       = db_tiny.table("configs_geral")


def insert_configs_projetos(
 nome_proj
,url_rep
,destino_local
,script_inicial
,branchs
):
    configs_projetos.insert(
        {
         "nome_proj"        : nome_proj        
        ,"url_rep"          : url_rep          
        ,"destino_local"    : destino_local    
        ,"script_inicial"   : script_inicial   
        ,"branchs"          : branchs          
        }        
    )
    pass

if __name__ == '__main__':

    # insert_configs_projetos(
    #  nome_proj      = "IGPyAppFront"
    # ,url_rep        = "https://github.com/israelglixinski/IGPyAppFront.git"
    # ,destino_local  = "C:/Projetos"
    # ,script_inicial = "main.py"
    # ,branchs        = ["master","hom","dev"]
    # )
    
    # insert_configs_projetos(
    #  nome_proj      = "IGdfPyAppFront"
    # ,url_rep        = "https://github.com/israelglixinski/IGPyAppFront.git"
    # ,destino_local  = "C:/Projetos"
    # ,script_inicial = "main.py"
    # ,branchs        = ["master","hom","dev"]
    # )


    pass

