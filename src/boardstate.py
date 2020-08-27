from itertools import product

import numpy as np
from typing import Optional, List
import src.settings as settings


class BoardState:
    def __init__(self, board: np.ndarray, is_first_player_turn: bool = True,
                 creator_mode=False, notification=None):
        self.board: np.ndarray = board
        self.is_first_player_turn: bool = is_first_player_turn
        self.creator_mode = creator_mode
        self.notification = notification

    # def inverted(self) -> 'BoardState':
    #     return BoardState(board=self.board[::-1, ::-1] ^ True,
    #                       is_first_player_turn=not self.is_first_player_turn)

    def copy(self) -> 'BoardState':
        return BoardState(self.board.copy(), self.is_first_player_turn,
                          self.creator_mode, self.notification)

    def do_move(self, x, y) -> 'BoardState':
        if self.board[y, x] != 0:  # invalid move
            self.notification = "This field is already occupied"
            return self.copy()

        result = self.copy()
        result.board[y, x] = 1 if self.is_first_player_turn else -1
        result.is_first_player_turn = not self.is_first_player_turn

        return result

    # def get_possible_moves(self) -> List['BoardState']:
    #     return [] # todo

    @staticmethod
    def __is_coord_correct(y: int, x: int) -> bool:
        return 0 <= y < settings.board_size and 0 <= x < settings.board_size

    @property
    def is_game_finished(self) -> bool:
        for y, x in product(range(settings.board_size),
                            range(settings.board_size)):
            if self.board[y, x] == 0:
                continue

            modes = ((1, 0), (0, 1), (1, 1), (1, -1))
            answers_for_win_pos = [True, False, False, False, False, False, True]
            for mode in modes:
                victory = True
                for diff in range(-1, 6):
                    new_y = y + mode[0] * diff
                    new_x = x + mode[1] * diff

                    if answers_for_win_pos[diff + 1] != \
                            (not BoardState.__is_coord_correct(new_y, new_x) or
                             self.board[new_y, new_x] != self.board[y, x]):
                        victory = False
                        break

                if victory:
                    return victory
        return False

    # @property
    # def get_winner(self) -> Optional[int]:
    #   ...  # todo

    @staticmethod
    def initial_state() -> 'BoardState':
        board = np.zeros(shape=(settings.board_size, settings.board_size),
                         dtype=np.int8)

        board[settings.board_size // 2, settings.board_size // 2] = -1
        # ход чёрных

        return BoardState(board, True, False)
