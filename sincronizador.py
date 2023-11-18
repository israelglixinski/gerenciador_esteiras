from subprocess import Popen
import db_tiny
from time import sleep
import git
import os
from datetime import datetime



projetos = db_tiny.projetos

##### * definir todos os projetos como não inicializados
##### * fazer setando os pids como zero





def executar():
    for projeto in projetos:
        for branch in projeto["branchs"]:
            path_branch_repositorio = f'{projeto["destino_local"]}/{projeto["nome_proj"]}/{branch}'
            if os.path.exists(path_branch_repositorio):  pass
            else: os.makedirs(path_branch_repositorio)

            if os.path.exists(f'{path_branch_repositorio}/.git') == False: 
                git.Repo.clone_from(projeto["url_rep"], path_branch_repositorio,branch=branch)
                start_processo = Popen(f'python {path_branch_repositorio}/{projeto["script_inicial"]}')           
                db_tiny.update_pid(projeto['nome_proj'],start_processo.pid)


            else:
                repositorio = git.Repo(path_branch_repositorio)
                repositorio_remoto = repositorio.remotes.origin 

                last_commit_local = repositorio.commit().committed_datetime
                last_commit_remot = repositorio_remoto.fetch()[0].commit.committed_datetime
            
                if last_commit_local == last_commit_remot:
                    print(f"{projeto['nome_proj']} / {branch} - Estamos com a versão mais recente")

                else:
                    print(f"{projeto['nome_proj']} / {branch} - Precisamos atualizar o repositório")
                    repositorio_remoto.pull()
                sleep(3)

def iniciar_projetos():
    for projeto in projetos:
        for branch in projeto["branchs"]:
            path_branch_repositorio = f'{projeto["destino_local"]}/{projeto["nome_proj"]}/{branch}'
            
            start_processo = Popen(f'python {path_branch_repositorio}/{projeto["script_inicial"]}')           
            print (f'{projeto["script_inicial"]} - {start_processo.pid}')
            db_tiny.update_pid(projeto['nome_proj'],start_processo.pid)
            

            pass
    pass


def orquestrador():
    while True:
        # executar()
        print(datetime.now())
        configs = db_tiny.recupera_configs()
        sleep(60*configs.tempo_loop_minutos)
        pass

if __name__ == '__main__':
    orquestrador()
