while True:
    a,b,c =input(). split()
    b=int(b)
    c=int(c)
    if a=='#' and b==c==0:
        break
    elif b>17 or c>=80:
        print(str(a)+" Senior")
    else:
        print(str(a)+" Junior")
    
