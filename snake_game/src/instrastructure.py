import pygame
from constants import *
from direction import Direction
from element import Element

class Infrastructure:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.fond = pygame.font.Font(None, SCALE)

    def is_quit_enent(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('quit event')
                return True
        return False
    
    def get_pressed_key(self) -> Direction | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Direction.UP
        if key[pygame.K_RIGHT]:
            return Direction.RIGHT
        if key[pygame.K_DOWN]:
            return Direction.DOWN
        if key[pygame.K_LEFT]:
            return Direction.LEFT
        return None
    
    def fill_screen(self) -> None:
        self.screen.fill(SCREEN_COLOR)
    
    def draw_element(self, e: Element, color) -> None:
        pygame.draw.rect(
            self.screen,
            pygame.color(color),
            (e.x * SCALE, e.y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE),
            0,
            ELEMENT_RADIUS
        )

    def draw_score(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}", True, pygame.color(SCORE_COLOR))
            (5,5)
        )

    def draw_game_over(self) -> None:
        message = self.font.render('GAME OVER', True, pygame.color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get.rect(center=((WIDTH // 2) * SCALE, (HEIGHT // 2) * SCALE))
        )

    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(FPS)

    def quit(self) -> None:
        pygame.quit()