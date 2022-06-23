def compute_parity(n: int):
    f = bin(n).replace("0b", "")
    a = {"1":0,"0":0}
    for i in f:
        if i == "1":
            a[i] += 1
        else:
            a[i] += 1
    if a["1"]%2 == 0:
        return 0
    else:
        return 1
