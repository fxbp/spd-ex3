## Metode de xifratge substitutiu: PlayFair (poligrafic per parells de lletres)
## Metode de transpocicional: Rail Fence

## Xifrat RailFence: Utilitzant la mida de la clau com a nombre de rails, es transposa el text entrant.
## Xifrat PlayFair: un cop s'ha xifrat el text en clar amb RailFence es xifra amb playFair:
##                  - La mida de la taula es de 6x6 (s'eviten collisions de lletres)
##                  - Es contemplen els simbols ' ', '.', ',', '?','!','$',':','(',')','-' per completar la taula

## Alfabet en els 2 casos sera l'angles tant d'entrada com de sortida
## l'alfabet en minuscula: a-z
## Es contemplen els simbols ' ', '.', ',', '?','!','$',':','(',')','-'
## com que la taula es de 36 posicions la llargada maxima efectiva de la clau es de 36, pero pot ser mers llarga.


from funcions import *

BOARD_SIZE = 6

def get_inputs():
    inFile = input("Entra el nom del fitxer on hi ha el text clar: ")
    outFile = input("Entra el nom de fitxer on es guardarà el text xifrat: ")
    key = input("Entra la clau amb la que vols xifrar: ")

    return inFile, outFile, key


def get_row_col(board, character, size):
    for row in range(0,size):
        for col in range(0,size):
            if board[row][col] == character:
                return row, col

    return -1, -1

def encrypt_playfair(key,text):
    board = populate_playfair(BOARD_SIZE,key)
    to_encrypt = preproces_playfair(text)
    result = ""
    if len(to_encrypt)%2 != 0:
        to_encrypt += ' '
    print(board)
    print(key)
    for i in range(0,len(to_encrypt),2):
        row, col = get_row_col(board,to_encrypt[i] ,BOARD_SIZE)
        row2, col2 = get_row_col(board, to_encrypt[i+1],BOARD_SIZE)
        to_add = ''
        to_add2 = ''
        print(row,col)
        print(row2,col2)
        #Si les files son iguals, s'agafa el de la respectiva dreta circularment
        if row == row2:
            to_add = board[(row+1)%BOARD_SIZE][col]
            to_add2 = board[(row2+1)%BOARD_SIZE][col2]
        elif col == col2:
            to_add = board[row][(col +1)% BOARD_SIZE]
            to_add2 = board[row2][(col2 +1)% BOARD_SIZE]
        else:
            to_add = board[row][col2]
            to_add2 = board[row2][col]

        result += to_add + to_add2


    return result

print(encrypt_playfair("ab","abc"))
