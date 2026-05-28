import numpy as np

# =========================
# CREATE ARRAYS
# =========================

even = np.array([2, 4, 6, 8, 10])

odd = np.array([
    [1, 3, 5],
    [7, 9, 11]
])

print("EVEN ARRAY:")
print(even)

print("\nODD ARRAY:")
print(odd)

# =========================
# SHAPE & DIMENSIONS
# =========================

print("\n==============")
print("SHAPES:")
print(even.shape)
print(odd.shape)

print("\n==============")
print("DIMENSIONS:")
print(even.ndim)
print(odd.ndim)

# =========================
# 1D ARRAY OPERATIONS
# =========================

print("\n==============")
print("1D INDEXING & SLICING")

print("First element:", even[0])
print("Last element:", even[-1])
print("Middle slice:", even[1:-1])
print("From index 2 to end:", even[2:])

# =========================
# 2D ARRAY INDEXING
# =========================

print("\n==============")
print("2D INDEXING")

print("Element 9:", odd[1, 1])
print("Element 5:", odd[0, 2])

print("First row:", odd[0])
print("Second row:", odd[1])

print("Second column:", odd[:, 1])

# =========================
# MATH OPERATIONS
# =========================

print("\n==============")
print("MATH OPERATIONS")

print("Add 10:", even + 10)
print("Multiply by 2:", even * 2)
print("Subtract 3:", even - 3)

# =========================
# BONUS CHALLENGE
# =========================

print("\n==============")
print("BONUS CHALLENGE")

arr = np.array([1, 2, 3, 4, 5, 6])

first_half = arr[:3]
second_half = arr[3:]

print("First half:", first_half)
print("Second half:", second_half)

print("First half * 2:", first_half * 2)
print("Second half + 5:", second_half + 5)