## Metode de xifratge substitutiu: PlayFair (poligrafic per parells de lletres)
## Metode de transpocicional: Rail Fence

## Xifrat RailFence: Utilitzant la mida de la clau com a nombre de rails es transposa el text entrant.
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



def encrypt_playfair(key,text):
    board = populate_playfair(BOARD_SIZE,key)
    to_encrypt = preproces_playfair(text)
    result = ""
    print(board)
    possible_chars= get_possible_characters()

    i = 0
    while i<len(to_encrypt)-1:
        if not to_encrypt[i] in possible_chars:
            result+=to_encrypt[i]
            i+=1
        elif not to_encrypt[i+1] in possible_chars:
            result+= to_encrypt[i] + to_encrypt[i+1]
            i+=2
        else:
            row, col = get_row_col(board,to_encrypt[i] ,BOARD_SIZE)
            row2, col2 = get_row_col(board, to_encrypt[i+1],BOARD_SIZE)
            to_add = ''
            to_add2 = ''
            #Si les files son iguals, s'agafa el de la respectiva dreta circularment
            if row == row2:
                to_add = board[row][(col +1)% BOARD_SIZE]
                to_add2 = board[row2][(col2 +1)% BOARD_SIZE]
            elif col == col2:
                # si les columnes son iguals, s'agafa el de abaix respectivament circularment
                to_add = board[(row+1)%BOARD_SIZE][col]
                to_add2 = board[(row2+1)%BOARD_SIZE][col2]
            else:
                # altrament s'agafa el de la diagonal oposada
                to_add = board[row2][col]
                to_add2 = board[row][col2]

            i+=2
            result += to_add + to_add2

    return result

def encrypt():
    inFile, outFile, key = get_inputs()
    plain_text = open(inFile, 'r').read()
    n_rail =  len(key)
    encrypted_text = encrypt_playfair(key, plain_text.lower())
    #print(encrypted_text)
    transposed_text = codificaRailFence(encrypted_text,n_rail)

    #print(transposed_text)
    output = open(outFile,"w")
    output.write(transposed_text)
    #output.write(encrypted_text)
    output.close()

    print("Encryption finalized. Result in {}".format(outFile))
encrypt()
