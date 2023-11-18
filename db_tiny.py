import tinydb
from tinydb import Query,where

##### * Definição do banco de dados
db_tiny = tinydb.TinyDB("db_tiny.json")

##### * Definição das tabelas
projetos            = db_tiny.table("projetos")
configs             = db_tiny.table("configs")


def insert_projetos(
 nome_proj
,url_rep
,destino_local
,script_inicial
,script_inicial_pid
,branchs
,monitoramento
,monitoramento_param
,monitoramento_valores
):
    projetos.insert(
        {
         "nome_proj"                : nome_proj        
        ,"url_rep"                  : url_rep          
        ,"destino_local"            : destino_local    
        ,"script_inicial"           : script_inicial   
        ,"script_inicial_pid"       : script_inicial_pid   
        ,"branchs"                  : branchs          
        ,"monitoramento"            : monitoramento
        ,"monitoramento_param"      : monitoramento_param
        ,"monitoramento_valores"    : monitoramento_valores
        }        
    )
    pass

def insert_configs(tempo_loop_minutos):
    configs.insert({"tempo_loop_minutos":tempo_loop_minutos})
    pass

def update_pid(nome_proj,pid):
    querry_nome_proj = Query()
    projetos.update(fields={'script_inicial_pid': pid},cond=querry_nome_proj["nome_proj"] == nome_proj)
    pass

def popula_inicial():
    insert_configs(tempo_loop_minutos=1)

    insert_projetos(
     nome_proj              = "exemplo_robo"
    ,url_rep                = "https://github.com/israelglixinski/exemplo_robo.git"
    ,destino_local          = "C:/Projetos"
    ,script_inicial         = "main.py"
    ,script_inicial_pid     = 0
    ,branchs                = ["main"]
    ,monitoramento          = "log"
    ,monitoramento_param    =   {"path_log_file"        : "./logs/log.txt"
                                ,"minutos_max_sem_alt"  : 5
                                }
    ,monitoramento_valores  =   {"ultima_alteracao"     : None}
    )

    insert_projetos(
     nome_proj              = "exemplo_web"
    ,url_rep                = "https://github.com/israelglixinski/exemplo_web.git"
    ,destino_local          = "C:/Projetos"
    ,script_inicial         = "inicial.py"
    ,script_inicial_pid     = 0
    ,branchs                = ["main"]
    ,monitoramento          = "web"
    ,monitoramento_param    =   {"url"                           : "localhost"
                                ,"max_tentativas"                :5
                                ,"segundos_max_cada_tentativa"   :60
                                }
    ,monitoramento_valores  =   {"ultima_confirmacao":None}
    )
    pass

def recupera_configs():
    class Obj_configs:
        def __init__(self):
            self.tempo_loop_minutos = None
            pass
    obj_configs = Obj_configs()

    querry_configs = Query()
    obj_configs.tempo_loop_minutos = configs.search(querry_configs["tempo_loop_minutos"].exists())[-1]["tempo_loop_minutos"]
    
    return obj_configs


if __name__ == '__main__':
    # configs.insert({"teste":"primeiro"})
    recupera_configs()



    pass

