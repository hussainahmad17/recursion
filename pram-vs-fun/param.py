# print the sum from 1 to n using parameterized recursion
def task(sum, i, n):
    if i>n:
        print(sum)
        return
    task(sum+i,i+1,n)

task(0,1,4)         