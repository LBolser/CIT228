print("\n<<<<< 8-7 >>>>>")
def make_album(artist, albumName, tracks = None):

    album = {}
    album["Artist"] = artist.title()
    album["Album Name"] = albumName.title()
    if tracks:
        album["Number of Tracks"] = tracks
    return album

print(make_album("Disturbed","Ten Thousand Fists"))
print(make_album("Deviations Project", "Ivory Bow", 17))
print(make_album("The Brian Setzer Orchestra", "The Dirty Boogie", 13))

print("\n<<<<< 8-8 >>>>>") 
numToEnter = int(input("How many albums are you entering?"))
counter = 0
while counter < numToEnter:
    artist = input("Artist: ")
    albumName = input("Album: ")
    tracks = int(input("Number of Tracks: "))
    print(make_album(artist,albumName,tracks))


