
from elasticsearch import Elasticsearch
import datetime

INDEX = 'aind-isolation'

class Aggregator(object):

    def __init__(self, addr='http://localhost:9200'):
        try:
            es = Elasticsearch([addr])
            print('ES info: ', es.info())
            self.es = es
        except Exception as ex:
            print('ES Connection Error', ex)


    def addGameRecord(self, player1, player2, winner, outcome, history, depth=0, game_type='game_stats'):

        body = {
            "player1": player1,
            "player2": player2,
            "winner": winner,
            "history": history,
            "description": outcome,
            "createAt": datetime.datetime.now()
        }

        if depth > 0:
            body["searchDepth"] = depth

        return self.es.index(index=INDEX, doc_type=game_type, body=body)

    def addSingleBoardRecord(self, game_type, id, depth, moves, time):
        print('test', INDEX, game_agent, id, depth, time, moves)
        return self.es.index(index=INDEX, doc_type=game_type, body={
            "boardId": id,
            "depth": depth,
            "timeRemain": time,
            "moves": moves
        })
