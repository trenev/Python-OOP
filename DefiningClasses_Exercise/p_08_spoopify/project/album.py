class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        filtered_song = [element for element in self.songs if element.name == song_name]
        try:
            if self.published:
                return "Cannot remove songs. Album is published."
            self.songs.remove(filtered_song[0])
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for element in self.songs:
            result += f"== {element.get_info()}\n"
        return result
