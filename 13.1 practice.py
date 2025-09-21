A = 1

while A <= 9:
    B = 1
    while B <= A:
        C = A * B
        print(f'{A}*{B}={C}',end = '\t')
        B += 1
    print()
    A += 1