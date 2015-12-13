def singleNumber(self, A):
    r = 0
    for i in A:
        r ^= i
    return r