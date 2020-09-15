from src.boardstate import BoardState
from src.ai import AI


def test_next_move():
    cur_ai = AI()
    current_board = BoardState.initial_state()
    answer1_board = BoardState.initial_state()
    answer2_board = BoardState.initial_state()
    current_board.load('board_3_in_a_row.pickle')
    answer1_board.load('board_3_in_a_row_ans1.pickle')
    answer2_board.load('board_3_in_a_row_ans2.pickle')
    assert (cur_ai.next_move(current_board, None)[0].board.all() ==
            answer1_board.board.all() or
            cur_ai.next_move(current_board, None)[0].board ==
            answer2_board.board.all())
