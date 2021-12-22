def removeDuplicate(lista):
    n_l = []
    for c in lista:
        if c not in n_l:
            n_l.append(c)
    return n_l

def removeDuplicateWithSet(lista):
    return list(set(lista))

print(removeDuplicate([1, 2, 3, 4, 5, 4, 5, 1, 90]))
print(removeDuplicateWithSet([1, 2, 3, 4, 5, 4, 5, 1, 90]))
