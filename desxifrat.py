

from funcions import *

BOARD_SIZE = 6

def get_inputs():
    inFile = input("Entra el nom del fitxer on hi ha el text xifrat: ")
    outFile = input("Entra el nom de fitxer on es guardarà el resultat de desxifrat: ")
    key = input("Entra la clau amb la que vols desxifrar: ")

    return inFile, outFile, key


def decrypt_playfair(key,text):
    board = populate_playfair(BOARD_SIZE,key)
    to_decypt = text
    result = ""

    for i in range(1,len(to_decypt),2):
        row, col = get_row_col(board,to_decypt[i-1] ,BOARD_SIZE)
        row2, col2 = get_row_col(board, to_decypt[i],BOARD_SIZE)
        to_add = ''
        to_add2 = ''

        #Si les files son iguals, s'agafa el de la respectiva dreta circularment
        if row == row2:
            to_add = board[row][(col -1)% BOARD_SIZE]
            to_add2 = board[row2][(col2 -1)% BOARD_SIZE]
        elif col == col2:
            to_add = board[(row-1)%BOARD_SIZE][col]
            to_add2 = board[(row2-1)%BOARD_SIZE][col2]
        else:
            to_add = board[row][col2]
            to_add2 = board[row2][col]

        result += to_add + to_add2

    result = postproces_playfair(result)

    return result



def decrypt():
    inFile, outFile, key =get_inputs()
    encrypted_text = open(inFile, 'r').read()
    n_rail = len(key)
    to_decrypt = descodificaRailFence(encrypted_text,n_rail)
    print(to_decrypt)
    print(len(to_decrypt))
    decrypted = decrypt_playfair(key,to_decrypt)
    print(decrypted)
    output = open(outFile,"w")
    output.write(decrypted)
    output.close()
    print("Decrytion finalized. Result in {}".format(outFile))
decrypt()
