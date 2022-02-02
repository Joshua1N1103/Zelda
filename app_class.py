import sys, pygame
from settings import *
from level import Level

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        pygame.display.set_caption('Zelda')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'

        # Variables
        self.level = Level()

        self.load()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'help':
                # How to play page here
                pass
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    ############### HELPER FUNCTIONS ###############

    def draw_text(self, words, screen, pos, size, color, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        text_size = text.get_size()
        pos[0] = pos[0] - text_size[0] / 2
        pos[1] = pos[1] - text_size[1] / 2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('assets/TowerDefense_Text.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (800, 150)).convert_alpha()
        self.start_button = pygame.image.load('assets/Start_text.png').convert_alpha()
        self.start_button_rect = self.start_button.get_rect(center= (680, 400))
        self.start_button = pygame.transform.scale(self.start_button, (400, 75)).convert_alpha()
        self.exit_button = pygame.image.load('assets/Exit_text.png').convert_alpha()
        self.exit_button = pygame.transform.scale(self.exit_button, (400, 75)).convert_alpha()
        self.exit_button_rect = self.exit_button.get_rect(center= (680, 600))
        self.howtoplay_button = pygame.image.load('assets/HowtoPlay_text.png').convert_alpha()
        self.howtoplay_button = pygame.transform.scale(self.howtoplay_button, (500, 100)).convert_alpha()
        self.howtoplay_button_rect = self.howtoplay_button.get_rect(center= (650, 800))

    ############### INTRO FUNCTIONS ###############

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'playing'
                elif self.howtoplay_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'help'
                elif self.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.blit(self.background, (500, 10))
        self.screen.blit(self.start_button, (680, 400))
        self.screen.blit(self.exit_button, (680, 600))
        self.screen.blit(self.howtoplay_button, (650, 800))

        pygame.display.update()

    ############### PLAYING FUNCTIONS ###############

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Events while Playing

    def playing_update(self):
        pass

    def playing_draw(self):
        self.screen.fill('light gray')
        self.level.run()


        pygame.display.update()
        '''self.draw_text('CURRENT SCORE: 0', self.screen, [WIDTH / 2 - 150, 12], 18, WHITE, START_FONT)
        self.draw_text('HIGH SCORE: 0', self.screen, [WIDTH / 2 + 150, 12], 18, WHITE, START_FONT)'''
