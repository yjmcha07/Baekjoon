n=int(input())
astart = 100
bstart = 100
for i in range (n):
    a,b = map(int, input(). split())
    if a>b:
        bstart=bstart-a
    if a<b:
        astart=astart-b
print(astart)
print(bstart)
        
