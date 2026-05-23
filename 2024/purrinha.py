qj = int(input())
nomes = []
pontos = []
for c in range(qj):
    nomes.append(input())
    pontos.append(0)
nr = int(input())
for c in range(nr):
    palitos = list(map(int, input().split()))
    palpites = list(map(int, input().split()))
    for i in range(qj):
        if palpites[i] == sum(palitos):
            pontos[i] += 1
if pontos.count(max(pontos)) > 1:
    print("EMPATE")
else:
    i = pontos.index(max(pontos))
    print(f"{nomes[i]} GANHOU")
