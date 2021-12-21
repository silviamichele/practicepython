number = int(input('Digite um número: '))
divisores = [x for x in range(1, number+1) if number % x == 0]
print(f"{number} é divisivel por: {divisores}")
