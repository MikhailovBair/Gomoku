import numpy as np
from typing import Optional, List
from src.settings import Settings


class BoardState:
    settings = Settings()

    def __init__(self, board: np.ndarray, is_first_player_turn: bool = True,
                 creator_mode=False):
        self.board: np.ndarray = board
        self.is_first_player_turn: bool = is_first_player_turn
        self.creator_mode = creator_mode

    # def inverted(self) -> 'BoardState':
    #     return BoardState(board=self.board[::-1, ::-1] ^ True,
    #                       is_first_player_turn=not self.is_first_player_turn)

    def copy(self) -> 'BoardState':
        return BoardState(self.board.copy(), self.is_first_player_turn,
                          self.creator_mode)

    def do_move(self, x, y) -> Optional['BoardState']:
        """
        :return: new BoardState or None for invalid move
        """
        if self.board[y, x] != 0:   # invalid move
            return None

        result = self.copy()
        result.board[y, x] = 1 if self.is_first_player_turn else -1
        result.is_first_player_turn = not self.is_first_player_turn

        return result

    # def get_possible_moves(self) -> List['BoardState']:
    #     return [] # todo

    @property
    def is_game_finished(self) -> bool:
        ...  # todo

    @property
    def get_winner(self) -> Optional[int]:
        ...  # todo

    @staticmethod
    def initial_state() -> 'BoardState':
        board = np.zeros(shape=(Settings.board_size(), Settings.board_size()),
                         dtype=np.int8)

        board[7, 0] = 1  # фигура первого игрока
        # board[6, 1] = -1  #фигура второго игрока

        return BoardState(board, True, False)
