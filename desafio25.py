import random
min, max, tentativas = 0,100, 0

print('Pense em um número...')
#incluir timer 20s
while True:
    num_s = random.randint(min, max)
    print(f'Npumero sorteado: {num_s}\nDigite: \n0. se o número sorteado for menor que o número que você escolheu\n.1. se o número sorteado for equivalente ao número que você escolheu\n..2. se o número sorteado for maior que o número que você escolheu\n...qualquer outro número para sair')
    op = int(input())
    if op == 2:
        #print(min, max)
        max = num_s + 1
        tentativas += 1
    elif op == 0:
        min = num_s - 1
        #print(min, max)
        tentativas += 1
    elif op == 1:
        print('aêeeeeeeeee')
        print('tentativas: ',tentativas)
        break
    else:
        print('foi bom jogar com você')
        break
