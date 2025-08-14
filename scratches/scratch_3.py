def teste(*args):
    result = ""
    for i, word in enumerate(args):
        if i > 0:
            result += " "
        result += str(word)
    return result