import config
import os
import git


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
    print('\n')

    if os.path.exists(projeto.pasta_local_projeto): pass                                    #* VERIFICA SE EXISTE A PASTA QUE RECEBERÁ O PROJETO 
    else: os.makedirs(projeto.pasta_local_projeto)                                          #* CASO NÃO EXISTA, CRIA A PASTA

    ##### * VERIFICAMOS SE TEMOS A PASTA DO REPOSITÓRIO NA PASTA QUE RECEBERÁ O PROJETO
    if os.path.exists(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}'): 
        ##### * CASO JÁ EXISTA A PASTA VERIFICAMOS SE EXISTE A PASTA GIT
        if os.path.exists(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}/.git'): 
            ##### * CASO JÁ EXISTA A PASTA É SÓ REALIZAR O PULL
            repo = git.Repo(f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}')
            o = repo.remotes.origin
            o.pull()
            pass
        else:
            ##### * MAS SE NÃO EXISTIR A PASTA DO GIT, ENTÃO INFORMAMOS O ERRO. POIS NÃO SERÁ POSSIVEL CLONAR EM UMA PASTA JÁ EXISTENTE
            print(f"ERRO - VERIFIQUE O PROJETO: {projeto.nome_projeto}")
    else:
        ##### * SE AINDA NÃO EXISTE A PASTA DO REPOSITÓRIO ENTÃO FAZEMOS O CLONE DO REPOSITÓRIO
        git.Repo.clone_from(projeto.endereco_repositorio, f'{projeto.pasta_local_projeto}/{projeto.nome_projeto}')
        pass


