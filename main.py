import random

class PlaylistIterator:
    def hasNext(self):
        pass

    def next(self):
        pass

class SimplePlaylistIterator(PlaylistIterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def hasNext(self):
        return self.index < len(self.playlist.songs)

    def next(self):
        song = self.playlist.songs[self.index]
        self.index += 1
        return song

class ShuffledPlaylistIterator(PlaylistIterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.shuffled_songs = playlist.songs[:]
        random.shuffle(self.shuffled_songs)  # Shuffle the songs randomly
        self.index = 0

    def hasNext(self):
        return self.index < len(self.shuffled_songs)

    def next(self):
        song = self.shuffled_songs[self.index]
        self.index += 1
        return song

class FavoritesPlaylistIterator(PlaylistIterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0

    def hasNext(self):
        while self.index < len(self.playlist.songs):
            if "Fav" in self.playlist.songs[self.index]:  # Mark favorites with 'Fav' in name
                return True
            self.index += 1
        return False

    def next(self):
        song = self.playlist.songs[self.index]
        self.index += 1
        return song

class Playlist:
    def __init__(self):
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def iterator(self, type):
        if type == "simple":
            return SimplePlaylistIterator(self)
        elif type == "shuffled":
            return ShuffledPlaylistIterator(self)
        elif type == "favorites":
            return FavoritesPlaylistIterator(self)
        else:
            return None

# Main code
if __name__ == "__main__":
    # Create a playlist
    playlist = Playlist()
    playlist.addSong("Song 1")
    playlist.addSong("Song 2 Fav")
    playlist.addSong("Song 3")
    playlist.addSong("Song 4 Fav")
    playlist.addSong("Song 5")

    # Simple Playlist Iterator
    print("Simple Playlist:")
    simple_iterator = playlist.iterator("simple")
    while simple_iterator.hasNext():
        print(f"Playing: {simple_iterator.next()}")

    # Shuffled Playlist Iterator
    print("\nShuffled Playlist:")
    shuffled_iterator = playlist.iterator("shuffled")
    while shuffled_iterator.hasNext():
        print(f"Playing: {shuffled_iterator.next()}")

    # Favorites Playlist Iterator
    print("\nFavorites Playlist:")
    favorites_iterator = playlist.iterator("favorites")
    while favorites_iterator.hasNext():
        print(f"Playing: {favorites_iterator.next()}")
