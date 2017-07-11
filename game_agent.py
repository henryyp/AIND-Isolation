"""
    Udacity - AI Coursework
    Henry YP Ho (henryyp.ho@gmail.com)
"""

# --------------------------------------------- #
# SEARCH TIMEOUT CLASS
# --------------------------------------------- #
class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

# --------------------------------------------- #
# CUSTOM SCORE 1 CLASS
# --------------------------------------------- #
def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    raise NotImplementedError

# --------------------------------------------- #
# CUSTOM SCORE 2 CLASS
# --------------------------------------------- #
def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    raise NotImplementedError

# --------------------------------------------- #
# CUSTOM SCORE 3 CLASS
# --------------------------------------------- #
def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!
    raise NotImplementedError

# --------------------------------------------- #
# BASE CLASS
# --------------------------------------------- #
class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

# --------------------------------------------- #
# MINIMAX PLAYER
# --------------------------------------------- #
class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def getClassName(self):
        return __class__.__name__

    # minimax method
    def minimax(self, game, depth):
        legal_moves = game.get_legal_moves()
        curDepth = self.search_depth - depth

        if self.search_depth is depth:
            li = []
            depth -= 1
            for i in legal_moves:
                tDepth, tVal = self.minimax(game.forecast_move(i), depth)
                li.append(tDepth + tVal)
            if len(li) <= 0:
                return (-1, -1)
            num = max(li)
            ind = li.index(num)
            return legal_moves[ind]
        elif depth <= 0:
            return curDepth, len(legal_moves)
        elif not isinstance(legal_moves, list) or len(legal_moves) <= 0:
            return curDepth, 0
        else:
            func = max if depth%2 > 0 else min
            depth -= 1
            tot = []
            for i in legal_moves:
                iDepth, iVal = self.minimax(game.forecast_move(i), depth)
                tot.append( iDepth + iVal )
            return curDepth, func(tot)

# --------------------------------------------- #
# ALPHABETA CLASS
# --------------------------------------------- #
class AlphaBetaPlayer(IsolationPlayer):

    def getClassName(self):
        return __class__.__name__

    # get move, implement iterative deepening
    def get_move(self, game, time_left):
        self.time_left = time_left
        try:
            return self.alphabeta(game, self.search_depth)
        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

    def isTerminal(self, moves, depth):
        val = True if depth is 0 or len(moves) is 0 else False
        return val

    # set and find alpha
    def maxValue(self, game, depth, alpha, beta):
        legal_moves = game.get_legal_moves()
        if self.isTerminal(legal_moves, depth):
            return len(legal_moves), (self.search_depth - depth)

        depth -= 1
        bestVal = float("-inf")
        for i in legal_moves:
            iVal, iDepth = self.minValue(game.forecast_move(i), depth, alpha, beta)
            bestVal = max(bestVal, iVal)
            if bestVal >= beta:
                return bestVal, iDepth
            alpha = max(alpha, bestVal)
        # print('maxValue: ', alpha, beta, bestVal)
        return bestVal, depth


    # set and find beta
    def minValue(self, game, depth, alpha, beta):
        legal_moves = game.get_legal_moves()
        if self.isTerminal(legal_moves, depth):
            return len(legal_moves), (self.search_depth - depth)

        depth -= 1
        bestVal = float("inf")
        for i in legal_moves:
            iVal, iDepth = self.maxValue(game.forecast_move(i), depth, alpha, beta)
            bestVal = min(bestVal, iVal)
            if bestVal <= beta:
                return bestVal, iDepth
            beta = min(beta, bestVal)
        # print('minValue: ', alpha, beta, bestVal)
        return bestVal, depth


    # alpah beta pruning
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):

        legal_moves = game.get_legal_moves()
        bestVal = float("-inf")
        bestDepth = 0
        tot = []

        for i in legal_moves:
            iVal, iDepth = self.minValue(game, depth, bestVal, beta)
            bestVal = iVal if iVal > bestVal else bestVal
            tot.append(bestVal)

        print(tot)

        if len(tot) == 0:
            return (-1, -1)

        index = tot.index( max(tot) )
        return legal_moves[index]
