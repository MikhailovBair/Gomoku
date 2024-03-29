import pygame
from pygame import Surface

from src.ai import AI, PositionEvaluation
from src.boardstate import BoardState
from src.game_controls import game_loop
import settings.game_settings as game_set


pygame.init()
screen: Surface = pygame.display.set_mode([game_set.display_size,
                                           game_set.display_size])

ai = AI(PositionEvaluation(), game_set.ai_search_depth)
game_loop(screen, BoardState.initial_state(), ai)
pygame.quit()
