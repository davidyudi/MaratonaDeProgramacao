a = list(input().split())
a.remove(min(a))
a.remove(max(a))
print(a[0])
