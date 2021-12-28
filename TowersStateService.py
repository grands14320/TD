from Towers import Tower
from utils.Singleton import SingletonMeta


class TowersStateService(metaclass=SingletonMeta):

    __clicked_structure: Tower.Tower = None

    def set_clicked_structure(self, clicked_structure: Tower.Tower | None):
        self.__clicked_structure = clicked_structure

    def get_clicked_structure(self):
        return self.__clicked_structure


