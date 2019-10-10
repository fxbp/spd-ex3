import string
## Métodes de railFence reaprofitats de l'exercici 1-----------------------------------------------

def obtenirNovaPosicio(posicio, rail, desp, diff, mida):
    # calcula la seguent posicio en base al nombre de num_rails
    if diff == 0:
        diff = desp
    # si diff = 0 es que som al primer o ultim rail, per tant hem de moure desp cada cop
    posicio = posicio + diff
    diff = desp-diff
    # excepte el primer i ultim rail, tots els rails tenen 2 desplaçaments:
    # el primer a desp - rail*2
    # el segon a rail*2
    # utilitza la variable diff per intercanviar aquest 2 desplaçaments
    if posicio >= mida:
        rail +=1;
        posicio = rail
        diff  = desp -2*rail

    return posicio, rail, diff

def codificaRailFence(missatge, num_rails):
# retorna el missatge xifrat tipus rail Fence utilitzant num_rails
    xifrat = [0 for x in range(len(missatge))]
    rail = 0;
    posicio = rail;
    desp = 2*num_rails -2
    if num_rails==1:
        desp = 1
    # desp son les posicions que ha de desplaçar el primer rail
    diff  = 0
    for k in range(len(missatge)):
        xifrat[k]= missatge[posicio]
        posicio, rail, diff = obtenirNovaPosicio(posicio,rail, desp, diff, len(missatge))

    return "".join(str(x) for x in xifrat)

def descodificaRailFence(missatge, num_rails):
# retorna el missatge dexifrat utilitzant el metode rail Fence i num_rails
    desxifrat = [0 for x in range(len(missatge))]
    rail = 0;
    posicio = rail;
    desp = 2*num_rails -2
    if num_rails==1:
        desp = 1
    # desp son les posicions que ha de desplaçar el primer rail
    diff  = 0
    for k in range(len(missatge)):
        desxifrat[posicio] = missatge[k]
        posicio, rail, diff = obtenirNovaPosicio(posicio,rail, desp, diff, len(missatge))

    return "".join(str(x) for x in desxifrat)


## FUNCIONS PLAYFAIR ------------------------------------------------------------

def get_possible_characters():
    possible = list(string.ascii_lowercase)
    possible.append(' ')
    possible.append('.')
    possible.append(',')
    possible.append('?')
    possible.append('!')
    possible.append('$')
    possible.append(':')
    possible.append('(')
    possible.append(')')
    possible.append('-')

    return possible

def populate_playfair(size, key):
    board = [['a' for row in range(0,size)] for col in range(0,size)]
    possible_chars= get_possible_characters()
    actual_character = 0
    for row in range(0,size):
        for col in range(0,size):
            set = False
            while actual_character < len(key) and not set:
                if key[actual_character] in possible_chars:
                    board[row][col]=key[actual_character]
                    possible_chars.remove(key[actual_character])
                    set = True
                actual_character +=1
            if not set:
                board[row][col]=possible_chars[0]
                possible_chars.remove(possible_chars[0])

    return board

def preproces_playfair(text):
#inserir caracter '$' entre els parell de lletres iguals
    result = text[0]
    for i in range(1,len(text)):
        if text[i]==text[i-1]:
            result+='$'
        result += text[i]

    return result

def postproces_playfair(text):
    result = text[0]
    for i in range(1,len(text)-1):
        if not (text[i]=='$' and text[i-1]==text[i+1]):
            result += text[i]
    result += text[len(text)-1]
    print(text[len(text)-1])
    return result

def get_row_col(board, character, size):
    for row in range(0,size):
        for col in range(0,size):
            if board[row][col] == character:
                return row, col

    return -1, -1
