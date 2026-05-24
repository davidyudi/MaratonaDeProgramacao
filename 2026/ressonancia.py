import math
n = int(input())
matriz = []
distancia = []
linha = []
for i in range(n):
    x, y = map(int, input().split())
    linha.append(x)
    linha.append(y)
    matriz.append(linha[:])
    linha.clear()
    print(f"i = {i}")
print(matriz)
print(linha)