a,b= map(int, input(). split())
basket=[]
for i in range(a):
    basket.append(0)
for i in range(b):
    x,y,z = map(int, input(). split())
    for n in range (x-1,y):
        basket[n]=z
print(*basket)

        
    
        
        
