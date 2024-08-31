a,b=map(int, input(). split())
basket=[]
for i in range (1,a+1):
    basket.append(i)
for i in range (b):
    x,y = map(int, input(). split())
    temp=basket[x-1]
    basket[x-1]=basket[y-1]
    basket[y-1]=temp
print(*basket)