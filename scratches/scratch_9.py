def produto_escalar(vetor1, vetor2):
    x = 0
    for i in range(len(vetor1)):
        x += vetor1[i] * vetor2[i]

    return x
print(produto_escalar([1, 2, 3], [4, 5, 6]))