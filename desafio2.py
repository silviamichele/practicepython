numero = int(input('Digite um número: '))
if(numero % 2 == 0):
    print('par', end=' ')
    if(numero % 4 == 0):
        print('e multiplo de 4')
else:
    print('impar')
