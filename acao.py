def identificar(input):
    """
    {abrir, executar, rodar, instânciar} {chrome, excel, vs code}
    """

    listAcoes = ['abrir', 'executar', 'rodar', 'instânciar', 'instanciar']
    listApps = {
        'vscode': {
            'terms': 'vscode,visual studio code,vs code,code',
        },
        'word': {
            'terms': 'word,microsoft word,office word'
        },
        'excel': {
            'terms': 'excel,microsoft excel,office excel'
        },
        'chrome': {
            'terms': 'chrome,google chrome',
            'variables': {
                'url': 'url:,url,site:,site'
            }
        },
        'pesquisarGoogle': {
            'terms': 'pesquisar,buscar,pesquisa,busca,busque,procure,procura',
            'variables': {
                'search': 'busca'
            }
        },
        'previsao': {
            'terms': 'previsão do tempo,previsão,previsao,previsao do tempo,previsão tempo,previsao tempo,clima,temperatura,tempo',
            'variables': {
                'city': 'cidade:,cidade'
            }
        },
        'cotação': {
            'terms': 'cotação,cotacao,cotaçao,cotacão',
            'variables': {
                'currency': 'moeda:,moeda'
            }
        }
    }

    out ={
        'success': False,
        'phrase': '',
        'action': '',
        'app': None,
        'variables': {}
    }
    ### pegar ação (será desconsiderada)
    found = False
    for letter in input:
        out['phrase'] += letter
        for action in listAcoes:
            if action in out['phrase']:
                found = True
                break
        if found:
            break
    if found:
        out['action'] = input[:len(out['phrase'])]
        input = input[len(out['phrase']):]
    
    out['phrase'] = ''
    
    
    ### pegar aplicativo
    found = False
    for letter in input:
        out['phrase'] += letter
        for app in listApps.keys():
            for term in listApps[app]['terms'].split(','):
                if term in out['phrase']:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        out['success'] = True
        out['app'] = app
        input = input[len(out['phrase']):]
    
    out['phrase'] = ''




    # estava aqui
    ### pegar variaveis
    if out['app']:
        if 'variables' in listApps[out['app']].keys():
            found = False
            for letter in input:
                out['phrase'] += letter
                for variable in listApps[out['app']]['variables'].keys():
                    if term in out['phrase']:
                        found = True
                        break
                if found:
                    break
            if found:
                out['success'] = True
                out['app'] = app
                input = input[len(out['phrase']):]

    return out

if __name__ == '__main__':
    print(identificar('abrir chrome site bradesco.com'))