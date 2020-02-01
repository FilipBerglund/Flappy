import pygame
from GameState import GameState

WIDTH  = 1000
HEIGHT = 600

class GameLoop:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_state = GameState(self.window)
        clock = pygame.time.Clock()

    def update(self):
        self.game_state.update()

def main():
    game = GameLoop()
    while True:
        game.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
