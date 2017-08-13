"""
    Udacity - AI Coursework
    Henry YP Ho (henryyp.ho@gmail.com)
"""

# --------------------------------------------- #
# RECURSIVE GAME TREE WITH GIVEN DEPTH
# --------------------------------------------- #
def recursiveGameTree(game, depth=3):
    legal_moves = game.get_legal_moves()
    if depth > 0 and len(legal_moves) > 0:
        depth -= 1
        return dict((i, recursiveGameTree(game.forecast_move(i), depth)) for i in legal_moves)
    else:
        return len(legal_moves)

# --------------------------------------------- #
# CALCULATE MINIMAX FOR EACH LEVEL
# --------------------------------------------- #
def calMM(tree, curLevel=0):
    if isinstance(tree, list):
        return [calMM(v, curLevel) for v in tree]
    elif isinstance(tree, dict):
        # Append level
        curLevel += 1
        # Odd / Even represents Max or Min
        func = min if curLevel%2 > 0 else max
        """
            Suggested in the Slack forum, using generator expression
            RATHER than list comprehension to conserve memory use, e.g.

            To work out min() of some value:
                tList = [self.calMM(v, curLevel) for k, v in tree.items()]
                return min(tList)
            We can simply do, which create the list in memory and apply the function:
                min(self.calMM(v, curLevel) for k, v in tree.items())
        """
        return func(calMM(v, curLevel) for k, v in tree.items())

    elif isinstance(tree, int):
        return tree + curLevel

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
        # get legal moves
        legal_moves = game.get_legal_moves()
        # build game tree
        tree = recursiveGameTree(game, depth)

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        elif (isinstance(tree, dict)):
            calTree = calMM(list(tree.values()), depth)
            treeKey = list(tree.keys())
            return treeKey[calTree.index(max(calTree))]
        else:
            # if no tree return final legal moves or abandon game
            return legal_moves[len(legal_moves) - 1] if len(legal_moves) > 0 else (-1,-1)

# --------------------------------------------- #
# Data Gathering MINIMAX PLAYER
# --------------------------------------------- #
class DGMiniMaxPlayer(IsolationPlayer):

    # get move, implement iterative deepening
    def get_move(self, game, time_left):
        self.time_left = time_left
        best_move = (-1, -1)
        depth = 1
        self.moveCount = 0
        startTime = time()
        moveDepth = [8,8,9,11,11,11,15,20,15,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30]
        while time_left() > 100 and depth < moveDepth[self.moveCount]:
            best_move = self.dgminimax(game, depth)
            print('minimax time left:', time_left(), time() - startTime, self.moveCount, depth)
            depth += 1
        else:
            self.moveCount += 1
            return best_move

    # minimax method
    def dgminimax(self, game, depth):
        # get legal moves
        legal_moves = game.get_legal_moves()
        # build game tree
        tree = recursiveGameTree(game, depth)


        if (isinstance(tree, dict)):
            calTree = calMM(list(tree.values()), depth)
            treeKey = list(tree.keys())
            return treeKey[calTree.index(max(calTree))]
        else:
            # if no tree return final legal moves or abandon game
            return (-1,-1)

# --------------------------------------------- #
# FULL MINIMAX CLASS
# --------------------------------------------- #
class FullMinimaxPlayer(IsolationPlayer):
    # get move, implement iterative deepening
    def get_move(self, game, time_left):
        self.time_left = time_left
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()

        li = []
        for i in legal_moves:
            tDepth, tVal = self.fullMinimax(game.forecast_move(i), self.search_depth)
            li.append(tDepth + tVal)
        if len(li) <= 0:
            return (-1, -1)
        num = max(li)
        ind = li.index(num)
        return legal_moves[ind]

    def getClassName(self):
        return __class__.__name__

    # full minimax
    def fullMinimax(self, game, depth):
        legal_moves = game.get_legal_moves()
        curDepth = self.search_depth - depth

        if depth <= 0:
            return curDepth, len(legal_moves)
        elif not isinstance(legal_moves, list) or len(legal_moves) <= 0:
            return curDepth, 0
        else:
            func = min if depth%2 > 0 else max
            depth -= 1
            tot = []
            for i in legal_moves:
                iDepth, iVal = self.fullMinimax(game.forecast_move(i), depth)
                tot.append( iDepth + iVal )
            return curDepth, func(tot)

# --------------------------------------------- #
# ALPHABETA CLASS
# --------------------------------------------- #
class AlphaBetaPlayer(IsolationPlayer):

    # get move, implement iterative deepening
    def get_move(self, game, time_left):
        self.time_left = time_left
        self.search_depth = 7
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()

        li = []
        for i in legal_moves:
            tDepth, tVal, tA, tB = self.alphabeta(game.forecast_move(i), self.search_depth)
            li.append(tDepth + tVal)
            # print('ab', tA, tB)
        if len(li) <= 0:
            return (-1, -1)
        num = max(li)
        ind = li.index(num)
        return legal_moves[ind]

    def calAlphaBeta(self, d, val, alpha, beta):
        if (d)%2 > 0:
            return val, beta
        else:
            return alpha, val

    # alpah beta pruning
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        legal_moves = game.get_legal_moves()
        curDepth = self.search_depth - depth
        func = min if depth%2 > 0 else max
        if depth <= 0:
            a, b = self.calAlphaBeta(depth, len(legal_moves), alpha, beta)
            return curDepth, len(legal_moves), a, b
        elif not isinstance(legal_moves, list) or len(legal_moves) <= 0:
            return curDepth, 0, alpha, beta
        else:
            depth -= 1
            tot = []
            for i in legal_moves:
                a, b = self.calAlphaBeta(depth, len(legal_moves), alpha, beta)
                iDepth, iVal, iA, iB = self.alphabeta(game.forecast_move(i), depth, a, b)
                tot.append(iVal)
                # if iVal > b or iVal < a:
                #     continue
                # else:
                break
            # print('tmp', depth, iDepth, func(tot), iA, iB)
            return depth, func(tot), iA, iB
