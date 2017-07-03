
from elasticsearch import Elasticsearch

INDEX = 'aind-isolation'
DOC_TYPE = ''

class Aggregator(object):

    def __init__(self, addr='http://localhost:9200'):
        try:
            es = Elasticsearch([addr])
            print('ES info: ', es.info())
            self.es = es
        except Exception as ex:
            print('ES Connection Error', ex)


    def addBoardRecord(id, depth, time, moves):
        print('test', id, depth, time, moves)
        # self.es.index(index=INDEX, doc_type=DOC_TYPE, body={
        #     "boardId": id,
        #     "depth": depth,
        #     "timeRemain": time,
        #     "moves": moves
        # })
