"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import argparse
import datetime
import json
import random
from colorama import Fore, Back, Style
from importlib import reload
from isolation import Board
from board_analytics import Aggregator
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, OrgMinimaxPlayer,
                        custom_score, custom_score_2, custom_score_3)
from sample_players import (RandomPlayer, GreedyPlayer)



class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""
    def __init__(self):
        self.agg = Aggregator()

    # SETUP CONDITIONS
    def setupConditions(self,
                        Player1,
                        Player2,
                        player1SearchDepth,
                        player2SearchDepth,
                        player1IsIterative,
                        player2IsIterative,
                        randomisePos):
        player1 = Player1(search_depth=player1SearchDepth, isIterative=player1IsIterative)
        player2 = Player2(search_depth=player2SearchDepth, isIterative=player2IsIterative)
        game = Board(player1, player2)
        if randomisePos:
            game.apply_move((random.randint(0, 6), random.randint(0, 6)))
            game.apply_move((random.randint(0, 6), random.randint(0, 6)))

        return (player1, player2, game)

    # PLAYER 2 GAME
    def playerGame(self, Player1, Player2,
                    repeatNum=1, saveToES=False, showLogs=False,
                    randomisePos=True, time_limit=150,
                    player1_search_depth=3,
                    player1_is_iterative_deepening=False,
                    player2_search_depth=3,
                    player2_is_iterative_deepening=False,
                    game_type='game_stats'):


        while repeatNum > 0:
            player1, player2, game = self.setupConditions(Player1,
                                                          Player2,
                                                          player1_search_depth,
                                                          player2_search_depth,
                                                          player1_is_iterative_deepening,
                                                          player2_is_iterative_deepening,
                                                          randomisePos)

            # make sure player 1 is the active player before we finish off the game
            assert(player1 == game.active_player)
            # play game
            winner, history, outcome = game.play(time_limit)

            winnerColor = Fore.WHITE if winner is player1 else Fore.YELLOW
            winnerPlayer = 'player1' if winner is player1 else 'player2'

            if not saveToES or showLogs:
                print(Fore.CYAN     + 'name (ES type):              ', game_type)
                print(Fore.CYAN     + 'time limit:                  ', time_limit)
                print(Fore.GREEN    + 'players:                     ', Fore.WHITE + player1.getClassName(), Fore.GREEN  + 'VS', Fore.YELLOW + player2.getClassName())
                print(Fore.WHITE    + 'player1 start depth:         ', player1.start_depth)
                print(Fore.WHITE    + 'player1 depth:               ', player1.search_depth)
                print(Fore.WHITE    + 'player1 iterative deepening: ', player1.isIterativeDeeping())
                print(Fore.YELLOW   + 'player2 start depth:         ', player2.start_depth)
                print(Fore.YELLOW   + 'player2 depth:               ', player2.search_depth)
                print(Fore.YELLOW   + 'player2 iterative deepening: ', player2.isIterativeDeeping())
                print(winnerColor   + 'winner:                      ', winner.getClassName())
                print(winnerColor   + 'winner player:               ', winnerPlayer)
                print(Fore.MAGENTA  + 'radomised position:          ', randomisePos)
                print(Fore.MAGENTA  + 'outcome:                     ', outcome)
                print(Fore.MAGENTA  + 'history:                     ', json.dumps(history))
                print(Style.RESET_ALL)


            if saveToES:
                self.agg.addGameRecord(
                    player1=player1.getClassName(),
                    player2=player2.getClassName(),
                    isPlayer1IterativeDeeping=player1.isIterativeDeeping(),
                    isPlayer2IterativeDeeping=player2.isIterativeDeeping(),
                    player1StartDepth=player1.start_depth,
                    player1Depth=player1.search_depth,
                    player2StartDepth=player2.start_depth,
                    player2Depth=player2.search_depth,
                    outcome=outcome,
                    winner=winner.getClassName(),
                    winnerPlayer=winnerPlayer,
                    history=history,
                    isRandomisePos=randomisePos,
                    timeLimit=time_limit,
                    game_type=game_type)

            repeatNum -= 1




if __name__ == "__main__":
    from isolation import Board
    # unittest.main()

    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    isoTest = IsolationTest()
    parser = argparse.ArgumentParser(description="test and save agents")
    parser.add_argument('-name', help='AIND ')
    parser.add_argument('-name_date', action='store_true', help='AIND boolean to add date')
    parser.add_argument('-write', action='store_true', help='AIND boolean to write to ES')
    parser.add_argument('-logs', action='store_true', help='AIND boolean to show logs')
    parser.add_argument('-repeat', type=int, help='AIND integer to number of times to repeat')
    parser.add_argument('-time_limit', type=float, help='AIND float to time limit')
    parser.add_argument('-p1_type', help='AIND string of the type of player 1')
    parser.add_argument('-p2_type', help='AIND string of the type of player 2')
    parser.add_argument('-p1_iterative', action='store_true', help='AIND boolean is iterative deepening for player 1')
    parser.add_argument('-p2_iterative', action='store_true', help='AIND boolean is iterative deepening for player 2')
    parser.add_argument('-p1_depth', type=int, help='AIND integer for search depth of player 1')
    parser.add_argument('-p2_depth', type=int, help='AIND integer for search depth of player 2')
    parser.add_argument('-p1_heuristic', help='AIND string name of the Heuristic Function for player 1')
    parser.add_argument('-p2_heuristic', help='AIND string name of the Heuristic Function for player 2')
    args = parser.parse_args()

    Player1 = {
        'greedy': GreedyPlayer,
        'alphabeta': AlphaBetaPlayer,
        'minimax': MinimaxPlayer,
        'random': RandomPlayer
    }.get(vars(args)['p1_type'], GreedyPlayer) # vars() turn namespace object to Dictionary

    Player2 = {
        'greedy': GreedyPlayer,
        'alphabeta': AlphaBetaPlayer,
        'minimax': MinimaxPlayer,
        'random': RandomPlayer
    }.get(vars(args)['p2_type'], GreedyPlayer)

    Heuristic1 = {
        'custom_score': custom_score,
        'custom_score_2': custom_score_2,
        'custom_score_3': custom_score_3
    }.get(vars(args)['p1_heuristic'], custom_score)

    Heuristic2 = {
        'custom_score': custom_score,
        'custom_score_2': custom_score_2,
        'custom_score_3': custom_score_3
    }.get(vars(args)['p2_heuristic'], custom_score)

    gameType = args.name if args.name is not None else 'game_stats'
    gameType = str(datetime.date.today()) + '_' + gameType if args.name_date is True else gameType

    # test with LOGS
    isoTest.playerGame(Player1=Player1,
                       Player2=Player2,
                       saveToES=args.write,
                       showLogs=args.logs,
                       time_limit=args.time_limit if args.time_limit is not None else 150,
                       repeatNum=args.repeat if args.repeat is not None else 1,
                       player1_is_iterative_deepening=args.p1_iterative,
                       player2_is_iterative_deepening=args.p2_iterative,
                       player1_search_depth=args.p1_depth if args.p1_depth is not None else 3,
                       player2_search_depth=args.p2_depth if args.p2_depth is not None else 3,
                       game_type=gameType)
