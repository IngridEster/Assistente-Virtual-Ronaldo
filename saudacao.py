import logging

NOME_DO_AGENTE = 'ronaldo'


def identificar(input):
    """
    Ex:
    Olá NOME_DO_AGENTE
    Oi NOME_DO_AGENTE
    Ok NOME_DO_AGENTE
    eae NOME_DO_AGENTE
    NOME_DO_AGENTE
    """

    listSaudacoes = ['olá', 'ola', 'oi', 'ok', 'eae']

    out = {'success': False, 'phrase': ''}
    found = False
    for letter in input:
        out['phrase'] += letter
        for saudacao in listSaudacoes:
            if saudacao in out['phrase']:
                if NOME_DO_AGENTE in out['phrase']:
                    found = True
                    break
        if NOME_DO_AGENTE in out['phrase']:
            found = True
        if found:
            break
    if found:
        out['success'] = True
        out['input'] = input[len(out['phrase']) :]

    return out


if __name__ == '__main__':
    logging.debug(identificar('olá'))
