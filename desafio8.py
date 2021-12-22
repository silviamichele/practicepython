pares = {
    'pedra':'tesoura',
    'papel':'pedra',
    'tesoura':'papel'
}
def clear():
    print("\n" * 130)
    print('press 1 nos 2 campos para sair')

while True:
    j1 = input('Jogador 1: ')
    clear()
    j2 = input('Jogador 2: ')
    clear()
    if j1 == '1' or j2 == '1':
        break
    elif pares[j1] == j2:
        print('joagdor 1 ganhou')
    elif pares[j2] == j1:
        print('jogador 2 ganhou')
    else:
        print('empate!!!')
