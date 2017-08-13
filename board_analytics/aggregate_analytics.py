from elasticsearch import Elasticsearch
from colorama import Fore, Back, Style
from functools import reduce
import datetime
import io, json

INDEX = 'aind-isolation'
ADDR = 'http://localhost:9200'

class Analytics:

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

    # BUILD QUERY
    def buildAggQuery(self, num=21):
        output = {}
        for i in range(0, num):
            output['winning_pos_{}'.format(i)] = {
                "scripted_metric": {
                    "params": {
                        "_agg": {
                            "move_num": i,
                            "transactions": []
                        }
                    },
                    "init_script" : "for( int i = 0; i<7; i++ ){ for( int j = 0; j<7; j++ ){ def test = [[i, j]]; test.add(0); params._agg.transactions.add(test) }}",
                    "map_script" : "for(t in params._agg.transactions){ if(params._source.history.get(params._agg.move_num) == t[0]){ t[1]++ } }",
                    "combine_script": "return params._agg.transactions",
                    "reduce_script": "int len = params._aggs.length; int innerLen = params._aggs[0].length; for(int i=0; i<innerLen; i++){ for(int j=1; j<len; j++){ params._aggs[0][i][1] += params._aggs[j][i][1] } } return params._aggs[0]"                }
            }

        return output

    # BOARD STATS AGG
    def boardStats(self, winnerPlayer='player1', doc_type='2017-08-09_random_pos_game', totPos=15, mustQuery=[]):

        allMustQuery = [
              { "match": { "winner_player": winnerPlayer } },
              # { "match": { "player1_iterative_deeping": True } },
              # { "match": { "player2_iterative_deeping": True } }
            ] + mustQuery

        results = self.es.search(index="aind-isolation", doc_type=doc_type, body={
        	"size": 0,
        	"query": {
        	    "bool": {
        		  "must": allMustQuery
        		}
        	},
        	"aggs" : self.buildAggQuery(totPos)
        })

        try:
            winning_move_dist = {}

            for tA in range(0,totPos):
                tName = 'winning_pos_{}'.format(tA)
                tot = reduce(lambda x, y: x + int(y[1]), results['aggregations'][tName]['value'], 0)

                # newResult = sorted(results['aggregations'][tName]['value'],
                #                  key=lambda x: x[1], reverse=True)
                # winning_move_dist[tA] = [x[0] for x in newResult if int(x[1]) > 20]


                tmpR = results['aggregations'][tName]['value']
                normalisedScore = 1/tot * 100 if tot > 0.0 else 0.0
                winning_move_dist[tA] = [[x[0], round(x[1]*normalisedScore, 2)] for x in tmpR if int(x[1]) > 0]

                print('Total Game won for {}: {}'.format(tName, tot))
                for i, v in enumerate(results['aggregations'][tName]['value']):
                    color = Fore.YELLOW if i%2 is 0 else Fore.WHITE
                    prob = round(v[1]/tot * 100, 2) if tot > 0.0 else 0
                    print('{0} {1}:{2}%'.format(color,  v[0], str(prob)))
                print(Style.RESET_ALL)


            print(Fore.MAGENTA, '{} winning_move_dist: '.format(winnerPlayer), winning_move_dist)
            with open('{}_winning_move_dist.json'.format(winnerPlayer), 'w') as outfile:
                json.dump(winning_move_dist, outfile)

        except Exception as ex:
            print('Error: ', ex)
