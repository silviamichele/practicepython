with open('numeros_primos.txt', 'r') as file:
    numeros_primos = [int(x) for x in file]
with open('numeros_felizes.txt', 'r') as filehappy:
    numeros_felizes = [int(x) for x in filehappy]

numeros_s = list(set(numeros_primos) & set(numeros_felizes))
print(sorted(numeros_s))
