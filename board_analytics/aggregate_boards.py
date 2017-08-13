
from elasticsearch import Elasticsearch
from colorama import Fore, Back, Style
import datetime

INDEX = 'aind-isolation'
ADDR = 'http://localhost:9200'

class Aggregator(object):

    def __init__(self, esIndex=INDEX, addr=ADDR):
        try:
            es = Elasticsearch([addr])
            print(Fore.MAGENTA + 'ES info: ', Fore.WHITE + Style.DIM)
            print(es.info())
            print(Style.RESET_ALL)
            self.es = es
            self.addr = addr
            self.esIndex = esIndex

        except Exception as ex:
            print(Fore.RED + 'ES Connection Error', ex)
            print(Style.RESET_ALL)

    # ADD SINGLE GAME RECORD
    def addGameRecord(self,
                      player1,
                      player2,
                      isPlayer1IterativeDeeping,
                      isPlayer2IterativeDeeping,
                      player1StartDepth,
                      player1Depth,
                      player2StartDepth,
                      player2Depth,
                      winner,
                      winnerPlayer,
                      outcome,
                      history,
                      isRandomisePos,
                      timeLimit,
                      game_type):


        body = {
            "player1": player1,
            "player2": player2,
            "player1_iterative_deeping": isPlayer1IterativeDeeping,
            "player2_iterative_deeping": isPlayer2IterativeDeeping,
            "player1_start_depth": player1StartDepth,
            "player1_depth": player1Depth,
            "player2_start_depth": player2StartDepth,
            "player2_depth": player2Depth,
            "winner_type": winner,
            "winner_player": winnerPlayer,
            "history": history,
            "time_limit": str(timeLimit),
            "outcome": outcome,
            "random_position": isRandomisePos,
            "createAt": datetime.datetime.now()
        }

        print(Fore.GREEN + 'add record at: ', body["createAt"])
        print(Style.RESET_ALL)
        return self.es.index(index=self.esIndex, doc_type=game_type, body=body)

    def addSingleBoardRecord(self, game_type, id, depth, moves, time):
        print(FORE.GREEN + 'added: ', self.esIndex, game_agent, id, depth, time, moves)
        print(Style.RESET_ALL)
        return self.es.index(index=self.esIndex, doc_type=game_type, body={
            "boardId": id,
            "depth": depth,
            "timeRemain": time,
            "moves": moves
        })
