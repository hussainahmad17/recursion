# TC is o(2^n) because at every step, two functions are running
# SC is o(1) as there are the "l" and "r" just, can be ignored
def task(n):
    if n == 0 or n == 1:
        return n
    return task(n-1) + task(n-2)
print(task(9))