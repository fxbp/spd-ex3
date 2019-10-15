from funcions import *
import matplotlib.pyplot as plt


def frequence(text):
    dict = {}
    possible_chars= get_possible_characters()
    for i in range(0,len(possible_chars)):
        dict[possible_chars[i]] =0
    for k in range(len(text)):
        if text[k] in possible_chars:
            dict[text[k]] +=1;

    return dict


def calculateIndexC():
    file = input("Entra el fitxer al que vols calcular l'index de coincidencia: ")
    text = open(file, 'r').read()
    frequence_table = frequence(text)
    keys=list()
    freq=list()
    totalFreq=0
    lenText=0
    for key in frequence_table:
        keys.append(key)
        freq.append(frequence_table[key])
        totalFreq += frequence_table[key]*(frequence_table[key]-1)
        lenText+=frequence_table[key]

    ic= len(frequence_table)*totalFreq/(lenText*(lenText-1))

    print("L'index de coincidencia del text xifrat és: ", ic)

    plt.plot(keys,freq,'ro')
    plt.xlabel("Caracters")
    plt.ylabel("frequencia")
    plt.show()

calculateIndexC()
