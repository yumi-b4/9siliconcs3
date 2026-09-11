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
![ClassRelationshipDiagram](<Class Relationship Diagram.png>)

## Python Implementation
    
    class Song:
        def __init__(self, title, artist, duration):
            self.title = title
            self.artist = artist
            self.duration = duration

        def display_song(self):
            print("Song:", self.title)
            print("Artist:", self.artist)
            print("Duration:", self.duration, "minutes")


    class Playlist:
        def __init__(self, title, totalDuration, creator, songCount):
            self.title = title
            self.totalDuration = totalDuration
            self.creator = creator
            self.__songCount = songCount
            self.songs = []

        def add_song(self, song):
            self.songs.append(song)
            self.__songCount += 1
            self.totalDuration += song.duration

        def remove_song(self, song):
            if song in self.songs:
                self.songs.remove(song)
                self.__songCount -= 1
                self.totalDuration -= song.duration
            else:
                print("Song is not in the playlist.")

        def play_playlist(self):
            print("Playing:", self.title)

            for song in self.songs:
                print("-", song.title, "by", song.artist)

        def display_playlist(self):
            print("Title:", self.title)
            print("Total Duration:", self.totalDuration, "minutes")
            print("Creator:", self.creator)
            print("Song Count:", self.__songCount)

        def get_song_count(self):
            return self.__songCount


    playlist1 = Playlist("Study Playlist", 120.5, "Maria", 10)

    song1 = Song("Until I Found You", "Stephen Sanchez", 2.57)
    song2 = Song("Dandelions", "Ruth B.", 3.53)
    song3 = Song("Snooze", "SZA", 3.22)


    print("--- BEFORE ASSOCIATION ---")
    playlist1.display_playlist()

    print("Songs connected:", len(playlist1.songs))


    print("\n--- BUILDING RELATIONSHIP ---")
    print("Adding songs to Playlist...")

    playlist1.add_song(song1)
    playlist1.add_song(song2)
    playlist1.add_song(song3)


    print("\n--- AFTER ASSOCIATION ---")
    playlist1.display_playlist()

    print("\nRelated songs:")

    for song in playlist1.songs:
        print("-", song.title, "by", song.artist)


    print("\n--- PLAYLIST ---")
    playlist1.play_playlist()
```



## Test Run 
![Test Run](<Screenshot 2026-09-12 014126.png>)

## Object Relationship Diagram


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