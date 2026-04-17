for n in range(100):
    b=bin(n)[2:]
    if b.count('1')%2==0:
        b=b+'00'
    else:
        b=b+'10'
    r=int(b,2)
    if r>77:
        print(n)
        break