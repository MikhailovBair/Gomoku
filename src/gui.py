from itertools import product

import pygame
from pygame import Surface

from src.boardstate import BoardState
import src.settings as settings


def draw_board(screen: Surface, pos_x: int, pos_y: int, elem_size: int,
               board: BoardState):
    black_board_color = (0, 0, 0)
    white_board_color = (200, 200, 200)
    black_figure_color = (100, 100, 100)
    white_figure_color = (255, 255, 255)

    for y, x in product(range(settings.board_size), range(settings.board_size)):
        color = white_board_color if (x + y) % 2 == 0 else black_board_color
        position = (pos_x + x * elem_size, pos_y + y * elem_size,
                    elem_size, elem_size)
        pygame.draw.rect(screen, color, position)
        figure = board.board[y, x]

        if figure == 0:
            continue

        if figure > 0:
            figure_color = white_figure_color
        else:
            figure_color = black_figure_color
        r = elem_size // 2 - 10

        pygame.draw.circle(screen, figure_color,
                           (position[0] + elem_size // 2,
                            position[1] + elem_size // 2), r)

    if board.notification:
        font = pygame.font.SysFont('None', 40)
        text = font.render(board.notification, True, (255, 80, 80))
        text_rect = text.get_rect()
        text_rect.center = (settings.display_size / 2,
                            settings.display_size / 2)
        screen.blit(text, text_rect)
