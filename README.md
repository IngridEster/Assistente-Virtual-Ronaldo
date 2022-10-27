# Assistente-Virtual-Ronaldo
Aplicação responsável em pegar o input do usuário e executar as ações.

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

# Utilização
O ronaldo entende frases formatadas seguindo um padrão conforme descrito abaixo:
```
{
   'olá', 'ola', 'oi', 'ok', 'eae'
}
   ronaldo
{
   'abrir', 'executar', 'rodar', 'instânciar', 'instanciar', 'adicionar'
}
{
   vscode, visual studio code, vs code, code
   word, microsoft word, office word
   excel, microsoft excel, office excel
   chrome, google chrome
   previsão do tempo, previsão, previsao, previsao do tempo, previsão tempo, previsao tempo, clima, temperatura, tempo
   cotação, cotacao, cotaçao, cotacão
   lembrete
   traduzir
   pesquisar, buscar, procurar, busque
}
```
O ronaldo consegue responder frases como as dos exemplos abaixo:
 - Ok ronaldo cotação
 - Ok ronaldo adicionar lembrete ir ao mercado
 - Olá ronaldo abrir chrome
 - Olá ronaldo previsão do tempo para jaraguá do sul
 - Olá ronaldo traduzir eu fui ao mercado
 - Ronaldo abrir vscode
 - Oi ronaldo pesquisar por Elvis Presley