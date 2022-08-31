import functions as myf
from random import randint
file = '/home/l4ndrade/Documentos/Repositórios/Meus Projetos/dados.json'

while True:

    # MENU INICIAL:
    myf.tittle('Vamos jogar FORCA!')
    opt1 = myf.readint("""Escolha a sua opção:
    1 - Jogar
    2 - Adicionar Palavra
    3 - Remover palavras
    >""", 1, 3)
    myf.line()

    if opt1 == 1: # JOGAR
    # MENU INTERNO 1
        opt2 = myf.readint("""Como deseja jogar?
    1 - Jogar com palavra aleatória
    2 - Escolher palavra para a partida
    3 - Voltar
    >""", 1, 3)

        if opt2 == 1: # PALAVRA ALEATÓRIA
        # MENU INTERNO 1.1
            opt3 = myf.readint("""Deseja escolher a categoria ou prefere jogar com uma categoria aleatória? 
            [1] Escolher categoria
            [2] Categoria aleatória
            >""", 1 ,2)

            
            if opt3 == 1: # ESCOLHE CATEGORIA
            # MENU INTERNO 1.1.1
                cat = myf.readint("""Escolha a categoria:
            [1] - Alimentos
            [2] - Animais
            [3] - CEP (Cidade, estado ou país)
            [4] - Cores
            [5] - Nomes
            [6] - Objetos
            [7] - Profissões
            >""", 1, 7)
                cat = myf.catconv(cat)
            # CATEGORIA ALEATÓRIA
            else:
                cat = randint(1, 7)
                cat = myf.catconv(cat)

            json_dict = myf.openjson(file)
            word = json_dict[cat][randint(1, len(json_dict[cat])) - 1]

        elif opt2 == 2: # ESCOLHER PALAVRA
        # MENU INTERNO 1.2
            cat = myf.readalpha('Informe a categoria da palavra escolhida: ').capitalize().strip()
            word = myf.readalpha('Informe a palavra escolhida: ').strip()

        else: # VOLTAR
            continue


    elif opt1 == 2: # ADICIONAR PALAVRA
    # MENU INTERNO 2
        while True:
            json_dict = myf.openjson(file)
            cat = myf.readint("""Escolha a categoria onde a palavra será adicionada:
[1] - Alimentos
[2] - Animais
[3] - CEP (Cidade, estado ou país)
[4] - Cores
[5] - Nomes
[6] - Objetos
[7] - Profissões
>""", 1, 7)
            cat = myf.catconv(cat)
            word = myf.readalpha("""Digite a palavra que você quer adiconar
>""", json_dict[cat])
            myf.openjson(file, word, cat, 'add')
            print('Palavra adicionada com sucesso!')
            sn = myf.readint("""Deseja adicionar uma nova palavra?
[1] - SIM
[2] - NÃO
>""", 1, 2)
            if sn == 2:
                break


    else: # REMOVER PALAVRA
        cat = myf.readint("""Escolha a categoria da palavra deletada:
[1] - Alimentos
[2] - Animais
[3] - CEP (Cidade, estado ou país)
[4] - Cores
[5] - Nomes
[6] - Objetos
[7] - Profissões
>""", 1, 7)
        cat = myf.catconv(cat)
        while True:
            word = myf.readalpha('Digite a palavra que você quer deletar: ')
            try:
                myf.openjson(file, word=word, cat=cat, action='remove')
            except:
                print('A palavra usada nunca foi adicionada, por favor escolha outra!')
            else:
                print('Palavra removida com sucesso!')
                break
        


# ---------------------GAME-----------------------------

    if opt1 == 1:
        # DECLARAÇÃO DE VARIÁVEIS
        face = lleg = rleg = larm = body = ''
        rarm = ' '
        wordingame = list()
        usedletters = list()
        wordbackup = list(word)
        miss = 0
        loose = win = False
        for c in range(len(word)):
            wordingame.append('_')
        myf.tittle('O JOGO VAI COMEÇAR!')


        while True:
            error = True
            print(f'''
/-----\      Categoria: {cat}
|      |     Letras: {len(word)}
|    {face} 
|     {rarm}{body}{larm}
|      {body}
|      {rleg}{lleg}
|
|   
''')
            print(f'LETRAS USADAS: {usedletters}')

            if loose:
                print(f"""VOCÊ PERDEU!!!!
                A PALAVRA ERA {word}""")
                break
            if win:
                print('PARABÉNS, VOCÊ GANHOU!!!!')
                break

            for item in wordingame:
                print(item, end=' ')
            letter = myf.readalpha("""\nDigite uma letra para tentar acertar
>""", exceptionlst=usedletters)[0]
            usedletters.append(letter)

            for item in word:
                if letter == item:
                    pos = wordbackup.index(letter)
                    del wordingame[pos]
                    del wordbackup[pos]
                    wordingame.insert(pos, letter)
                    wordbackup.insert(pos, '_')
                    error = False
            if error == True:
                miss += 1
                if miss == 1:
                    face = '(o-o)'
                elif miss == 2:
                    body = '|'
                elif miss == 3:
                    rarm = '/'
                elif miss == 4:
                    larm = '\\'
                elif miss == 5:
                    rleg = '/'
                else:
                    lleg = '\\'
                    loose = True
            if '_' not in wordingame:
                win = True
# ---------------------FIM DO GAME-----------------------------
