## SG 4 - Understanding Classes and Objects

## Class Name
Real-World Context: Music

## Class Description
Class Name: Playlist
Description: It will act as a representation of a musical track that can be played and handled in a music applictaion. 

## Properties

┌───────────────┬────────────┬───────────────────────────────┐
│ Property      │ Data Type  │ Description                   │
├───────────────┼────────────┼───────────────────────────────┤
│ title         │ string     │ Name of the playlist          │
│ totalDuration │ double     │ Total length of the playlist  │
│ creator       │ string     │ Person who made the playlist  │
│ songCount     │ int        │ Number of songs in playlist   │
└───────────────┴────────────┴───────────────────────────────┘


## Methods

Methods         Description
addSong()       It allows to add a song to the playlist
removeSong()    Removes a song from the playlist
playPlaylist()  Starts playing the playlist

## Class Diagram 

┌─────────────────────────────────────┐
│              Playlist               │
├─────────────────────────────────────┤
│ title : String                      │
│ totalDuration : double              │
│ creator : String                    │
│ songCount : int                     │
├─────────────────────────────────────┤
│ addSong(song : String)              │
│ removeSong(song : String)           │
│ playPlaylist()                      │
└─────────────────────────────────────┘

## Design Explanation 
### Why did you choose this class?
    I chose Playlist as a class because it has been a common part of my daily life, particularly when choosing a specific playlist based on the time or mood of the day. In addition, a playlist is a simple example of how objects cann store information and perform actions.

### Which property do you think is the most important? Why?
    I believe that the most important property is the title of the playlist, as it becomes its identity which helps users find it from other playlists. 

### Which property do you think is the most important? Why?
	I believe that the most important property is the title of the playlist, as it becomes its identity which helps users find it from other playlists. 
