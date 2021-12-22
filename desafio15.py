def reverseSentence(sentence):
    n_s = sentence.split(' ')[::-1]
    return ' '.join(n_s)
    
d = input('Digite uma frase: ')
print(reverseSentence(d))
