class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        filtered_album = [element for element in self.albums if element.name == album_name]
        try:
            if filtered_album[0].published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(filtered_album[0])
            return f"Album {album_name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for element in self.albums:
            result += f"{element.details()}\n"
        return result
