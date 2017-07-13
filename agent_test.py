"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import datetime
import json
import random
from importlib import reload
from isolation import Board
from board_analytics import Aggregator
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, OrgMinimaxPlayer,
                        custom_score, custom_score_2, custom_score_3)
from sample_players import (RandomPlayer, GreedyPlayer)



class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""
    def __init__(self):
        self.setup()

    def setup(self):
        # reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = Board(self.player1, self.player2)
        self.agg = Aggregator()

    def playGreedyMMGame(self, player1, player2, repeatNum=1, saveToES=False, randomisePos=True):
        i = 0

        while i < repeatNum:
            game = Board(player1, player2)
            if randomisePos:
                game.apply_move((random.randint(0, 6), random.randint(0, 6)))
                game.apply_move((random.randint(0, 6), random.randint(0, 6)))

            # make sure player 1 is the active player before we finish off the game
            assert(player1 == game.active_player)
            # play game
            winner, history, outcome = game.play(time_limit=float("inf"))

            if not saveToES:
                print('players:', player1.getClassName(), player2.getClassName())
                print('search depth: ', player2.search_depth)
                print('winner:', winner.getClassName(), outcome)
                print('history:', json.dumps(history))
            else:
                depth = player2.search_depth if hasattr(player2, 'search_depth') else 0
                print(test.agg.addGameRecord(player1=player1.getClassName(), player2=player2.getClassName(), depth=depth, outcome=outcome, winner=winner.getClassName(), history=history))

            i += 1

    def testMiniMax(self):
        playerAB = AlphaBetaPlayer()
        playerMM = MinimaxPlayer()
        playerR = RandomPlayer()
        playerG = GreedyPlayer()


    def playTestScore(self):
        playerAB = AlphaBetaPlayer()
        playerMM = MinimaxPlayer()
        playerR = RandomPlayer()
        playerG = GreedyPlayer()
        self.game(playerG, playerMM)

        self.testScoreFunc(game, playerMM)

    def testScoreFunc(self, game, testPlayer):
        print(game.play())





if __name__ == "__main__":
    from isolation import Board
    # unittest.main()
    playerAB = AlphaBetaPlayer(search_depth=7)
    playerMM = MinimaxPlayer(search_depth=5)
    playerOM = OrgMinimaxPlayer(search_depth=3)
    playerR = RandomPlayer()
    playerG = GreedyPlayer()
    test = IsolationTest()

    # test with save
    # test.playGreedyMMGame(player1=playerG, player2=playerFMM, saveToES=True, repeatNum=160)
    # test with LOGS
    test.playGreedyMMGame(player1=playerR, player2=playerMM, saveToES=True, repeatNum=100)
