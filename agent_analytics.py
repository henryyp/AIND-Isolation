from board_analytics import Analytics


if __name__ == "__main__":
    from isolation import Board

    # analytics = Analytics()
    # analytics.boardStats()
    # analytics.boardStats(winnerPlayer='player2')

    analytics = Analytics()
    analytics.boardStats(doc_type='2017-08-09_random_pos_game')
    analytics.boardStats(doc_type='2017-08-09_random_pos_game', winnerPlayer='player2')
