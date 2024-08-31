H,M=map(int, input(). split())
if 45<= M <= 59:
    M=M-45
else:
    if H==0:
        H=23
        M=M+15
    else:
        H=H-1
        M=M+15
print(H,M)