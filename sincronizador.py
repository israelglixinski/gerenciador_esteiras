from subprocess import Popen
import embedded_db_tinydb
from time import sleep
import git
import os


configs_projetos = embedded_db_tinydb.configs_projetos





def executar():

    for projeto in configs_projetos:
        
        #######################################################
        ##### * PARA TESTE DAS VARIAVEIS DO PROJETO 
        #######################################################
        print('\n')
        print (f'projeto.nome_proj      = {projeto["nome_proj"      ]}')
        print (f'projeto.url_rep        = {projeto["url_rep"        ]}')
        print (f'projeto.destino_local  = {projeto["destino_local"  ]}')
        print (f'projeto.script_inicial = {projeto["script_inicial" ]}')
        for branch in projeto["branchs"]:print (f'branch = {branch}')
        print('\n')
        #######################################################

        for branch in projeto["branchs"]:
            path_branch_repositorio = f'{projeto["destino_local"]}/{projeto["nome_proj"]}/{branch}'
            if os.path.exists(path_branch_repositorio):  pass
            else: os.makedirs(path_branch_repositorio)

            if os.path.exists(f'{path_branch_repositorio}/.git') == False: 
                git.Repo.clone_from(projeto["url_rep"], path_branch_repositorio,branch=branch)
                start_processo = Popen(f'python {projeto["script_inicial"]}')           
                print (f'{projeto["script_inicial"]} - {start_processo.pid}')
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

if __name__ == '__main__':
    executar()
