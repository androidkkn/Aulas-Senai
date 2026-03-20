// inicia o git (repositório) no seu projeto
    git init

// adiciona todos os arquivos modificados, ao stage
    git add .

// cria e descreve um ponto na história
    git commit -m "message here"

// envia alterações para o repositório remoto
    git push

// pucha as alterações para o repositório online
    git pull

// mostra o status de versionamentos dos arquivos
    git status

// configura o git local ao seu git hub 
    - git config --global user.name "[nome do seu perfil no github]"

    - git config --global user.email "[seu email que esta cadastrado no github]"

// cria a branch entrando nela
    - git switch -c [nome]
    ou
    - git checkout -b [nome]

// cria multiplas branch's de uma só vez
    git branch [nome] && git branch [nome2]... (pode ser infinito)

// deleta uma ou mais branch's de uma so vez
    - git branch -d [nome]
    ou
    - git branch -d [nome1] [nome2] [nome3]