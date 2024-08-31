while True:
    a,b,c = map(int, input(). split())
    group=[]
    group.append(a)
    group.append(b)
    group.append(c)
    group.sort()

    if a==b==c==0:
        break
    else:
        if group[0]**2+group[1]**2 == group[2]**2:
            print("right")
        else:
            print("wrong")
   