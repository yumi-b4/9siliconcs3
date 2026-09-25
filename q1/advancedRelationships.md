# Advanced Class Relationships

## Previous Activities
[classAttrib](q1/ClassAttributesMethods.md)
[classRel](q1/ClassRelationships.md)


## Existing System Description:
The system provides a playlist management where users can add or remove songs from it. Each playlist contains informaition such as its name, genre, total duration, and number of songs.

## Inheritance Relationship
Parent: PLaylist
Child: playlistYumi
Explanation: The playlistYumi is a type of Playlist, so it lies under Playlist. It inherits the properties and methods of Playlist.


## Inheritance UML
![Inheritance](aR_inheritanceDiagram.png)

## Composition/Aggregation
Relationship: Playlists contains a collection of Songs
Explanation: A playlist consist of multiple song objects. Songs can exist independently of a Playlist, therefore it represents an aggregation.


## Advanced UML Diagram
![Advanced UML](aR_advancedClassDiagram.png)

## Python Implementation
[Source Code](advancedRelationships.py)

class Song:

    def __init__(self, title, artist, duration):

        self.title = title

        self.artist = artist

        self.duration = duration

class Playlist:

    def ___init__(self, name, genre, total_duration, song_count):
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
![Test](<Screenshot 2026-09-24 190329.png>)


## Object Diagram
![Objects](<Screenshot 2026-09-25 122408.png>)

## Reflection

1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class?

I chose the playlistYumi as the child class of Playlist because it reperesents a specific type of plyalist. It inherits the same basic characteristics and fuctions of a Playlist.


2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.

Inheritance allowed playlistYumi to reuse the methods and attributes that were already defined in the Playlist. Since this was inherited, I didnt have to write the same code again inside playlistYumi.

3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.

The relationship between the playlist and song is aggregation since a playlist contains song objects, however the songs can exist independently from the playlist. Because of this, the playlist does not control the entire lifecycle of the songs that are in the playlist. 

4. What is the difference between Association from Part III and the advanced relationship you
implemented?

The advanced relationship simply showed the aggregation between playlist and song, where a playlist contains multiple song object, but can only exict independently from the playlist. On the other hand, the inheritance relationship is represented between the playlist and playlistYumi, where playlistYumi is a type of playlist that inhertits its attributes and methods. 

5. How does your design follow the DRY principle?

My design follows the DRY principle because common playlist attributes and methods are written only once in the parent class. playlistYumi inherits and reuses them instead of difining the same code again. While the song class also keeps song-related information in one place only, making the whole code easier to maintain and understand while reducing repetition.