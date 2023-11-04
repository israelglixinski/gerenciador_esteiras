



class Projeto_config():

    def __init__(self
    ,nome_configuracao       
    ,endereco_repositorio    
    ,pasta_local_projeto     
    ,branch_producao         
    ,branch_homologacao      
    ,branch_desenvolvimento  
    ,script_inicial          
    ) :
        self.nome_configuracao       = nome_configuracao       
        self.endereco_repositorio    = endereco_repositorio    
        self.pasta_local_projeto     = pasta_local_projeto     
        self.branch_producao         = branch_producao         
        self.branch_homologacao      = branch_homologacao      
        self.branch_desenvolvimento  = branch_desenvolvimento  
        self.script_inicial          = script_inicial          





proj_IGPyAppFront               = Projeto_config(
    nome_configuracao           = 'IGPyAppFront'
    ,endereco_repositorio       = 'https://github.com/israelglixinski/IGPyAppFront.git' 
    ,pasta_local_projeto        = 'C:/Projetos'
    ,branch_producao            = 'master'
    ,branch_homologacao         = 'hom'
    ,branch_desenvolvimento     = 'dev'
    ,script_inicial             = 'main.py'
    )

proj_bot_sms                    = Projeto_config(
    nome_configuracao           = 'bot_sms'
    ,endereco_repositorio       = 'https://github.com/israelglixinski/bot_sms.git' 
    ,pasta_local_projeto        = 'C:/Projetos'
    ,branch_producao            = 'master'
    ,branch_homologacao         = 'hom'
    ,branch_desenvolvimento     = 'dev'
    ,script_inicial             = 'main.py'
    )


lista_projetos_executar = [proj_IGPyAppFront,proj_bot_sms]


