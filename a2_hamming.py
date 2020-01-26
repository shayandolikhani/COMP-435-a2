def hammingdistance(hex1, hex2):
    a = str(bin(int(hex1, 16))[2:])
    b = str(bin(int(hex2, 16))[2:])
    i = 0
    ctr = 0
    if len(a) > len(b):
        b = "{:0>{s}}".format(b, s=len(a))
    elif len(b) > len(a):
        a = "{:0>{s}}".format(a, s=len(b))

    while i < len(a):
        if a[i] != b[i]:
            ctr += 1
        i += 1
    return ctr