import random
def sorteador(num):
    numeros = []
    for x in range(num):
        #numeros.append(int(random.random() * 100))
        numeros.append(int(random.randint(0, 10)))
    return numeros
numeros = [set(sorteador(int(x))) for x in input('Digite 2 números separados por virgula: (ex.: 2, 3) ').split(',')]
print(numeros[0])
print(numeros[1])
print(numeros[0] ^ numeros[1])
