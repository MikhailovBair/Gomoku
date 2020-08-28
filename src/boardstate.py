from itertools import product
from typing import List

import numpy as np
import src.settings as settings
import pickle


class BoardState:
    def __init__(self, board: np.ndarray, is_first_player_turn: bool = True,
                 creator_mode=False, notification=None):
        self.board: np.ndarray = board
        self.is_first_player_turn: bool = is_first_player_turn
        self.creator_mode = creator_mode
        self.notification = notification

    def copy(self) -> 'BoardState':
        return BoardState(self.board.copy(), self.is_first_player_turn,
                          self.creator_mode, self.notification)

    def save(self):
        with open('saves/savefile.pickle', 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load():
        with open('saves/savefile.pickle', 'rb') as f:
            new_board_state = pickle.load(f)

        return new_board_state

    def do_move(self, y, x) -> 'BoardState':
        if self.board[y, x] != 0:  # invalid move
            self.notification = "This field is already occupied"
            return self.copy()

        result = self.copy()
        result.board[y, x] = 1 if self.is_first_player_turn else -1
        result.is_first_player_turn = not self.is_first_player_turn

        return result

    def get_good_possible_moves(self) -> List['BoardState']:
        possible_moves = []
        for y, x in product(range(settings.board_size),
                            range(settings.board_size)):
            if self.board[y, x] == 0:
                is_interesting = False
                for dy, dx in settings.interesting_zone:
                    if (self.is_coord_correct(y + dy, x + dx) and
                            self.board[y + dy, x + dx] != 0):
                        is_interesting = True
                        break

                if is_interesting:
                    possible_moves.append(self.copy())
                    possible_moves[-1] = possible_moves[-1].do_move(y, x)
        return possible_moves

    @staticmethod
    def is_coord_correct(y: int, x: int) -> bool:
        return 0 <= y < settings.board_size and 0 <= x < settings.board_size

    @property
    def is_game_finished(self) -> bool:
        for y, x in product(range(settings.board_size),
                            range(settings.board_size)):
            if self.board[y, x] == 0:
                continue

            answers_for_win_pos = [True, False, False, False, False, False,
                                   True]
            for vector in settings.basic_vectors:
                victory = True
                for diff in range(-1, 6):
                    new_y = y + vector[0] * diff
                    new_x = x + vector[1] * diff

                    if answers_for_win_pos[diff + 1] != \
                            (not BoardState.is_coord_correct(new_y, new_x) or
                             self.board[new_y, new_x] != self.board[y, x]):
                        victory = False
                        break

                if victory:
                    return victory
        return False

    @staticmethod
    def initial_state() -> 'BoardState':
        board = np.zeros(shape=(settings.board_size, settings.board_size),
                         dtype=np.int8)

        board[settings.board_size // 2, settings.board_size // 2] = -1
        # ход чёрных

        return BoardState(board, True, False)
