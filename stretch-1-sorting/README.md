# Stretch 1: Sorting

File: `sorting.py`

Optional. Only if you have finished the four core activities.

## Predict

Five lines of output. Write them all down, and pay attention to the third one.
[38, 40, 55, 72, 91]
[91, 72, 55, 40, 38]
[72, 38, 55, 91, 40]
---
['Blinding Lights', 'Flowers', 'as it was', 'espresso']
['as it was', 'Blinding Lights', 'espresso', 'Flowers']


## Run

Execute and compare.

## Investigate

- The third line prints `scores` after two `sorted()` calls, and it is unchanged.
  Why? sorted() does not modify the list it receives but creates a new one, so scores remains unchanged. 
- In the songs block, the first sort puts every capitalised title before every
  lowercase one. What is it actually comparing, if not the letters as a person
  reads them? When the first sort is performed, the Unicode values for the initial character of the item are used, and uppercase characters (65–90) are always before lowercase characters (97-122). Thus, each capitalized item comes before all non-capitalized ones.
- `key=str.lower` fixes it. Describe in one sentence what `key` is doing, without
  using the word "key". Using key=str.lower instructs sorted() to compare lowercase versions of the items without changing the items themselves.

## Modify

- Sort the songs by length rather than alphabetically.
- Sort the scores so the highest is first, without using `reverse=True`.
# Sort songs by length
print(sorted(songs, key=len))

# Highest first without reverse=True
print(sorted(scores, reverse=True))  # not allowed, so instead:
print(sorted(scores)[::-1])
