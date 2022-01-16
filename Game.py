import pygame

from screens import GameOverSuccess, GameOverDefeat
import Level0
from utils import Time
from EventsStateService import EventStateService
from PlayerProgressStateService import PlayerProgressStateService
from utils.Utility import Tools
from enums.CurrentScreen import CurrentScreen


class Game:

    current_level = 0
    levels = []
    time = Time.Time()
    event_state_service: EventStateService = EventStateService()
    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self):
        pygame.init()
        config = Tools.get_config()
        self.HEIGHT = int(config['window']['HEIGHT'])
        self.WIDTH = int(config['window']['WIDTH'])
        self.FPS = int(config['window']['fps'])
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.__initialize_levels()
        pygame.display.set_caption('TEDE')
        self.running = True
        self.game_over_defeat: GameOverDefeat.GameOverDefeat = GameOverDefeat.GameOverDefeat()
        self.game_over_success: GameOverSuccess.GameOver = GameOverSuccess.GameOver()

    def run(self):
        """
        Runs main game loop
        """
        while self.running:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            self.__draw_relevant_screen()
            self.time.update()
            pygame.display.flip()
            self.check_events()
        pygame.quit()

    def check_events(self):
        """
        Listens for game events such as clicks
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            self.event_state_service.set_events(events)

    def __draw_relevant_screen(self):
        """
        Draws appropaite screen
        """
        if self.player_progress_state_service.get_current_screen() == CurrentScreen.LEVEL:
            if self.levels[self.current_level].is_over:
                self.__initialize_levels()
            self.levels[self.current_level].update(self.window)
        elif self.player_progress_state_service.get_current_screen() == CurrentScreen.GAME_OVER:
            self.game_over_defeat.draw(self.window)
        elif self.player_progress_state_service.get_current_screen() == CurrentScreen.WIN:
            self.game_over_success.draw(self.window)

    def __initialize_levels(self):
        self.levels.clear()
        self.levels.append(Level0.Level0())


