from utils.Singleton import SingletonMeta
from enums.CurrentScreen import CurrentScreen


class PlayerProgressStateService(metaclass=SingletonMeta):
    """
    Holds information about player's current progress
    """
    __hp: int = 100
    __money: int = 40
    __current_wave_name: str = 'Idle'
    __is_wave_ongoing = False
    __current_screen: CurrentScreen = CurrentScreen.LEVEL

    def set_hp(self, hp: int) -> None:
        self.__hp = hp

    def get_hp(self) -> int:
        return self.__hp

    def subtract_health(self, amount: int) -> None:
        self.__hp = self.__hp - amount

    def set_money(self, money: int) -> None:
        self.__money = money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, amount: int) -> None:
        self.__money = self.__money + amount

    def subtract_money(self, amount: int) -> None:
        self.__money = self.__money - amount

    def set_current_wave_name(self, wave_name: str) -> None:
        self.__current_wave_name = wave_name

    def get_current_wave_name(self) -> str:
        return self.__current_wave_name

    def set_is_wave_ongoing(self, state: bool) -> None:
        self.__is_wave_ongoing = state

    def get_is_wave_ongoing(self) -> bool:
        return self.__is_wave_ongoing

    def get_current_screen(self) -> CurrentScreen:
        return self.__current_screen

    def set_current_screen(self, screen: CurrentScreen) -> None:
        self.__current_screen = screen

    def restart_progress(self):
        self.__money = 40
        self.__hp = 100
        self.__current_screen = CurrentScreen.LEVEL
        self.__current_wave_name = 'Idle'
        self.__is_wave_ongoing = False

