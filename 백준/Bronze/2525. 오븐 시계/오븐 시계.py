a,b = map(int, input(). split())
c=int(input())
if b+c<60:
    b=b+c
elif b+c==60:
    b=0
    a=a+1
elif b+c>60:
    a=a+(b+c)//60
    b=(b+c)%60
if a>=24:
    a=a%24
print(a,b)
