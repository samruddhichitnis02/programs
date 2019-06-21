n=int(input('Enter an Integer number only-'))
def to_bin(n):
    x=bin(n)
    print(x)
    r =((x & 0x0F) << 4 | (x & 0xF0) >> 4)
    print(r)

to_bin(n)
