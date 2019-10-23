import sys
import os
from unittest import TestCase,mock
from tic_tac_toe import Game


class HiddenPrints:
    """suppress stdout"""
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class GameTest(TestCase):

    @mock.patch('builtins.input')
    def setUp(self,m_input):
        m_input.side_effect = ['Anton','Alena']
        with HiddenPrints():
            self.game = Game()

    @mock.patch('builtins.input')
    def test_check_for_int(self, m_input):
        with HiddenPrints():
            m_input.side_effect = ['5']
            self.assertEqual(self.game.check_for_int('s'), 4)

    def test_is_pos_free(self):
        with HiddenPrints():
            self.assertTrue(self.game.is_pos_free(1))

    @mock.patch('builtins.input')
    def test_turn_suggestion(self, m_input):
        m_input.side_effect = ['3']
        with HiddenPrints():
            self.assertEqual(self.game.turn_suggestion(1),"O")

    def test_check_the_winner(self):
        self.assertFalse(self.game.check_the_winner("X"))


