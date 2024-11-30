import numpy as np

arr = np.array([[1, 'i', 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:])
print(type(arr))
print(arr.dtype)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[::2])

def func(ones,two=None):
    print(ones,two)

one=1
two=2 
# func(one,two)

print("-------------------")
print(max(3,4) - min(3,4))