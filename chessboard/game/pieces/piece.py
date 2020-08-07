from abc import ABC, abstractmethod


class Piece(ABC):

    @abstractmethod
    def set_in_play(self, inPlay: bool):
        pass

    @abstractmethod
    def is_in_play(self) -> bool:
        pass

    @abstractmethod
    def set_position(self, pos):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def set_photo(self, photo):
        pass

    @abstractmethod
    def get_photo(self):
        pass

