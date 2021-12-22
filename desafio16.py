import random

lista = [
    'paz','love','deus','vida','123pass','mais','fiel','mae','pai', 'feliz', 'jesus'
]
# alfabeto = 'ABCDEFGHIJKLMOPQRSTUVWZYZ'
# alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
# numeros = '0123456789'
# caracters_especiais = '!@#$%&*()-+.,;?{[}]^><:'
caracters = '<:TUVW#$%&CDEwxABI}]^>yz045678lmq,;?{MOPQn12FGH*(ghijku)-+ZJKL@opRSrst[YZa.v39!bcdef'

def gerarSenha(qtd_cadacters):
    new_p = ''
    for x in range(0, qtd_cadacters):
        caracter = random.randint(0, len(caracters)-1)
        new_p += caracters[caracter]
    return new_p

def gerarSenhaFacil(qtd_words):
    new_p = ''
    c = 0
    while c<qtd_words:
        word = random.randint(0, len(lista)-1)
        new_p += lista[word]
        c+=1
    return new_p

qtd_caracters = int(input('Quantidade de caracters: '))
if qtd_caracters<8:
    print('é recomendado que uma senha possua mais do que 8 caracters')
else:
    print(gerarSenha(qtd_caracters))
