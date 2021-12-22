import random
tentativas = 0
numero = random.randint(1, 9)
while True:
    print('press 0 to exit')
    num = int(input('digite um número: '))
    if num == 0:
        break
    elif num == numero:
        print('\n'*50)
        print('acertouuuuu')
        print(f'você tentou {tentativas}x')
        numero = random.randint(1, 9)
    elif num > numero:
        print(f'{num} é maior que o número sorteado')
        tentativas += 1
    else:
        print(f'{num} é menor que o número sorteado')
        tentativas += 1
