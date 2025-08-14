def teste(palavra):
    total_vogais = 0
    total_consoantes = 0
    for caractere in palavra:
        if caractere == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
                total_vogais += 1
        else:
                total_consoantes += 1

    return total_vogais, total_consoantes