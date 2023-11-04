
class Projeto_config():
    'Cria o objeto que receberá as configurações do projeto'
    def __init__(self
    ,nome_projeto       
    ,endereco_repositorio    
    ,pasta_local_projeto     
    ,branch_producao         
    ,branch_homologacao      
    ,branch_desenvolvimento  
    ,script_inicial          
    ) :
        self.nome_projeto               = nome_projeto                          #* DE PREFERENCIA O MESMO NOME DO PROJETO NO REPOSITÓRIO  
        self.endereco_repositorio       = endereco_repositorio                  #* URL DO ARQUIVO .GIT DO REPOSITÓRIO
        self.pasta_local_projeto        = pasta_local_projeto                   #* PASTA LOCAL QUE RECEBERÁ A PASTA DO REPOSITÓRIO CLONADO
        self.branch_producao            = branch_producao                       #* NOME DA BRANCH DE PRODUÇÃO
        self.branch_homologacao         = branch_homologacao                    #* NOME DA BRANCH DE HOMOLOGAÇÃO
        self.branch_desenvolvimento     = branch_desenvolvimento                #* NOME DA BRANCH DE DESENVOLVIMENTO
        self.script_inicial             = script_inicial                        #* SCRIPT PYTHON QUE SERÁ INICIADO OU REINICIADO A CADA ATUALIZAÇÃO



proj_IGPyAppFront                       = Projeto_config(
    nome_projeto                        = 'IGPyAppFront'
    ,endereco_repositorio               = 'https://github.com/israelglixinski/IGPyAppFront.git' 
    ,pasta_local_projeto                = 'C:/Projetos'
    ,branch_producao                    = 'master'
    ,branch_homologacao                 = 'hom'
    ,branch_desenvolvimento             = 'dev'
    ,script_inicial                     = 'main.py'
    )

proj_bot_sms                            = Projeto_config(
    nome_projeto                        = 'bot_sms'
    ,endereco_repositorio               = 'https://github.com/israelglixinski/bot_sms.git' 
    ,pasta_local_projeto                = 'C:/Projetos'
    ,branch_producao                    = 'master'
    ,branch_homologacao                 = 'hom'
    ,branch_desenvolvimento             = 'dev'
    ,script_inicial                     = 'main.py'
    )



##### * AQUI DEFINIMOS OS PROJETOS QUE DESEJAMOS QUE SEJAM MONITORADOS
lista_projetos_executar = [proj_IGPyAppFront,proj_bot_sms]


