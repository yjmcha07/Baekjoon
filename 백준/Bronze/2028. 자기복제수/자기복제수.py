a=int(input())
for i in range (a):
    b=int(input())
    c=(b**2)
    d=len(str(b))
    if str(c)[-d : ] == str(b):
        print("YES")
    else:
        print("NO")
