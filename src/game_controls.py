import pygame
from pygame import Surface

import src.settings as settings
from src.boardstate import BoardState
from src.ai import AI
from src.gui import draw_board


def game_loop(screen: Surface, board: BoardState, ai: AI):
    grid_size = screen.get_size()[0] // settings.board_size

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = [p // grid_size for p in event.pos]
                if event.button == 1:
                    # do move
                    board.notification = None
                    board = board.do_move(x, y)

                elif event.button == 3:
                    # change figure
                    board.board[y, x] = ((board.board[y, x] + 2) % 3) - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board = BoardState.initial_state()

                if event.key == pygame.K_s:
                    board.save()

                if event.key == pygame.K_l:
                    board = BoardState.load()

                if event.key == pygame.K_z:
                    pass

                # if event.key == pygame.K_SPACE:
                #     new_board = ai.next_move(board)
                #     if new_board is not None:
                #         board = new_board

        if board.is_game_finished:
            board.notification = "Second" if board.is_first_player_turn \
                else "First"
            board.notification += " player won! Press R to restart"

        draw_board(screen, 0, 0, grid_size, board)
        pygame.display.flip()
