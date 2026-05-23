v, n = map(int, input().split())
vdd = False
lista = []
for c in range(n):
    vvv = int(input())
    lista.append(vvv)

for c1 in range(n):
    for c2 in range(c1+1, n):
        for c3 in range(c2+1, n):
            if v + lista[c1] + lista[c2] + lista[c3] == 200:
                vdd = True
if vdd:
    print("fretegratis")
else:
    print("fretepago")