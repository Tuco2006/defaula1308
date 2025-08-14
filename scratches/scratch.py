def pi(x):
    pii=0
    y=0
    for i in range(x):
        if i%2 == 0:
            pii += 1/(1+y)
        else:
            pii -=1/(1+y)

        y += 2

    pii*=4
    return pii

calc = int(input("Digite um número para calcular PI:"))

print(pi(calc))