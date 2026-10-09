# Activity 2: Analysing scores

File: `score_analysis.py`

Ten exam results in, a report out: how many passed, the spread, and who needs
help.

## Predict

- How many pass and how many fail? 6 passed (72, 55, 91, 40, 66, 83) and 4 failed (38, 27, 45, 39). Note 40 counts as a pass because the test is >=.
- What is the pass rate? Pass rate: 6/10 = 60%
- What does the final line print, and in what order? Final line prints the failed scores sorted, i.e. [27, 38, 39, 45].
The empty lists have to be there before the loop since the loop uses .append() on them in each iteration. Without the lists, the first time passed.append(score) is called, Python will generate a NameError exception. There must be an entity to use append() on.
A score of 40 will make it into passed. The character that makes the decision is the = sign in >=. A change of that sign to > will push 40 into failed.
sum(), max(), min() and len() are built-in functions that in a single function call do what an accumulation loop does. That is, they traverse the entire list and provide one result. In case that the computation is too complex for just summing, finding the largest or counting, then an accumulation loop is required.
sorted(failed) returns a sorted list, but leaves the original list intact.

## Run

Execute and compare.

## Investigate

- Two empty lists are created before the loop and filled during it. Why do they
  have to exist before the loop starts?
  The empty lists have to be there before the loop since the loop uses .append() on them in each iteration. Without the lists, the first time passed.append(score) is called, Python will generate a NameError exception. There must be an entity to use append() on.
- A score of exactly 40 appears in the data. Which list does it end up in, and
  which character in the code decides that? You have met this question twice
  already this week. A score of 40 will make it into passed. The character that makes the decision is the = sign in >=. A change of that sign to > will push 40 into failed.
- `sum`, `max`, `min` and `len` all take the whole list at once. How is that
  different from the accumulator loops you wrote on Day 3, and when would you
  still need a loop? sum(), max(), min() and len() are built-in functions that in a single function call do what an accumulation loop does. That is, they traverse the entire list and provide one result. In case that the computation is too complex for just summing, finding the largest or counting, then an accumulation loop is required.
- The final line sorts `failed` but the list itself is unchanged afterwards.
  Hold that thought until activity 3. sorted(failed) returns a sorted list, but leaves the original list intact.

## Modify

- Report the number of learners who scored 70 or more, as a distinction band.
# Distinction band: 70 or more
distinctions = [s for s in scores if s >= 70]
print(f"{len(distinctions)} scored 70 or more")
- Print the average of the passing scores only, not of all of them.
# Average of passing scores only
pass_average = sum(passed) / len(passed)
print(f"Average of passing scores: {pass_average:.1f}")

- Change the pass mark to 50 and predict which numbers move before you run it.
# Pass mark of 50: passed becomes 4 (72, 55, 91, 66, 83 -> actually 5: 72,55,91,66,83)
With PASS_MARK = 50: 5 passed (72, 55, 91, 66, 83) and 5 failed (38, 40, 27, 45, 39), pass rate 50%, and Needs support: [27, 38, 39, 40, 45] (40 moves from passed to failed).