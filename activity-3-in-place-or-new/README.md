# Activity 3: In place, or a new one?

File: `in_place_or_new.py`

The most important thing to know about lists, and the thing that makes them
behave unlike the strings you met yesterday.

## Predict

Three blocks separated by dashes. Eight lines of output in total. Write them all
down first, and be careful with the ones that print `result`.
None
['Levitating', 'As It Was', 'Flowers', 'Espresso']
---
['As It Was', 'Blinding Lights', 'Espresso', 'Levitating', 'Flowers']
['Levitating', 'As It Was', 'Flowers', 'Espresso']
---
None
['As It Was', 'Blinding Lights', 'Espresso', 'Levitating', 'Flowers']


## Run

Execute and compare.

## Investigate

- `playlist.append("Flowers")` was assigned to `result`, and `result` printed as
  `None`. Yet the playlist did change. What does that tell you about what
  `append` hands back?
The method append modifies the list and returns nothing; nothing in Python is None, which means that assigning the return value of append to result discards it, as the author assumed that append would return the list after modifying it, which is incorrect.
- `sorted(playlist)` gave a sorted list **and** left the original alone. Compare
  that with `.sort()` in the third block, which did the opposite. Write the
  difference down in one sentence each.
  On the other hand, sorted(playlist) will not modify the list at all but instead will return a new, sorted list, while the method sort() will modify the original list and return None.
- Yesterday you learned that a string method never changes the string it was
  called on. Lists are the other way round: a list method usually changes the
  list and hands back nothing. Why does it matter that these two behave in
  opposite ways?
  This is important, because while the two methods have similar syntax and names, their behavior is completely opposite, so the habit of result = playlist.append(x) from strings will quietly destroy the list.

## Modify

- Rewrite the third block so the sorted playlist ends up in a new variable and
  the original order is preserved.
- Make `alphabetical` sort in reverse order without changing `playlist`.
# Third block rewritten: original preserved, sorted copy in a new variable
alphabetical = sorted(playlist)
print(alphabetical)
print(playlist)

# Reverse sort without changing playlist
reverse_alpha = sorted(playlist, reverse=True)
print(reverse_alpha)
print(playlist)


> `result = playlist.append(song)` is a fault almost everyone writes once. It
> quietly replaces your playlist with nothing. You will meet it again in about
> ten minutes.
