def teste(palavra, caractere):
    x = 0
    for letra in palavra:
        if letra == caractere:
            x += 1
    return x

print(teste('arara', 'a'))