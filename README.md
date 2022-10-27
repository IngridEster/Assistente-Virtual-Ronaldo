# Assistente-Virtual-Ronaldo
Aplicação frontend responsável em pegar o input do usuário e fazer as ações. 

# Requisitos
1. Ter o python versão >= 3.11
2. Pedir os arquivos a Ingrid ou Johan e colar na pasta de execução da ferramenta
   - .google_api_key
   - .hgbrasil_api_key

# Para rodar a aplicação
1. Criar virtual env
```
python -m venv env
```
2. Ativar venv de acordo com o sistema operacional

| Platform | Shell | Command to activate virtual environment |
| --- | --- | --- |
| POSIX | bash/zsh | $ source <venv>/bin/activate |
| POSIX | fish | $ source <venv>/bin/activate.fish |
| POSIX | csh/tcsh | $ source <venv>/bin/activate.csh |
| POSIX | PowerShell | $ <venv>/bin/Activate.ps1 |
| Windows | cmd.exe | C:\\> <venv>\Scripts\activate.bat |
| Windows | PowerShell | PS C:\\> <venv>\Scripts\Activate.ps1 |

3. Com a venv ativa execute o comando abaixo para instalar as dependências
```
pip install -r requirements.txt
```
4. Após fazer isso pode executar o projeto dando o comando abaixo
```
python server.py
```