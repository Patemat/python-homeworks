def ord_in_ascii(n1):
    n=n1.encode('ASCII')
    return ord(n1)
assert(ord_in_ascii('A')) == 65
assert(ord_in_ascii('B')) == 66
assert(ord_in_ascii('C')) == 67
assert(ord_in_ascii('Z')) == 90
assert(ord_in_ascii('a')) == 97
assert(ord_in_ascii('z')) == 122
