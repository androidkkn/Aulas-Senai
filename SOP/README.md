# Curso de Sistemas Operacionais - 90H (120 Aulas)

## Módulo 1 - Introdução a Sistemas Operacionais

### Aula 1 - Apresentação do Curso

### Aula 2 - Sistemas Operacionais e Sistemas de Arquivos

- O que é Sistemas Operacionais
    - Kernel
    - Shell
    - Programas
    - Interfaces:
        - GUI
        - CLI
- Sistema de Arquivos
    - Tipos de Armazenamentos
    - Sistemas de Armazenamentos
        - FAT32
        - NTFS
        - EXT4
        - APFS
- Tipos de Sistemas Operacionais
    - Codigo Fechado (Licença de Uso)
        - Win e MacOS (Ios - Celular)
    - Codigo Aberto (CopyLeft)
        - Linux (Diversas Distros)
        - Android (Sistema Google é Fechado)

## Módulo 2 - Sistemas Operacional de Código Fechado (Windowns)

### Aula 1 - Introdução ao Ecossistema Windowns

- Histórico
    - MS-DOS (Sistema CLI)
    - Win 95 e 98 (Cascata Sobre o MS-DOS)
    - Win XP (Baseado no NT)
        -Interface GUI Mais Robusta
    - Win Vista, 7, 8 ,8.1 (Base do NT)
    - Win 10, Win 11 (Mais Recente)
- Tipos de Licença
    - OEM: Licença Instalada na Máquina, Morre Junto com a Máquina
    - FPP: Usuário Compra uma Licença de 25 digitos, pode ser Tranferida de uma Máquina para outra, só pode ser usada em uma Única Máquina por vez
    - VL: Licença para EMpresas, Comprada pelo nº de Computadores que a Empresa tem.
- Downloads do Win
    - Baixar a ISO (Formato Para Fazer BOOT) Diretamente do Site da Microsoft
    - Intalar o Media Create Tool
        - Baixar a ISO ou Criar um PenDrive Bootável
    - Usar o Assistente
        - Atualiza o Sistema da Máquina Atual
- Virtualização
    - Virtualização de Hardware (Profissional)
        - Usada em Servidores para Criar Vários Sistemas opreacionais em uma Máquina
        - Sistema em Desuso (Sistemas em Nuvem vem Ganhando Mercado)
    - Virtualização de SO (Host / Guest)
        - Criação de Guest (VM)
    - Quando Usar Virtualização:
        - Ultilização de Sistemas Antigos, Precisa Rodar um SO mais Antigo
        - Teste em Sistemas Operacionais (Linux, Android e IOs)
- Instalação de SO em Mundo Real
    - Baixar ISO
    - Ultilizar Rufus para CRriar um Pendrive Bootável (Inicializável)
    - Permite a Instalação do SO em Diversas Máquinas de Forma Rápida
    - Ultilização de Softwares de Clonagem
        - Winpe, Ghost, Clonezilla
        - Permite a Cópia de Máquinas Já Configuradas (Com SO e Softwares Instalados)

### Operação em Modo Gráfico (GUI)
- Dualidade da Interface
    - Menu de Configurações (UWP): voltado para a experiência do Usuário
    - Painel de Controle (Win32): motor do Sistema, Configurações mais Avançadas

    - Métricas de Desempenho:
        - Gargalo do Sistema:
            - CPU:
            - Disco:
            - Memória:
                - QUando a Memória Atinge 100% - SWAP (usar memória de armazenamento para processamento) - Melhor com SSD
- Ferramentas de Administrção e Gerenciamento
    - diskmgmt.msc (Gerenciamento de Disco)
        - FAT32 e NTFS (Controle de Acesso)
    - Controle de Acesso:
        - Heranla de Permissões: Pasta Herda as Características da Pasta Superior 
        - Desabilitar Herança é negar o acesso a todos os outros usuários
        - Adicionar Manualmente o Acesso
        - Controle Total: "CUIDADO"
