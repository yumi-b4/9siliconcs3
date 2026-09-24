## Class Relationships: Association and Multiplicity

## Previous Work 

 [q1/classObjectUML.md](q1/classObjectULM.md)
 [q1/classAttributesMethods.md](q1/classAttributesMethods.md)

## Existing Class
Class: Playlist 
Description: A playlist is a collection of songs organized for a specififc mood or ppurpose. 

## New Related Class
Class: Song 
Description: A song represents a piece of music that can be added in a paylist.

## Association
Relationship: Playlists contains songs.
Explanation: A playlist has a song objects that are added to it. The playlist is able to manage and store songs that belongs to it. 

## Multiplicity
Multiplicity: 1 : 0..*
Explanation: A playlist can contain zero or more songs, which fits the system since a playlist can have different songs, and the number of songs can vary depending on the playlist. 

## UML Class Relationship Diagram 
![cR_UMLClassRelationshipDiagram](<Screenshot 2026-09-24 164845.png>)

## Python Implementation
class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:

    def __init__(self, name, genre, total_duration, song_count):
        self.name = name
        self.genre = genre
        self.totalDuration = total_duration
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("Song is not in the playlist.")

    def play_playlist(self):
        print("Playing playlist:", self.name)

# Song Objects
song1 = Song("Beautiful", "Bazzi", 3.0)
song2 = Song("Sober", "Bazzi", 4.0)

# Playlist Objects
playlistYumi = Playlist("LAUV_ontop", "Pop", 0, 0)

playlistYumi.add_song(song1)
playlistYumi.add_song(song2)

print("name:", playlistYumi.name)
print("genre:", playlistYumi.genre)
print("total duration:", playlistYumi.totalDuration)

print("Songs:")

for song in playlistYumi.songs:
    print(song.title, "-", song.artist, "-", song.duration)

print("song count:", len(playlistYumi.songs))

playlistYumi.play_playlist()


## Test Run 
![cR_TestRun](<Screenshot 2026-09-24 190329.png>)


## Object Relationship Diagram
![cR_ObjectRelationshipDiagram](<Screenshot 2026-09-24 193343.png>)


## Analysis 
### What is the association between your two classes? 
The association between playlist and song is significant, as playlists contain songs. It can store multiple song objects to it which allows the playlit to manage and access the songs connected to it. 

### What multiplicity did you choose and why?
I chose one-to-many multiplicity where one playlist can contain zero or more songs, which is appropriate since a playlist can have many songs that can vary. 

### How did you implement the relationship in Python?
I implemented the relationship by making a list inside the playlist class to store the related song. I also added an add_song() method that adds a song to the list. 

### Why did you store an object reference instead of copying its data?
I store an object reference for the playlist to be able to access the actual song object and its information. Like when a song is added to a playlist, the playlist can then access its attributes through that object which avoids having to copy the song's information into the playlist.

### If your relationship uses many, why is a list appropriate?
A list is necessary because one playlist can cointain many song objects. The list can store many references of a song, and new ones can be added using methods. This makes it easy to loop through the songs and access their informaation. 