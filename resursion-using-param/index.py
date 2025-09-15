def recur(x,n):
    for i in range(1,n+1):
        print(x)
recur(2,3)

# same thing with recursion

def recur2(x,n):
    if n==0:
        return
    print(x)
    recur2(x,n-1)

recur2(15,4)