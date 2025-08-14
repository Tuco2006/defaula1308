def teste(*args):
    maior = args[0]
    menor = args[0]

    for i in args:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

    return maior, menor

print(teste(5,7))