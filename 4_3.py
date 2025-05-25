#a*b mod m = 1 => a*b % m = 1
try:
    b = 1
    a, m = input().split(" ")
    a = int(a)
    m = int(m)

    while (a*b) % m != 1 and a*b < m:
        b += 1
    print(b)
except:
    print()