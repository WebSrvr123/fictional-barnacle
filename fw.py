# find weight
def fw(n: int):
    f = bin(n).replace("0b","")
    x = 0
    for i in f:
        if i == "1":
            x += 1
    return x
