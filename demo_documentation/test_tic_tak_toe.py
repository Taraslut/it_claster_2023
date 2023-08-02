from unittest import TestCase

from demo_documentation.tic_tac_toe import check_win


def test_check_win():
    b = [["X", "_", "_"],["X", "_", "_"],["X", "_", "_"]]

    rez = check_win(b)

    assert rez == True
