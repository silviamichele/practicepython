#https://www.practicepython.org/assets/Training_01.txt
with open('texto_base.txt', 'r') as file:
    topicos = {}
    for l in file:
        diretorios = str(l).split('/')
        if diretorios[2] in topicos:
            topicos[diretorios[2]] += 1
        else:
            topicos[diretorios[2]] = 1
    print(topicos)
