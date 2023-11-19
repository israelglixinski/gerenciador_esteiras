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
,script_inicial
,script_inicial_pid
,branch
,verify
,verify_ult_confirm
,verify_log_path
,verify_log_min_inalt
,verify_web_url
,verify_web_max_try
,verify_web_timeout_max
):
    projetos.insert(
        {
         "nome_proj"                : nome_proj        
        ,"url_rep"                  : url_rep          
        ,"script_inicial"           : script_inicial   
        ,"script_inicial_pid"       : script_inicial_pid   
        ,"branch"                   : branch          
        ,"verify"                   : verify
        ,"verify_ult_confirm"       : verify_ult_confirm
        ,"verify_log_path"          : verify_log_path
        ,"verify_log_min_inalt"     : verify_log_min_inalt
        ,"verify_web_url"           : verify_web_url
        ,"verify_web_max_try"       : verify_web_max_try
        ,"verify_web_timeout_max"   : verify_web_timeout_max
        }        
    )
    pass

def insert_configs(tempo_loop_minutos,destino_local):
    configs.insert({"tempo_loop_minutos"    :tempo_loop_minutos })
    configs.insert({"destino_local"         :destino_local      })
    pass

def update_pid(nome_proj,pid):
    querry_nome_proj = Query()
    projetos.update(fields={'script_inicial_pid': pid},cond=querry_nome_proj["nome_proj"] == nome_proj)
    pass

def popula_inicial():
    
    insert_configs(
         tempo_loop_minutos = 1
        ,destino_local      = "c:/Projetos"
        )

    insert_projetos(
        nome_proj               = "exemplo_robo"
        ,url_rep                = "https://github.com/israelglixinski/exemplo_robo.git"
        ,script_inicial         = "main.py"
        ,script_inicial_pid     = 0
        ,branch                 = "main"
        ,verify                 = "log"
        ,verify_ult_confirm     = None
        ,verify_log_path        = "./logs/log.txt"
        ,verify_log_min_inalt   = 5
        ,verify_web_url         = None
        ,verify_web_max_try     = None
        ,verify_web_timeout_max = None
        )

    insert_projetos(
        nome_proj               = "exemplo_web"
        ,url_rep                = "https://github.com/israelglixinski/exemplo_web.git"
        ,script_inicial         = "inicial.py"
        ,script_inicial_pid     = 0
        ,branch                 = "main"
        ,verify                 = "web"
        ,verify_ult_confirm     = None
        ,verify_log_path        = None
        ,verify_log_min_inalt   = None
        ,verify_web_url         = "localhost"
        ,verify_web_max_try     = 5
        ,verify_web_timeout_max = 2
        )
    pass

def recupera_configs():
    class Obj_configs:
        def __init__(self):
            self.tempo_loop_minutos     = None
            self.destino_local          = None
            pass
    obj_configs = Obj_configs()

    querry_configs = Query()
    obj_configs.tempo_loop_minutos  = configs.search(querry_configs["tempo_loop_minutos"    ].exists())[-1]["tempo_loop_minutos"    ]
    obj_configs.destino_local       = configs.search(querry_configs["destino_local"         ].exists())[-1]["destino_local"         ]
    
    return obj_configs

def recupera_projeto(nome_proj):
    querry_projeto = Query()
    consulta = projetos.search(querry_projeto["nome_proj"] == nome_proj)[0]
    return consulta


if __name__ == '__main__':
    # configs.insert({"teste":"primeiro"})
    popula_inicial()
    # recupera_configs()
    # recupera_projeto('exemplo_robo')


    pass

