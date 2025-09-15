# print the sum to n 
# TC is o(n) becz fun run/iterate to n times
# SC is o(n) becz stack once full of n functions and then becomes empty

def fun(n):
    if n==1:
        return 1 
    return n * fun(n-1)

print(fun(5))