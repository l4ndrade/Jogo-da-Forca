import json


def line(txt='-', tam=30):
    print(txt * tam)


def tittle(txt):
    line('-', len(txt)+4)
    print(txt.center((len(txt)+4)))
    line('-', len(txt)+4)


def readint(txt, min, max):
    """
    txt -> Texto do input;
    min -> número mínimo aceito como resposta;
    max -> número máximo aceito como resposta.
    """
    while True:
        try:
            a = int(input(txt))
        except ValueError:
            print('\033[1;31mERRO: Digite um valor inteiro válido!\033[m')
        else:
            if min <= a <= max:
                return a
            else:
                print(f'\033[1;31mERRO: Digite um valor entre {min} e {max}\033[m')


def openjson(file, word='', cat='', action='returndict'):
    try:
        with(open)(file) as json_file:
            json_dict = json.load(json_file)
        if action == 'returndict':
            return json_dict
        elif action == 'add':
            json_dict[cat].append(word)
            json_dumped = json.dumps(json_dict, separators=(',', ':'))
        elif action == 'remove':
            json_dict[cat].remove(word)
            json_dumped = json.dumps(json_dict, separators=(',', ':'))
        if action != 'returndict':
            with open(file, 'w') as json_file:
                json_file.write(json_dumped)
    except:
        print('Ação escolhida não pode ser executada')


def catconv(cat):
    if cat == 1:
        cat = "alimentos"
    elif cat == 2:
        cat = "animais"
    elif cat == 3:
        cat = "cep"
    elif cat == 4:
        cat = "cores"
    elif cat == 5:
        cat = "nomes"
    elif cat == 6:
        cat = "objetos"
    else:
        cat = "emprego" 
    return cat


def readalpha(txt, exceptionlst=[]):
    """
    txt -> Texto do input;
    exceptionlst -> lista de palavras que a função não aceita.
    """
    while True:
        a = str(input(txt)).strip()
        if a.isalpha():
            if a not in exceptionlst:
                break
            else:
                print(f'\n\033[1;31mA letra {a} já foi usada!\033[m')  
        else:
            print('\n\033[1;31mIsso não é uma letra, tente novamente!\033[m')
    return a
