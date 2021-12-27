#no lugar errado é um "touro", e no lugar certo é bull
'''
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
'''
import random
sorted = str(random.randint(999, 9999))
num = input('Número: ')
r = len([num[x] for x, y in enumerate(sorted) if sorted[x] == num[x]])
d = len([x for x in num if x in sorted])
#print(r)
#print(d)
print(f'{d-r} cow(s), {r} bull(s)')
print(sorted)
