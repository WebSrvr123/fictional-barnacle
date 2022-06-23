import fw
# fw.fw = find weight
def ciwsw(n: int, max_difference=5, FORCE_max_difference=False):
    diff = max_difference
    weight = fw.fw(n)
    for i in range(n - diff, n + diff):
        if fw.fw(i) == weight:
            if i == n:
                pass
            return i
        if FORCE_max_difference:
            return False
        diff += 1



