import pygame
from pygame import Surface

from src.ai import AI, PositionEvaluation
from src.boardstate import BoardState
from src.game_controls import game_loop
import src.settings as settings


pygame.init()
screen: Surface = pygame.display.set_mode([settings.display_size,
                                           settings.display_size])

ai = AI(PositionEvaluation(), settings.ai_search_depth)
game_loop(screen, BoardState.initial_state(), ai)
pygame.quit()
