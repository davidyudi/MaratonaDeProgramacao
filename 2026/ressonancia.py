import math
n = int(input())
matriz = []
distancia = []
linha = []
for c in range(n):
    x, y = map(float, input().split())
    linha.append(x)
    linha.append(y)
    matriz.append(linha[:])
    linha.clear()
for i in range(len(matriz)):
    for j in range(len(matriz) - i):
        d = math.sqrt(pow((matriz[i][0] - matriz[j][0]), 2)+pow((matriz[i][1]-matriz[j][1]),2))
        if d != 0 and d not in distancia:
            distancia.append(d)
print(f"{min(distancia):.4f}")