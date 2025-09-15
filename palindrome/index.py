# name = "nitin"
# l=0
# r=len(name) - 1
# while l<=r:
#     if l == r:
#         return True
#     return False
 


# TC is o(n/2) == o(n), and SC is o(1)
def is_palindrome(name):
    l = 0
    r = len(name) - 1
    while l <= r:
        if name[l] != name[r]:
            return False
        l += 1
        r -= 1
    return True

name = "niwtien"
print(is_palindrome(name))

