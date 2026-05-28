import numpy as np

# =========================
# 1. CREATE DATASET
# =========================

# 5 students, 3 subjects (Math, Physics, Chemistry)
scores = np.array([
    [80, 75, 90],
    [60, 65, 70],
    [90, 85, 95],
    [50, 55, 60],
    [70, 72, 68]
])

print("SCORES:")
print(scores)

# =========================
# 2. BASIC INFO
# =========================

print("\nSHAPE:", scores.shape)
print("DIMENSIONS:", scores.ndim)

# =========================
# 3. STATISTICS (PER SUBJECT)
# =========================

print("\nMEAN (each subject):", np.mean(scores, axis=0))
print("MEAN (overall):", np.mean(scores))

print("MIN (each subject):", np.min(scores, axis=0))
print("MAX (each subject):", np.max(scores, axis=0))

print("STD (spread):", np.std(scores))

# =========================
# 4. STUDENT TOTAL & AVERAGE
# =========================

student_totals = np.sum(scores, axis=1)
student_avg = np.mean(scores, axis=1)

print("\nTOTAL SCORES PER STUDENT:", student_totals)
print("AVERAGE PER STUDENT:", student_avg)

# =========================
# 5. BEST STUDENT
# =========================

best_student_index = np.argmax(student_totals)
print("\nBEST STUDENT INDEX:", best_student_index)
print("BEST STUDENT TOTAL:", student_totals[best_student_index])

# =========================
# 6. NORMALIZATION (0-1 SCALE)
# =========================

normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

print("\nNORMALIZED DATA:")
print(normalized)

# =========================
# 7. MATRIX OPERATION (BONUS)
# =========================

weights = np.array([0.3, 0.3, 0.4])  # importance of each subject

final_score = scores @ weights

print("\nWEIGHTED FINAL SCORES:")
print(final_score)