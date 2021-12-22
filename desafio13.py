i = 0
j = 1
#0, 1, 1, 2, 3, 5, 8, 13,
while i < 100:
    print(f'{i} {j}', end=' ')
    i += j
    j += i
