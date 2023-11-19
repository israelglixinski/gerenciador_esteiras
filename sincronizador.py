from datetime import datetime
from subprocess import Popen
from time import sleep
import db_tiny
import git
import os


##### * Carregamento inicial das informações do banco
projetos    = db_tiny.projetos
configs     = db_tiny.recupera_configs()

def registrando(texto):
    '''Para registro, exibição e monitoração das ações'''
    print(f'{datetime.now().strftime("%Y/%m/%d %H:%M:%S")} - {texto}')

def iniciar_servico_projeto(nome_projeto):
    projeto = db_tiny.recupera_projeto(nome_projeto)
    path_script_inicial = f'{configs.destino_local}/{projeto["nome_proj"]}/{projeto["branch"]}/{projeto["script_inicial"]}'
    start_processo = Popen(f'python {path_script_inicial}')   
    db_tiny.update_pid(projeto['nome_proj'],start_processo.pid)
    pass


##### * Define todos os projetos como não inicializados, setando o PID como zero
for projeto in projetos:
    db_tiny.update_pid(projeto['nome_proj'],0)

def rotina():
    '''Ações principais para sincronização e execução dos projetos'''
    
    ##### * Para cada projeto na lista de projetos
    for projeto in projetos:
        registrando(f"Trabalhando com o projeto: '{projeto['nome_proj']}'")
        
        ##### * Caminho em que será trabalhado no projeto
        path_branch_repositorio = f'{configs.destino_local}/{projeto["nome_proj"]}/{projeto["branch"]}'
        
        ##### * Verifica se a pasta de destino do projeto já existe
        if os.path.exists(path_branch_repositorio):  pass                                   #* Caso a pasta já exista não é necessário mais ações
        else:                                                                               #* Mas caso não exista é necessário criala
            registrando('Não foi encontrado a pasta de destino do projeto')
            os.makedirs(path_branch_repositorio)
            registrando('Criado uma nova pasta para trabalhar no projeto')

        ##### * Verificação se já temos o repositório clonado na pasta de destino
        if os.path.exists(f'{path_branch_repositorio}/.git') == False:                      #* Caso ainda não esteja clonado, énecessário clonar           
            registrando('Não foi encontrado o repositório, iniciando clone...') 
            git.Repo.clone_from(projeto["url_rep"], path_branch_repositorio,branch=projeto["branch"])
            registrando('Finalizado clone') 
            iniciar_servico_projeto(projeto["nome_proj"])                                   #* Inicia o script inicial do projeto


        else:
            repositorio = git.Repo(path_branch_repositorio)
            repositorio_remoto = repositorio.remotes.origin 

            last_commit_local = repositorio.commit().committed_datetime
            last_commit_remot = repositorio_remoto.fetch()[0].commit.committed_datetime
        
            if last_commit_local == last_commit_remot:
                registrando(f'{projeto["nome_proj"]} / {projeto["branch"]} - Estamos com a versão mais recente')

            else:
                registrando(f'{projeto["nome_proj"]} / {projeto["branch"]} - Precisamos atualizar o repositório')
                repositorio_remoto.pull()
            sleep(3)

def iniciar_projetos():
    for projeto in projetos:
        path_branch_repositorio = f'{configs.destino_local}/{projeto["nome_proj"]}/{projeto["branch"]}'
        
        start_processo = Popen(f'python {path_branch_repositorio}/{projeto["script_inicial"]}')           
        print (f'{projeto["script_inicial"]} - {start_processo.pid}')
        db_tiny.update_pid(projeto['nome_proj'],start_processo.pid)
            

        pass
    pass


def orquestrador():
    while True:
        registrando('Iniciando rotina')
        rotina()
        registrando('Finalizado rotina')
        configs = db_tiny.recupera_configs()
        sleep(60*configs.tempo_loop_minutos)
        pass

if __name__ == '__main__':
    orquestrador()
