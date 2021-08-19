import sys

def bolha(indice):
    n = len(indice)
    for i in range(n):
        for j in range(0, n-i-1):
            if indice[j] > indice[j+1]:
                swap = indice[j]
                indice[j] = indice[j+1]
                indice[j+1] = swap
    return indice

if __name__=='__main__':

    indice = [4,2,18,6,14,10,12,8,16,0,23]
    print("Indice ordenado: ")
    print(bolha(indice))