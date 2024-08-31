matrix=[]
for i in range(9):
    a=list(map(int,input(). split()))
    matrix.append(a)
max_number=0
max_row=0
max_col=0
for row in range(9):
    for col in range(9):
        if max_number<=matrix[row][col]:
            max_number=matrix[row][col]
            max_row=row+1
            max_col=col+1
print(max_number)
print(max_row , max_col)
