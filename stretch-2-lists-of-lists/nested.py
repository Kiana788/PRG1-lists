register = [
    ["Ada", 72, 68],
    ["Grace", 55, 61],
    ["Alan", 91, 88],
]

for row in register:
    name = row[0]
    marks = row[1:]
    average = sum(marks) / len(marks)
    print(f"{name}: {average:.1f}")

print("---")

print(register[0])
print(register[0][0])
print(register[2][1])
# Learner with the highest average
best = max(register, key=lambda row: sum(row[1:]) / len(row[1:]))
print(best[0])  # Alan

# Fourth learner: add to the data, nothing else changes
register.append(["Margaret", 78, 84])
