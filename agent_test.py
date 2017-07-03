"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import json
from importlib import reload
from isolation import Board
from board_analytics import Aggregator
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, custom_score,
                        custom_score_2, custom_score_3)
from sample_players import (RandomPlayer, GreedyPlayer)



class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = Board(self.player1, self.player2)

    def testMiniMax(self):
        playerAB = AlphaBetaPlayer()
        playerMM = MinimaxPlayer()
        playerR = RandomPlayer()
        playerG = GreedyPlayer()


    def runABGreedyStatsTest(self):
        


if __name__ == '__main__':
    unittest.main()
