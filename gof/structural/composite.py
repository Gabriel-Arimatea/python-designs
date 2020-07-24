from abc import ABC, abstractmethod


class Media(ABC):

    @abstractmethod
    def get_name(self, object):
        raise NotImplementedError("Adicionar não implementado")

    @abstractmethod
    def play_media(self):
        raise NotImplementedError("Tocar não implementado")


class Song(Media):

    def __init__(self, name):
        self.__name = name
    
    def get_name(self, object):
        print(self.__name)
    
    def play_media(self):
        print(f'Tocando {self.__name}')

class Playlist(Media):

    def __init__(self, name):
        self.__name = name
        self.__list_media = []
    
    def get_name(self, object):
        print(self.__name)
    
    def play_media(self):
        print(f"Tocando {self.__name}")
        for media in self.__list_media:
            media.play_media()

    def add(self, object):
        self.__list_media.append(object)

def test():
    song1 = Song("Full Circle")
    song2 = Song("Scar Tissue")
    playlist1 = Playlist("5FDP")
    playlist1.add(song1)
    playlist1.add(song2)
    song3 = Song("Buried Alive")
    playlist = Playlist("Rock")
    playlist.add(playlist1)
    playlist.add(song3)
    playlist.play_media()