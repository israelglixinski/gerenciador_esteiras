import git

# Nome do repositório online
REPO_URL = "https://github.com/seu_nome/seu_repositório.git"

# Pasta local do repositório
REPO_DIR = "/caminho/para/pasta/local"

# Nome da branch a ser clonada
BRANCH_NAME = "dev"

def main():
    # Clona o repositório
    git.clone(REPO_URL, REPO_DIR, branch=BRANCH_NAME)

if __name__ == "__main__":
    main()