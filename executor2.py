from time import sleep
import config
import git
import os



for projeto in config.lista_projetos_executar:
    
    ##### * PARA TESTE DAS VARIAVEIS DO PROJETO 
    print('\n')
    print(f'nome_projeto            = {projeto.nome_projeto             }')
    print(f'endereco_repositorio    = {projeto.endereco_repositorio     }')
    print(f'pasta_local_projeto     = {projeto.pasta_local_projeto      }')
    print(f'branch_producao         = {projeto.branch_producao          }')
    print(f'branch_homologacao      = {projeto.branch_homologacao       }')
    print(f'branch_desenvolvimento  = {projeto.branch_desenvolvimento   }')
    print(f'script_inicial          = {projeto.script_inicial           }')
    print(f'lista_ambientes_ativos  = {projeto.lista_ambientes_ativos   }')
    print('\n')

    for branch_proj in projeto.lista_ambientes_ativos:
        if branch_proj == 'PROD': my_branch = projeto.branch_producao
        if branch_proj == 'HOM' : my_branch = projeto.branch_homologacao
        if branch_proj == 'DEV' : my_branch = projeto.branch_desenvolvimento

        path_branch_repositorio = f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}/{my_branch}'
        if os.path.exists(branch_proj):  pass
        else: os.makedirs(branch_proj)

        if os.path.exists(f'{branch_proj}/.git') == False: 
            git.Repo.clone(projeto.endereco_repositorio, path_branch_repositorio,branch=my_branch)
        else:


            pass











    if os.path.exists(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}'): 
        ##### * CASO JÁ EXISTA A PASTA VERIFICAMOS SE EXISTE A PASTA GIT
        if os.path.exists(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}/.git'): 
            ##### * CASO JÁ EXISTA A PASTA É SÓ REALIZAR O PULL
            repositorio = git.Repo(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}')
            repositorio_remoto = repositorio.remotes.origin 

            last_commit_local = repositorio.commit().committed_datetime
            last_commit_remot = repositorio_remoto.fetch()[0].commit.committed_datetime
        
            if last_commit_local == last_commit_remot:
                print(f"{projeto.nome_projeto} - Estamos com a versão mais recente")
            else:
                print(f"{projeto.nome_projeto} - Precisamos atualizar o repositório")
                repositorio_remoto.pull()
            sleep(3)
            pass
        
        else:
            ##### * MAS SE NÃO EXISTIR A PASTA DO GIT, ENTÃO INFORMAMOS O ERRO. POIS NÃO SERÁ POSSIVEL CLONAR EM UMA PASTA JÁ EXISTENTE
            print(f"ERRO - VERIFIQUE O PROJETO: {projeto.nome_projeto}")
    else:
        ##### * SE AINDA NÃO EXISTE A PASTA DO REPOSITÓRIO ENTÃO FAZEMOS O CLONE DO REPOSITÓRIO
        git.Repo.clone_from(projeto.endereco_repositorio, f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}')
        pass

