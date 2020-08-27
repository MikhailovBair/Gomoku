from itertools import product

import pygame
from pygame import Surface

from src.settings import Settings
from src.ai import AI, PositionEvaluation
from src.boardstate import BoardState


def draw_board(screen: Surface, pos_x: int, pos_y: int, elem_size: int, board: BoardState):
    black_board_color = (0, 0, 0)
    white_board_color = (200, 200, 200)
    black_figure_color = (100, 100, 100)
    white_figure_color = (255, 255, 255)

    for y, x in product(range(Settings.board_size()), range(Settings.board_size())):
        color = white_board_color if (x + y) % 2 == 0 else black_board_color
        position = pos_x + x * elem_size, pos_y + y * elem_size, elem_size, elem_size
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


def game_loop(screen: Surface, board: BoardState, ai: AI):
    grid_size = screen.get_size()[0] // Settings.board_size()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = [p // grid_size for p in event.pos]
                if event.button == 1:
                    # do move
                    board = board.do_move(x, y)


                elif event.button == 3:
                    # change figure
                    board.board[y, x] = ((board.board[y, x] + 2) % 3) - 1



            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_r:
            #         board = board.inverted()
            #
            #     if event.key == pygame.K_SPACE:
            #         new_board = ai.next_move(board)
            #         if new_board is not None:
            #             board = new_board

        draw_board(screen, 0, 0, grid_size, board)
        pygame.display.flip()


pygame.init()

screen: Surface = pygame.display.set_mode([Settings.display_size(),
                                           Settings.display_size()])
ai = AI(PositionEvaluation(), Settings.ai_search_depth())

game_loop(screen, BoardState.initial_state(), ai)

pygame.quit()
