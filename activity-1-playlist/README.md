# Activity 1: The playlist

File: `playlist.py`

A music queue: songs get added, played, skipped ahead of and pulled out.

## Predict

Write down every line of output before running. There are nine. The last one is
the whole list, so get the order right as well as the contents.
Starting with 3 songs
Levitating
Blinding Lights
Now 5 songs
Now playing: Levitating
4 left in the queue
Next up after this one: Golden Hour
Removed Flowers by request
['As It Was', 'Golden Hour', 'Espresso', 'Blinding Lights']

## Run

Execute it.

## Investigate

- `playlist[0]` and `playlist[-1]` picked out the first and last songs. That is
  the same notation you used on strings yesterday. What does that tell you about
  how Python thinks about both? Both strings and lists can be indexed and sliced because both are sequences. The way that Python handles both types is the same so anything you learned about strings will directly apply to lists as well.
- `pop(0)` did two things at once. Name both. There are two jobs that pop(0) does: it deletes the item that is located at index 0 from the list, and returns the deleted item so that it may be assigned to now_playing.
- `insert(1, "Golden Hour")` put a song at position 1. What happened to the song
  that was already there? The song that already occupied index 1 ("Espresso," after all the pops and appends) got moved down to index 2. Nothing was overwritten; everything in the list starting at index 1 got moved over by one index.
- The `remove` is inside an `if`. What would happen without the `if`, if the song
  were not in the list? Predict first, then try it.
If the if statement wasn't there, remove would raise an error, ValueError: list.remove(x): x not in list, if the song being looked for was not in the list.

## Modify

- Add a song to the end of the queue without using `append`.
# Add a song to the end without append
playlist += ["Golden Hour"]
# or:
playlist = playlist + ["Golden Hour"]
- Play the next two songs in one go, printing both titles.
# Play the next two songs in one go
now_playing = playlist.pop(0)
next_up = playlist.pop(0)
print(f"Now playing: {now_playing}, next up: {next_up}")
- Change the program so removing a song that is not there prints a message
  rather than doing nothing.
# Removing a song that is not there prints a message instead of crashing
def remove_song(playlist, song):
    if song in playlist:
        playlist.remove(song)
    else:
        print(f"{song} is not in the queue")