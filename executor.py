import config



for projeto in config.lista_projetos_executar:

    print('\n')
    print(f'nome_configuracao       = {projeto.nome_configuracao       }')
    print(f'endereco_repositorio    = {projeto.endereco_repositorio    }')
    print(f'pasta_local_projeto     = {projeto.pasta_local_projeto     }')
    print(f'branch_producao         = {projeto.branch_producao         }')
    print(f'branch_homologacao      = {projeto.branch_homologacao      }')
    print(f'branch_desenvolvimento  = {projeto.branch_desenvolvimento  }')
    print(f'script_inicial          = {projeto.script_inicial          }')
    print('\n')


