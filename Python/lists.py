playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]
print(f"This is my playlist: {playlist}")

print(playlist[0])
print(playlist[-1])
print(playlist[1:4])

playlist[1] = "Song 2"
print(playlist)

playlist.append("Song F")
print(playlist)

playlist.insert(2, "Song D")
print(playlist)

playlist_2 = ["Song X", "Song Y"]
playlist.extend(playlist_2)
print(playlist)

playlist.remove("Song X")
print(playlist)

print(playlist.pop(-1))

playlist.sort()

print(playlist.reverse())

print(len(playlist))

playlist.count("Song D")

playlist.index("Song 2")