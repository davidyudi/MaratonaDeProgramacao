t = int(input())
q1, l1 = map(int, input().split())
q2, l2 = map(int, input().split())
q3, l3 = map(int, input().split())
maior = 0
for a in range(t//q1+1):
    for b in range(t//q2+1):
        usado = (q1*a) + (q2*b)
        if usado <= t:
            sobra = t - usado
            c = sobra//q3
            lucro = (a*l1)+(b*l2)+(c*l3)
        if lucro > maior:
            maior = lucro
print(maior)