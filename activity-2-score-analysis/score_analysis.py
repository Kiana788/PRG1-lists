PASS_MARK = 40

scores = [72, 38, 55, 91, 40, 27, 66, 83, 45, 39]

passed = []
failed = []

for score in scores:
    if score >= PASS_MARK:
        passed.append(score)
    else:
        failed.append(score)

print(f"{len(scores)} learners sat the paper")
print(f"{len(passed)} passed, {len(failed)} did not")

average = sum(scores) / len(scores)
print(f"Average: {average:.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")

pass_rate = len(passed) / len(scores) * 100
print(f"Pass rate: {pass_rate:.0f}%")

print(f"Needs support: {sorted(failed)}")

# Distinction band: 70 or more
distinctions = [s for s in scores if s >= 70]
print(f"{len(distinctions)} scored 70 or more")

# Average of passing scores only
pass_average = sum(passed) / len(passed)
print(f"Average of passing scores: {pass_average:.1f}")

# Pass mark of 50: passed becomes 4 (72, 55, 91, 66, 83 -> actually 5: 72,55,91,66,83)
