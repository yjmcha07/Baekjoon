m = int(input())
ball=1

for i in range (m):
    a,b = map(int, input(). split())
    if a==ball:
        ball=b
    elif b==ball:
        ball=a

print(ball)
