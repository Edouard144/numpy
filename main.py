import numpy as np

a = np.array([1,2,3])
b = (a+2)
c = [1,2,3,4]

print(c)
print(a)
print(b)
print(a + b)

# creating a 2D array
d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print()
print()
print(".")

#printing a 3D
print(d)

# TOview the shape of your table
print(d.shape)
print(d.ndim)