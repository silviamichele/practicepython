#lista padrão definida pel@ criador dos desafios
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input('Digite um número:  '))
print(f'números da lista {a} que são menores que {number}: {[c for c in a if c < number]}')
