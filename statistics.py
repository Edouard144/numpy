import numpy as np

a = np.array([1,2,3,45,10])

print(np.mean(a))

print(np.median(a))

print(np.min(a))

print(np.max(a))

print(np.std(a))

print(np.var(a))

print()
print()

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.mean(b))
print(np.mean(b, axis=0))  # column-wise
print(np.mean(b, axis=1))  # row-wise