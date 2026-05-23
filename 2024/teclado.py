n = int(input())
for c in range(n):
    p = list(input())
    for l in range(len(p)):
        if p[l] in "ABC":
            p[l] = "2"
        elif p[l] in "DEF":
            p[l] = "3"
        elif p[l] in "GHI":
            p[l] = "4"
        elif p[l] in "JKL":
            p[l] = "5"
        elif p[l] in "MNO":
            p[l] = "6"
        elif p[l] in "PQRS":
            p[l] = "7"
        elif p[l] in "TUV":
            p[l] = "8"
        elif p[l] in "WXYZ":
            p[l] = "9"
    print("".join(p))
