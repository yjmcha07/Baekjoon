n,m = map(int, input(). split())
a=[]
d=[]
for i in range (n):
    b= list(map(int, input().split()))
    a.append(b)
for t in range (n):
    c=list(map(int, input(). split()))
    d.append(c)
for p in range (len(a)):
    for k in range (len(a[p])):
        print(a[p][k]+d[p][k], end=" ")
    print()