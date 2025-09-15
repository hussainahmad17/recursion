# we reverse an array using reverse function
# array = [12, 34, 56, 67 ,79]
# # print(array.reverse())  modeilfies the array but return nothing
# array.reverse()
# print(array)


# using recursion
# TS and SC is o(n)
# array = [12,45,78,90,21,54,78,23]
# def task(array, l, r):
#     if l>=r:
#         return
#     array[l],array[r] = array[r],array[l]
#     task(array,l+1,r-1)

# task(array,0,7)
# print(array)

# using while loop
array = [12,45,78,90,21,54,78,23]
l=0
r=len(array) - 1
while(l<=r):
    array[l],array[r] = array[r],array[l]
    l+=1
    r-=1
print(array)
