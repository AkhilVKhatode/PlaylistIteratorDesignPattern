# Playlist Iterator in Python

This project demonstrates the implementation of the **Iterator Design Pattern** in Python to iterate through songs in a playlist. There are three types of iterators:

1. **Simple Playlist Iterator**: Iterates over the playlist in the order songs were added.
2. **Shuffled Playlist Iterator**: Shuffles the playlist and iterates through the shuffled order of songs.
3. **Favorites Playlist Iterator**: Iterates only over the songs marked as favorites (those containing the word "Fav" in their name).

## Project Structure

- **playlist_iterator.py**: Contains the implementation of the `Playlist`, `PlaylistIterator`, and various iterators (Simple, Shuffled, and Favorites).
- **main.py**: The entry point where a playlist is created, and all the iterators are demonstrated.

## Features

- Add songs to the playlist.
- Iterate through the playlist in different modes: simple, shuffled, and favorites.
- The favorites iterator skips non-favorite songs by checking if the song name contains "Fav".

## Example Output
```text
Simple Playlist:
Playing: Song 1
Playing: Song 2 Fav
Playing: Song 3
Playing: Song 4 Fav
Playing: Song 5

Shuffled Playlist:
Playing: Song 5
Playing: Song 3
Playing: Song 1
Playing: Song 4 Fav
Playing: Song 2 Fav

Favorites Playlist:
Playing: Song 2 Fav
Playing: Song 4 Fav
```
