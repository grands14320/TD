from Towers import Tower
from utils.Singleton import SingletonMeta


class DetailsStateService(metaclass=SingletonMeta):

    __active_tower: Tower.Tower = None
    __is_active: bool = False

    def set_is_active(self, is_active):
        self.__is_active = is_active

    def is_active(self):
        return self.__is_active

    def set_active_tower(self, tower: Tower.Tower):
        self.__active_tower = tower

    def get_active_tower(self) -> Tower.Tower:
        return self.__active_tower


