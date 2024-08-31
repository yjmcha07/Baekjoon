x=int(input())
n=int(input())
sum=0
while n>0:
    a,b = map(int, input(). split())
    c=a*b
    sum=sum+c
    n=n-1
if sum==x:
    print("Yes")
elif sum!=x:
    print("No")