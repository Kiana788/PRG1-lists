# Stretch 2: Lists of lists

File: `nested.py`

Optional, and a first look at something covered properly later in the module.

Each item in `register` is itself a list: a name followed by two marks.

## Predict

Three averages, then three more lines. Write them all down.
Ada: 70.0
Grace: 58.0
Alan: 89.5
---
['Ada', 72, 68]
Ada
91

## Run

Execute and compare.

## Investigate

- `row[0]` is a name and `row[1:]` is a list of marks. Why a slice for the marks
  rather than picking them out one at a time? Taking a slice captures all the marks in one go, so the code works regardless of the number of marks after the name; having to select them individually would mean changes to the code for every change in the number of marks

- `register[0]` gives a whole row. `register[0][0]` gives one name. Read the
  second one out loud in words, left to right. register[0][0] spoken: the first row of the register, then the first value of the row, which is the name "Ada".
- What would `register[1][2]` give? Predict, then check. register[1][2] holds the second mark of Grace: 61.
- If a third mark were added to every learner, which lines of this program would
  need changing? That is a good test of whether it was written well. Only the data needs changing, while the loop, the slice, and the average will continue working without any modifications, which indicates good programming.

## Modify

- Print the name of the learner with the highest average.
- Add a fourth learner and confirm nothing else needs changing.
# Learner with the highest average
best = max(register, key=lambda row: sum(row[1:]) / len(row[1:]))
print(best[0])  # Alan

# Fourth learner: add to the data, nothing else changes
register.append(["Margaret", 78, 84])
