import datetime

year = int(str(datetime.datetime.today()).split('-')[0])
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

print(f'{nome}, você completará 100 anos em: { year + (100-idade) }')
