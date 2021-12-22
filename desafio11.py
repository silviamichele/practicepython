def primo(num):
    divisores = [x for x in range(1, num+1) if num % x == 0]
    if len(divisores) == 2:
        return 'primo'
    else:
        return 'não é primo'

numero = int(input('digite um número: '))
print(primo(numero))
