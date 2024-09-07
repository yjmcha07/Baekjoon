a = int(input())
for i in range (a):
    b=int(input())
    if b<3:
        for i in range(b):
            print("#"*b)
        print()
    
    else:
        print('#'*b)
        for i in range(b-2):
            print(('#'+('J'*(b-2))+'#'))
        print('#'*b)
        print()
