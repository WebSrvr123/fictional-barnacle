def bitreverse(n: int):
    f = bin(n).replace("0b","")
    return int("0b"+f[::-1],base=2)
