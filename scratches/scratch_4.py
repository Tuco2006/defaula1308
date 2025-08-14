def teste(*args):
    if len(args) == 0:
        return 0
    total = 0
    for num in args:
        total += num
    return total / len(args)

teste(1,4,5,6)

print(teste(1,4,5,6))