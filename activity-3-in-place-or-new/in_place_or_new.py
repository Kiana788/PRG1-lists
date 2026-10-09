playlist = ["Levitating", "As It Was", "Blinding Lights"]

result = playlist.append("Flowers")
print(result)
print(playlist)

print("---")

alphabetical = sorted(playlist)
print(alphabetical)
print(playlist)

print("---")

result = playlist.sort()
print(result)
print(playlist)

# Third block rewritten: original preserved, sorted copy in a new variable
alphabetical = sorted(playlist)
print(alphabetical)
print(playlist)

# Reverse sort without changing playlist
reverse_alpha = sorted(playlist, reverse=True)
print(reverse_alpha)
print(playlist)
