with open('namelist.txt', 'r') as file:
    #print(list(file))
    lista = {}
    for l in list(file):
        #print(lista[l])
        if l[:-1] in lista:
            lista[l[:-1]] += 1
        else:
            lista[l[:-1]] = 1
    print(lista)
