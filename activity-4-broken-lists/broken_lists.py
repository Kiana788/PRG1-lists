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
