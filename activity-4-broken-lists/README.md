# Activity 4: Broken lists

File: `broken_lists.py`

Three faults. Nothing crashes, and every output looks like it could be right
until you check it properly.

## Predict

Work out what each call **should** produce:

- Adding "Golden Hour" to a two song queue 
add_song: the queue with Golden Hour added: ['Levitating', 'As It Was', 'Golden Hour']
- Removing both flagged songs, "Espresso" and "Flowers", from a four song list
 remove_flagged: ['Levitating', 'As It Was']
- Backing up a list, then adding to the original
make_backup: a backup that still equals ['Levitating', 'As It Was'] after appending to the original.

## Run

Execute it. All three are wrong.

## Investigate

- `add_song` printed `None`. Activity 3 covered exactly why. What did the author
  assume `append` handed back?
- `remove_flagged` removed "Espresso" but left "Flowers" behind. Trace the loop
  by hand, writing down the list and the current position after each pass. The
  list gets shorter while the loop is walking through it, and something gets
  skipped. Work out which and why.
- `make_backup` looks harmless. After appending to `original`, the backup has
  changed too. What did `backup = playlist` actually copy?

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
#	What you saw	What was wrong	How you fixed it
1	| add_song printed None and the queue lost its songs | playlist = playlist.append(song) replaces the list with append's return value, which is None	|Remove the assignment: call playlist.append(song) then return playlist
2	|remove_flagged removed "Espresso" but left "Flowers"|	Removing items while looping over the list shifts everything left, so the item after a removed one is skipped |	Loop over a copy (for song in playlist[:]) or build a new list of songs to keep
3	|The backup changed when the original changed |	backup = playlist copies the reference, not the list, so both names point at the same list | backup = playlist.copy() (or list(playlist))

## Modify

Fix all three. You should get a three song queue, a list with both flagged songs
gone, and a backup that does not change when the original does.
FLAGGED = ["Espresso", "Flowers"]


def add_song(playlist, song):
    playlist.append(song)
    return playlist


def remove_flagged(playlist):
    return [song for song in playlist if song not in FLAGGED]


def make_backup(playlist):
    backup = playlist.copy()
    return backup


queue = add_song(["Levitating", "As It Was"], "Golden Hour")
print(queue)  # ['Levitating', 'As It Was', 'Golden Hour']

mixed = ["Levitating", "Espresso", "Flowers", "As It Was"]
print(remove_flagged(mixed))  # ['Levitating', 'As It Was']

original = ["Levitating", "As It Was"]
saved = make_backup(original)
original.append("Golden Hour")
print(saved)  # ['Levitating', 'As It Was']
Trace of fault 2, for the log: list is ["Levitating", "Espresso", "Flowers", "As It Was"]. Position 0: keep. Position 1: "Espresso" flagged, removed, list becomes ["Levitating", "Flowers", "As It Was"] and the loop index moves to 2. Position 2 is now "As It Was", so "Flowers" at position 1 never gets looked at and survives

> The second fault is the nastiest thing in this module so far. Removing items
> from a list while looping over it is legal, runs without complaint, and
> silently skips things. The fix is to loop over a copy, or to build a new list
> of what you want to keep.
