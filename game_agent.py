"""
    Udacity - AI Coursework
    Henry YP Ho (henryyp.ho@gmail.com)
"""
from math import exp, floor
# Using the aggregated winning rate, created a lookup table to the position with highest probability in order
PLAYER1_DIS = {"0": [[[0, 0], 0.99], [[0, 2], 1.98], [[0, 3], 0.99], [[0, 5], 0.99], [[1, 0], 0.99], [[1, 1], 1.98], [[1, 2], 4.95], [[1, 3], 0.99], [[1, 4], 2.97], [[1, 5], 1.98], [[1, 6], 0.99], [[2, 0], 0.99], [[2, 1], 3.96], [[2, 2], 3.96], [[2, 3], 2.97], [[2, 4], 3.96], [[2, 5], 6.93], [[3, 0], 0.99], [[3, 1], 6.93], [[3, 2], 2.97], [[3, 3], 0.99], [[3, 4], 4.95], [[3, 5], 7.92], [[3, 6], 1.98], [[4, 2], 0.99], [[4, 3], 2.97], [[4, 4], 11.88], [[4, 5], 0.99], [[4, 6], 0.99], [[5, 2], 2.97], [[5, 3], 0.99], [[5, 4], 0.99], [[5, 5], 0.99], [[6, 2], 0.99], [[6, 3], 3.96], [[6, 4], 1.98]], "1": [[[0, 1], 0.99], [[0, 2], 1.98], [[0, 5], 2.97], [[1, 0], 1.98], [[1, 1], 0.99], [[1, 2], 1.98], [[1, 3], 6.93], [[1, 4], 6.93], [[1, 5], 1.98], [[2, 1], 3.96], [[2, 2], 1.98], [[2, 3], 2.97], [[2, 4], 3.96], [[2, 5], 2.97], [[2, 6], 1.98], [[3, 0], 0.99], [[3, 1], 0.99], [[3, 2], 3.96], [[3, 3], 2.97], [[3, 4], 2.97], [[3, 5], 1.98], [[3, 6], 0.99], [[4, 1], 6.93], [[4, 2], 4.95], [[4, 3], 3.96], [[4, 4], 4.95], [[4, 5], 3.96], [[4, 6], 0.99], [[5, 1], 2.97], [[5, 2], 2.97], [[5, 3], 4.95], [[5, 4], 2.97], [[5, 5], 0.99]], "2": [[[0, 0], 0.99], [[0, 1], 0.99], [[0, 2], 3.96], [[0, 3], 0.99], [[0, 4], 0.99], [[0, 6], 2.97], [[1, 1], 5.94], [[1, 2], 2.97], [[1, 3], 2.97], [[1, 4], 2.97], [[1, 6], 2.97], [[2, 0], 0.99], [[2, 1], 1.98], [[2, 2], 1.98], [[2, 3], 4.95], [[2, 4], 3.96], [[2, 5], 0.99], [[2, 6], 0.99], [[3, 1], 1.98], [[3, 2], 2.97], [[3, 3], 3.96], [[3, 4], 2.97], [[3, 5], 1.98], [[3, 6], 2.97], [[4, 0], 1.98], [[4, 1], 1.98], [[4, 2], 1.98], [[4, 3], 6.93], [[4, 4], 2.97], [[4, 6], 1.98], [[5, 1], 2.97], [[5, 2], 1.98], [[5, 3], 0.99], [[5, 4], 2.97], [[5, 6], 5.94], [[6, 0], 1.98], [[6, 3], 1.98], [[6, 5], 1.98]], "3": [[[0, 1], 1.98], [[0, 2], 4.95], [[0, 3], 0.99], [[0, 5], 1.98], [[0, 6], 0.99], [[1, 0], 0.99], [[1, 1], 2.97], [[1, 3], 2.97], [[1, 5], 0.99], [[2, 0], 0.99], [[2, 1], 3.96], [[2, 2], 5.94], [[2, 3], 2.97], [[2, 4], 6.93], [[2, 5], 0.99], [[2, 6], 0.99], [[3, 0], 2.97], [[3, 1], 1.98], [[3, 2], 5.94], [[3, 3], 2.97], [[3, 4], 5.94], [[3, 5], 2.97], [[4, 1], 0.99], [[4, 2], 3.96], [[4, 3], 5.94], [[4, 4], 1.98], [[4, 5], 2.97], [[5, 1], 1.98], [[5, 3], 5.94], [[5, 4], 0.99], [[6, 2], 1.98], [[6, 3], 3.96], [[6, 4], 1.98], [[6, 5], 1.98], [[6, 6], 0.99]], "4": [[[0, 0], 0.99], [[0, 1], 1.98], [[0, 2], 1.98], [[0, 3], 3.96], [[0, 4], 4.95], [[0, 5], 1.98], [[0, 6], 0.99], [[1, 0], 3.96], [[1, 1], 0.99], [[1, 2], 1.98], [[1, 3], 2.97], [[1, 4], 4.95], [[1, 6], 1.98], [[2, 0], 0.99], [[2, 1], 2.97], [[2, 2], 0.99], [[2, 3], 2.97], [[2, 4], 0.99], [[2, 5], 1.98], [[2, 6], 1.98], [[3, 0], 1.98], [[3, 2], 2.97], [[3, 3], 1.98], [[3, 4], 0.99], [[3, 5], 2.97], [[3, 6], 2.97], [[4, 0], 1.98], [[4, 1], 2.97], [[4, 2], 3.96], [[4, 3], 0.99], [[4, 4], 3.96], [[4, 6], 3.96], [[5, 0], 1.98], [[5, 1], 1.98], [[5, 2], 0.99], [[5, 4], 0.99], [[5, 5], 3.96], [[6, 1], 0.99], [[6, 2], 3.96], [[6, 4], 3.96], [[6, 5], 1.98], [[6, 6], 0.99]], "5": [[[0, 1], 0.99], [[0, 3], 4.95], [[0, 5], 2.97], [[1, 0], 2.97], [[1, 1], 4.95], [[1, 2], 2.97], [[1, 3], 2.97], [[1, 4], 0.99], [[1, 5], 0.99], [[1, 6], 0.99], [[2, 0], 1.98], [[2, 1], 1.98], [[2, 2], 3.96], [[2, 3], 3.96], [[2, 4], 1.98], [[2, 5], 2.97], [[2, 6], 1.98], [[3, 0], 1.98], [[3, 1], 1.98], [[3, 2], 1.98], [[3, 4], 2.97], [[3, 5], 1.98], [[3, 6], 0.99], [[4, 0], 1.98], [[4, 1], 4.95], [[4, 2], 2.97], [[4, 3], 1.98], [[4, 4], 0.99], [[4, 5], 2.97], [[4, 6], 2.97], [[5, 0], 3.96], [[5, 1], 2.97], [[5, 2], 1.98], [[5, 3], 2.97], [[5, 4], 0.99], [[5, 5], 2.97], [[6, 1], 0.99], [[6, 2], 2.97], [[6, 3], 0.99], [[6, 4], 0.99], [[6, 5], 1.98], [[6, 6], 0.99]], "6": [[[0, 1], 1.98], [[0, 2], 2.97], [[0, 4], 0.99], [[0, 5], 0.99], [[0, 6], 1.98], [[1, 1], 0.99], [[1, 2], 2.97], [[1, 3], 3.96], [[1, 4], 1.98], [[1, 5], 1.98], [[1, 6], 1.98], [[2, 1], 3.96], [[2, 2], 4.95], [[2, 3], 1.98], [[2, 4], 2.97], [[2, 5], 4.95], [[3, 0], 0.99], [[3, 1], 4.95], [[3, 2], 1.98], [[3, 3], 0.99], [[3, 4], 1.98], [[3, 5], 2.97], [[3, 6], 0.99], [[4, 0], 1.98], [[4, 1], 3.96], [[4, 2], 0.99], [[4, 3], 2.97], [[4, 4], 0.99], [[4, 5], 3.96], [[4, 6], 0.99], [[5, 0], 1.98], [[5, 2], 2.97], [[5, 3], 4.95], [[5, 4], 2.97], [[5, 5], 2.97], [[5, 6], 0.99], [[6, 0], 1.98], [[6, 1], 0.99], [[6, 2], 3.96], [[6, 3], 2.97], [[6, 5], 0.99]], "7": [[[0, 0], 0.99], [[0, 1], 0.99], [[0, 2], 0.99], [[0, 3], 3.96], [[0, 4], 2.97], [[0, 5], 0.99], [[1, 1], 1.98], [[1, 2], 0.99], [[1, 3], 2.97], [[1, 4], 0.99], [[1, 5], 2.97], [[1, 6], 0.99], [[2, 0], 1.98], [[2, 2], 2.97], [[2, 3], 1.98], [[2, 4], 2.97], [[2, 5], 2.97], [[2, 6], 1.98], [[3, 0], 1.98], [[3, 1], 5.94], [[3, 2], 3.96], [[3, 3], 1.98], [[3, 4], 2.97], [[3, 5], 0.99], [[3, 6], 0.99], [[4, 0], 0.99], [[4, 1], 3.96], [[4, 2], 2.97], [[4, 3], 4.95], [[4, 4], 3.96], [[4, 5], 1.98], [[4, 6], 2.97], [[5, 0], 2.97], [[5, 1], 1.98], [[5, 2], 0.99], [[5, 3], 5.94], [[5, 4], 3.96], [[6, 0], 0.99], [[6, 1], 0.99], [[6, 2], 2.97], [[6, 3], 0.99], [[6, 5], 0.99]], "8": [[[0, 1], 1.98], [[0, 2], 0.99], [[0, 3], 0.99], [[0, 4], 0.99], [[0, 5], 0.99], [[1, 0], 1.98], [[1, 1], 0.99], [[1, 2], 0.99], [[1, 3], 3.96], [[1, 4], 2.97], [[1, 5], 1.98], [[1, 6], 0.99], [[2, 1], 1.98], [[2, 2], 1.98], [[2, 3], 4.95], [[2, 4], 3.96], [[2, 5], 0.99], [[2, 6], 0.99], [[3, 0], 1.98], [[3, 1], 4.95], [[3, 2], 0.99], [[3, 3], 5.94], [[3, 4], 2.97], [[3, 5], 0.99], [[3, 6], 0.99], [[4, 0], 4.95], [[4, 1], 3.96], [[4, 2], 2.97], [[4, 3], 3.96], [[4, 4], 2.97], [[4, 5], 3.96], [[4, 6], 0.99], [[5, 0], 2.97], [[5, 1], 0.99], [[5, 2], 1.98], [[5, 3], 3.96], [[5, 4], 2.97], [[5, 5], 0.99], [[6, 1], 0.99], [[6, 2], 1.98], [[6, 3], 1.98], [[6, 4], 1.98], [[6, 6], 1.98]], "9": [[[0, 1], 0.99], [[0, 4], 1.98], [[0, 5], 0.99], [[1, 1], 1.98], [[1, 2], 6.93], [[1, 3], 1.98], [[1, 4], 2.97], [[1, 5], 2.97], [[1, 6], 0.99], [[2, 0], 1.98], [[2, 1], 0.99], [[2, 2], 3.96], [[2, 3], 2.97], [[2, 5], 4.95], [[2, 6], 0.99], [[3, 0], 0.99], [[3, 1], 2.97], [[3, 2], 3.96], [[3, 3], 3.96], [[3, 4], 3.96], [[3, 5], 4.95], [[3, 6], 1.98], [[4, 1], 1.98], [[4, 2], 5.94], [[4, 3], 0.99], [[4, 4], 1.98], [[4, 5], 2.97], [[4, 6], 2.97], [[5, 0], 3.96], [[5, 1], 0.99], [[5, 2], 3.96], [[5, 3], 0.99], [[5, 4], 2.97], [[6, 1], 0.99], [[6, 2], 3.96], [[6, 3], 0.99], [[6, 4], 0.99], [[6, 5], 2.97]], "10": [[[0, 0], 1.98], [[0, 1], 0.99], [[0, 2], 2.97], [[0, 3], 1.98], [[0, 4], 0.99], [[0, 5], 1.98], [[1, 0], 1.98], [[1, 1], 1.98], [[1, 2], 3.96], [[1, 3], 0.99], [[1, 5], 0.99], [[1, 6], 0.99], [[2, 0], 2.97], [[2, 1], 2.97], [[2, 2], 2.97], [[2, 3], 4.95], [[2, 4], 1.98], [[2, 5], 1.98], [[2, 6], 3.96], [[3, 0], 0.99], [[3, 1], 1.98], [[3, 2], 4.95], [[3, 3], 1.98], [[3, 4], 2.97], [[3, 5], 0.99], [[4, 0], 0.99], [[4, 1], 2.97], [[4, 2], 4.95], [[4, 3], 2.97], [[4, 5], 3.96], [[4, 6], 2.97], [[5, 0], 1.98], [[5, 1], 5.94], [[5, 2], 3.96], [[5, 3], 0.99], [[5, 4], 0.99], [[5, 5], 0.99], [[6, 0], 0.99], [[6, 1], 0.99], [[6, 2], 0.99], [[6, 3], 0.99], [[6, 4], 0.99], [[6, 5], 1.98], [[6, 6], 1.98]], "11": [[[0, 2], 1.98], [[0, 3], 1.98], [[0, 4], 4.95], [[0, 5], 1.98], [[1, 0], 0.99], [[1, 1], 0.99], [[1, 2], 0.99], [[1, 3], 0.99], [[1, 4], 1.98], [[1, 5], 1.98], [[1, 6], 0.99], [[2, 0], 3.96], [[2, 2], 0.99], [[2, 3], 4.95], [[2, 4], 1.98], [[2, 5], 1.98], [[2, 6], 1.98], [[3, 0], 0.99], [[3, 1], 1.98], [[3, 2], 2.97], [[3, 3], 2.97], [[3, 4], 2.97], [[3, 5], 3.96], [[3, 6], 0.99], [[4, 0], 0.99], [[4, 1], 3.96], [[4, 2], 2.97], [[4, 3], 0.99], [[4, 4], 3.96], [[4, 5], 0.99], [[4, 6], 3.96], [[5, 0], 1.98], [[5, 1], 1.98], [[5, 2], 3.96], [[5, 3], 1.98], [[5, 4], 4.95], [[5, 5], 2.97], [[5, 6], 0.99], [[6, 0], 0.99], [[6, 1], 0.99], [[6, 2], 2.97], [[6, 3], 0.99], [[6, 4], 1.98], [[6, 5], 1.98], [[6, 6], 0.99]], "12": [[[0, 0], 0.99], [[0, 1], 0.99], [[0, 2], 1.98], [[0, 3], 2.97], [[0, 4], 2.97], [[0, 5], 1.98], [[0, 6], 0.99], [[1, 0], 0.99], [[1, 1], 2.97], [[1, 2], 3.96], [[1, 3], 1.98], [[1, 4], 2.97], [[1, 5], 1.98], [[2, 0], 2.97], [[2, 1], 1.98], [[2, 2], 2.97], [[2, 3], 2.97], [[2, 4], 3.96], [[2, 5], 0.99], [[2, 6], 1.98], [[3, 0], 2.97], [[3, 1], 2.97], [[3, 2], 2.97], [[3, 3], 0.99], [[3, 4], 4.95], [[4, 0], 2.97], [[4, 1], 0.99], [[4, 2], 1.98], [[4, 3], 3.96], [[4, 4], 2.97], [[4, 5], 1.98], [[4, 6], 2.97], [[5, 1], 1.98], [[5, 2], 1.98], [[5, 3], 1.98], [[5, 4], 3.96], [[6, 0], 2.97], [[6, 1], 0.99], [[6, 2], 2.97], [[6, 3], 2.97], [[6, 4], 0.99], [[6, 5], 0.99]], "13": [[[0, 1], 0.99], [[0, 2], 0.99], [[0, 4], 1.98], [[0, 6], 0.99], [[1, 1], 2.97], [[1, 2], 1.98], [[1, 3], 0.99], [[1, 4], 1.98], [[1, 5], 2.97], [[2, 0], 0.99], [[2, 1], 1.98], [[2, 2], 0.99], [[2, 3], 3.96], [[2, 4], 0.99], [[2, 5], 6.93], [[2, 6], 0.99], [[3, 0], 0.99], [[3, 1], 0.99], [[3, 2], 3.96], [[3, 3], 1.98], [[3, 4], 3.96], [[3, 5], 1.98], [[3, 6], 3.96], [[4, 0], 0.99], [[4, 1], 1.98], [[4, 2], 3.96], [[4, 3], 3.96], [[4, 4], 2.97], [[4, 5], 0.99], [[4, 6], 2.97], [[5, 0], 1.98], [[5, 1], 0.99], [[5, 2], 2.97], [[5, 3], 2.97], [[5, 4], 3.96], [[5, 5], 0.99], [[5, 6], 1.98], [[6, 0], 2.97], [[6, 1], 0.99], [[6, 2], 1.98], [[6, 3], 2.97], [[6, 4], 1.98], [[6, 5], 1.98], [[6, 6], 2.97]], "14": [[[0, 1], 1.98], [[0, 3], 0.99], [[0, 4], 2.97], [[0, 5], 1.98], [[1, 0], 0.99], [[1, 1], 1.98], [[1, 2], 3.96], [[1, 3], 2.97], [[1, 4], 3.96], [[1, 6], 0.99], [[2, 0], 0.99], [[2, 1], 0.99], [[2, 2], 4.95], [[2, 3], 1.98], [[2, 4], 5.94], [[2, 5], 2.97], [[2, 6], 0.99], [[3, 0], 2.97], [[3, 1], 2.97], [[3, 2], 4.95], [[3, 3], 4.95], [[3, 4], 3.96], [[3, 5], 4.95], [[3, 6], 1.98], [[4, 1], 4.95], [[4, 2], 1.98], [[4, 3], 3.96], [[4, 4], 2.97], [[4, 6], 2.97], [[5, 1], 0.99], [[5, 2], 1.98], [[5, 3], 3.96], [[5, 4], 1.98], [[5, 5], 1.98], [[5, 6], 0.99], [[6, 1], 1.98], [[6, 3], 0.99]]}
PLAYER2_DIS = {"0": [[[0, 2], 2.02], [[0, 3], 3.03], [[0, 4], 1.01], [[0, 5], 2.02], [[1, 0], 2.02], [[1, 1], 1.01], [[1, 2], 1.01], [[1, 3], 5.05], [[1, 4], 1.01], [[1, 5], 1.01], [[1, 6], 1.01], [[2, 1], 5.05], [[2, 2], 5.05], [[2, 3], 4.04], [[2, 4], 4.04], [[2, 5], 1.01], [[3, 0], 3.03], [[3, 1], 5.05], [[3, 2], 1.01], [[3, 4], 4.04], [[3, 5], 5.05], [[3, 6], 1.01], [[4, 0], 2.02], [[4, 1], 4.04], [[4, 2], 5.05], [[4, 3], 1.01], [[4, 4], 6.06], [[4, 5], 4.04], [[4, 6], 3.03], [[5, 2], 3.03], [[5, 3], 3.03], [[5, 4], 3.03], [[6, 1], 1.01], [[6, 2], 2.02], [[6, 4], 2.02], [[6, 5], 1.01], [[6, 6], 1.01]], "1": [[[0, 1], 2.02], [[0, 3], 4.04], [[0, 5], 2.02], [[1, 1], 1.01], [[1, 2], 2.02], [[1, 3], 3.03], [[1, 4], 1.01], [[1, 5], 1.01], [[2, 0], 3.03], [[2, 1], 3.03], [[2, 2], 3.03], [[2, 3], 3.03], [[2, 4], 7.07], [[3, 0], 1.01], [[3, 1], 2.02], [[3, 2], 5.05], [[3, 3], 1.01], [[3, 4], 3.03], [[3, 5], 3.03], [[3, 6], 5.05], [[4, 0], 1.01], [[4, 2], 12.12], [[4, 3], 5.05], [[4, 4], 7.07], [[4, 5], 1.01], [[5, 0], 2.02], [[5, 1], 2.02], [[5, 2], 4.04], [[5, 3], 1.01], [[5, 4], 4.04], [[5, 6], 2.02], [[6, 1], 1.01], [[6, 3], 1.01], [[6, 4], 1.01]], "2": [[[0, 1], 1.01], [[0, 2], 2.02], [[0, 3], 3.03], [[0, 4], 2.02], [[0, 5], 2.02], [[1, 0], 1.01], [[1, 2], 1.01], [[1, 3], 5.05], [[1, 4], 1.01], [[1, 5], 3.03], [[1, 6], 2.02], [[2, 1], 4.04], [[2, 2], 3.03], [[2, 3], 6.06], [[2, 4], 2.02], [[2, 5], 1.01], [[2, 6], 1.01], [[3, 0], 2.02], [[3, 1], 3.03], [[3, 2], 5.05], [[3, 3], 2.02], [[3, 4], 4.04], [[3, 5], 4.04], [[3, 6], 2.02], [[4, 0], 1.01], [[4, 1], 4.04], [[4, 2], 3.03], [[4, 3], 1.01], [[4, 4], 3.03], [[4, 5], 1.01], [[4, 6], 3.03], [[5, 0], 2.02], [[5, 1], 1.01], [[5, 2], 2.02], [[5, 3], 5.05], [[5, 4], 3.03], [[5, 5], 1.01], [[5, 6], 2.02], [[6, 1], 2.02], [[6, 2], 1.01], [[6, 4], 1.01], [[6, 5], 1.01]], "3": [[[0, 4], 1.01], [[1, 0], 1.01], [[1, 1], 3.03], [[1, 2], 6.06], [[1, 3], 1.01], [[1, 5], 3.03], [[1, 6], 1.01], [[2, 1], 1.01], [[2, 2], 4.04], [[2, 3], 10.1], [[2, 4], 6.06], [[2, 5], 2.02], [[2, 6], 1.01], [[3, 0], 1.01], [[3, 1], 3.03], [[3, 2], 3.03], [[3, 3], 3.03], [[3, 4], 3.03], [[3, 5], 2.02], [[3, 6], 3.03], [[4, 0], 2.02], [[4, 1], 1.01], [[4, 2], 3.03], [[4, 3], 6.06], [[4, 4], 7.07], [[4, 5], 3.03], [[4, 6], 2.02], [[5, 1], 1.01], [[5, 3], 1.01], [[5, 4], 3.03], [[5, 5], 2.02], [[6, 1], 3.03], [[6, 2], 2.02], [[6, 3], 1.01], [[6, 4], 3.03], [[6, 6], 1.01]], "4": [[[0, 2], 4.04], [[0, 3], 2.02], [[0, 4], 2.02], [[0, 5], 1.01], [[0, 6], 1.01], [[1, 0], 2.02], [[1, 1], 2.02], [[1, 2], 3.03], [[1, 3], 3.03], [[1, 4], 1.01], [[1, 5], 4.04], [[1, 6], 1.01], [[2, 0], 1.01], [[2, 1], 2.02], [[2, 2], 2.02], [[2, 3], 3.03], [[2, 4], 3.03], [[2, 5], 6.06], [[2, 6], 1.01], [[3, 0], 1.01], [[3, 1], 1.01], [[3, 2], 4.04], [[3, 3], 2.02], [[3, 4], 3.03], [[3, 5], 2.02], [[3, 6], 2.02], [[4, 0], 2.02], [[4, 1], 3.03], [[4, 2], 1.01], [[4, 3], 1.01], [[4, 4], 5.05], [[4, 5], 2.02], [[4, 6], 2.02], [[5, 1], 2.02], [[5, 2], 1.01], [[5, 3], 5.05], [[5, 4], 3.03], [[5, 6], 2.02], [[6, 0], 3.03], [[6, 1], 1.01], [[6, 2], 3.03], [[6, 3], 2.02], [[6, 4], 2.02]], "5": [[[0, 2], 2.02], [[0, 3], 2.02], [[0, 4], 5.05], [[0, 5], 1.01], [[0, 6], 1.01], [[1, 0], 3.03], [[1, 1], 3.03], [[1, 2], 2.02], [[1, 3], 1.01], [[1, 5], 3.03], [[1, 6], 2.02], [[2, 1], 1.01], [[2, 2], 2.02], [[2, 3], 3.03], [[2, 4], 3.03], [[2, 5], 2.02], [[2, 6], 1.01], [[3, 0], 6.06], [[3, 1], 2.02], [[3, 2], 1.01], [[3, 3], 1.01], [[3, 5], 3.03], [[3, 6], 2.02], [[4, 0], 2.02], [[4, 2], 2.02], [[4, 3], 6.06], [[4, 4], 2.02], [[4, 5], 4.04], [[5, 0], 2.02], [[5, 1], 4.04], [[5, 2], 2.02], [[5, 3], 3.03], [[5, 4], 2.02], [[5, 5], 2.02], [[5, 6], 1.01], [[6, 0], 1.01], [[6, 1], 1.01], [[6, 2], 2.02], [[6, 3], 4.04], [[6, 4], 2.02], [[6, 5], 4.04], [[6, 6], 1.01]], "6": [[[0, 0], 1.01], [[0, 3], 3.03], [[0, 5], 1.01], [[1, 0], 1.01], [[1, 1], 4.04], [[1, 2], 2.02], [[1, 3], 4.04], [[1, 4], 2.02], [[1, 5], 1.01], [[2, 0], 1.01], [[2, 1], 4.04], [[2, 2], 3.03], [[2, 3], 6.06], [[2, 4], 3.03], [[2, 5], 3.03], [[2, 6], 2.02], [[3, 0], 3.03], [[3, 1], 1.01], [[3, 2], 5.05], [[3, 3], 4.04], [[3, 4], 3.03], [[3, 5], 3.03], [[3, 6], 2.02], [[4, 0], 2.02], [[4, 1], 3.03], [[4, 2], 3.03], [[4, 3], 2.02], [[4, 4], 1.01], [[4, 5], 1.01], [[4, 6], 3.03], [[5, 2], 4.04], [[5, 3], 2.02], [[5, 4], 2.02], [[5, 5], 3.03], [[5, 6], 1.01], [[6, 1], 1.01], [[6, 2], 2.02], [[6, 3], 3.03], [[6, 4], 1.01], [[6, 5], 1.01], [[6, 6], 2.02]], "7": [[[0, 2], 3.03], [[0, 3], 2.02], [[1, 0], 1.01], [[1, 1], 5.05], [[1, 2], 2.02], [[1, 4], 5.05], [[1, 5], 1.01], [[1, 6], 4.04], [[2, 2], 3.03], [[2, 3], 4.04], [[2, 4], 3.03], [[2, 5], 1.01], [[2, 6], 2.02], [[3, 0], 3.03], [[3, 1], 4.04], [[3, 2], 1.01], [[3, 3], 3.03], [[3, 4], 4.04], [[3, 5], 2.02], [[3, 6], 1.01], [[4, 0], 2.02], [[4, 1], 4.04], [[4, 2], 4.04], [[4, 3], 1.01], [[4, 4], 2.02], [[4, 5], 3.03], [[4, 6], 2.02], [[5, 1], 3.03], [[5, 2], 6.06], [[5, 3], 4.04], [[5, 4], 1.01], [[5, 5], 3.03], [[6, 2], 2.02], [[6, 3], 3.03], [[6, 4], 1.01], [[6, 5], 2.02], [[6, 6], 2.02]], "8": [[[0, 1], 4.04], [[0, 2], 3.03], [[0, 3], 1.01], [[0, 4], 2.02], [[0, 6], 1.01], [[1, 0], 1.01], [[1, 1], 3.03], [[1, 2], 2.02], [[1, 3], 3.03], [[1, 4], 2.02], [[1, 5], 2.02], [[1, 6], 1.01], [[2, 0], 4.04], [[2, 1], 4.04], [[2, 2], 1.01], [[2, 3], 1.01], [[2, 4], 2.02], [[2, 5], 1.01], [[3, 0], 3.03], [[3, 1], 1.01], [[3, 2], 3.03], [[3, 3], 2.02], [[3, 4], 4.04], [[3, 5], 3.03], [[3, 6], 2.02], [[4, 0], 2.02], [[4, 1], 1.01], [[4, 3], 3.03], [[4, 4], 4.04], [[4, 5], 1.01], [[4, 6], 2.02], [[5, 0], 1.01], [[5, 1], 4.04], [[5, 2], 2.02], [[5, 3], 4.04], [[5, 4], 7.07], [[5, 5], 5.05], [[6, 0], 1.01], [[6, 1], 1.01], [[6, 2], 1.01], [[6, 4], 2.02], [[6, 5], 1.01], [[6, 6], 1.01]], "9": [[[0, 1], 1.01], [[0, 2], 3.03], [[0, 3], 1.01], [[0, 4], 4.04], [[0, 6], 1.01], [[1, 0], 2.02], [[1, 1], 2.02], [[1, 2], 3.03], [[1, 4], 2.02], [[1, 5], 2.02], [[2, 0], 1.01], [[2, 1], 3.03], [[2, 2], 2.02], [[2, 3], 3.03], [[2, 4], 3.03], [[2, 5], 1.01], [[2, 6], 3.03], [[3, 0], 1.01], [[3, 1], 1.01], [[3, 2], 4.04], [[3, 3], 6.06], [[3, 4], 9.09], [[3, 5], 2.02], [[4, 0], 2.02], [[4, 1], 2.02], [[4, 2], 3.03], [[4, 3], 3.03], [[4, 4], 2.02], [[4, 5], 3.03], [[4, 6], 2.02], [[5, 0], 2.02], [[5, 1], 1.01], [[5, 2], 1.01], [[5, 4], 5.05], [[5, 5], 2.02], [[6, 0], 1.01], [[6, 1], 2.02], [[6, 2], 1.01], [[6, 3], 2.02], [[6, 4], 3.03], [[6, 5], 1.01], [[6, 6], 1.01]], "10": [[[0, 1], 4.04], [[0, 2], 2.02], [[0, 3], 1.01], [[0, 4], 1.01], [[0, 5], 1.01], [[0, 6], 1.01], [[1, 2], 1.01], [[1, 4], 2.02], [[1, 5], 2.02], [[1, 6], 2.02], [[2, 0], 4.04], [[2, 2], 7.07], [[2, 3], 5.05], [[2, 4], 2.02], [[2, 5], 2.02], [[2, 6], 1.01], [[3, 1], 4.04], [[3, 2], 6.06], [[3, 3], 4.04], [[3, 5], 2.02], [[3, 6], 3.03], [[4, 0], 4.04], [[4, 1], 4.04], [[4, 2], 4.04], [[4, 3], 7.07], [[4, 5], 1.01], [[4, 6], 1.01], [[5, 0], 1.01], [[5, 1], 2.02], [[5, 3], 2.02], [[5, 4], 4.04], [[5, 6], 3.03], [[6, 0], 1.01], [[6, 1], 1.01], [[6, 2], 1.01], [[6, 3], 3.03], [[6, 5], 2.02], [[6, 6], 1.01]], "11": [[[0, 0], 1.01], [[0, 1], 1.01], [[0, 2], 1.01], [[0, 3], 2.02], [[0, 4], 2.02], [[0, 5], 1.01], [[1, 2], 5.05], [[1, 3], 3.03], [[1, 4], 4.04], [[1, 5], 2.02], [[1, 6], 1.01], [[2, 0], 5.05], [[2, 1], 2.02], [[2, 2], 5.05], [[2, 3], 3.03], [[2, 4], 1.01], [[2, 5], 3.03], [[2, 6], 3.03], [[3, 0], 2.02], [[3, 1], 2.02], [[3, 2], 2.02], [[3, 4], 4.04], [[3, 5], 2.02], [[3, 6], 1.01], [[4, 0], 1.01], [[4, 1], 1.01], [[4, 2], 7.07], [[4, 3], 5.05], [[4, 4], 2.02], [[4, 5], 3.03], [[4, 6], 3.03], [[5, 0], 1.01], [[5, 2], 3.03], [[5, 3], 3.03], [[5, 4], 3.03], [[5, 5], 2.02], [[6, 1], 1.01], [[6, 2], 3.03], [[6, 4], 1.01], [[6, 6], 2.02]], "12": [[[0, 1], 2.02], [[0, 3], 3.03], [[0, 4], 3.03], [[0, 5], 2.02], [[1, 1], 3.03], [[1, 2], 5.05], [[1, 3], 4.04], [[1, 4], 4.04], [[1, 5], 2.02], [[2, 0], 3.03], [[2, 1], 2.02], [[2, 2], 2.02], [[2, 3], 1.01], [[2, 4], 2.02], [[2, 6], 2.02], [[3, 0], 4.04], [[3, 1], 4.04], [[3, 2], 3.03], [[3, 3], 4.04], [[3, 4], 1.01], [[3, 5], 5.05], [[3, 6], 1.01], [[4, 0], 2.02], [[4, 1], 4.04], [[4, 2], 2.02], [[4, 3], 2.02], [[4, 4], 2.02], [[4, 5], 1.01], [[4, 6], 1.01], [[5, 0], 1.01], [[5, 2], 4.04], [[5, 5], 4.04], [[6, 0], 2.02], [[6, 1], 3.03], [[6, 2], 3.03], [[6, 3], 1.01], [[6, 4], 3.03], [[6, 5], 2.02]], "13": [[[0, 1], 1.01], [[0, 2], 1.01], [[0, 3], 2.02], [[0, 4], 1.01], [[1, 1], 2.02], [[1, 2], 5.05], [[1, 3], 4.04], [[1, 4], 3.03], [[1, 5], 2.02], [[1, 6], 3.03], [[2, 0], 2.02], [[2, 1], 3.03], [[2, 2], 2.02], [[2, 3], 1.01], [[2, 4], 1.01], [[2, 5], 3.03], [[2, 6], 1.01], [[3, 0], 1.01], [[3, 1], 4.04], [[3, 2], 1.01], [[3, 3], 3.03], [[3, 4], 4.04], [[3, 5], 3.03], [[3, 6], 1.01], [[4, 1], 2.02], [[4, 2], 2.02], [[4, 3], 5.05], [[4, 4], 2.02], [[4, 5], 4.04], [[4, 6], 1.01], [[5, 0], 1.01], [[5, 1], 3.03], [[5, 2], 2.02], [[5, 3], 4.04], [[5, 5], 1.01], [[6, 0], 1.01], [[6, 1], 3.03], [[6, 2], 4.04], [[6, 3], 4.04], [[6, 4], 3.03], [[6, 5], 2.02], [[6, 6], 1.01]], "14": [[[0, 1], 2.02], [[0, 3], 4.04], [[0, 4], 1.01], [[0, 6], 1.01], [[1, 0], 1.01], [[1, 1], 6.06], [[1, 2], 7.07], [[1, 3], 6.06], [[1, 4], 4.04], [[1, 6], 2.02], [[2, 0], 1.01], [[2, 1], 2.02], [[2, 2], 3.03], [[2, 3], 2.02], [[2, 4], 2.02], [[2, 6], 3.03], [[3, 1], 1.01], [[3, 2], 4.04], [[3, 3], 4.04], [[3, 4], 2.02], [[3, 5], 1.01], [[3, 6], 2.02], [[4, 0], 4.04], [[4, 1], 1.01], [[4, 2], 1.01], [[4, 3], 2.02], [[4, 5], 2.02], [[4, 6], 1.01], [[5, 0], 2.02], [[5, 1], 1.01], [[5, 2], 7.07], [[5, 3], 4.04], [[5, 4], 3.03], [[5, 5], 1.01], [[5, 6], 2.02], [[6, 0], 1.01], [[6, 1], 1.01], [[6, 2], 3.03], [[6, 3], 1.01], [[6, 4], 1.01]]}

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
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    dis_to_use = PLAYER1_DIS if game._player_1 is player else PLAYER2_DIS
    move_dist = dis_to_use.get(str(game.move_count), None)
    weighted_move = next((m[1] for m in move_dist if m[0] == list(game.get_player_location(player))), 0.0) if(move_dist is not None) else 0.0

    return game.move_count/2 * (1 + weighted_move + float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player)))) )

# --------------------------------------------- #
# CUSTOM SCORE 2 CLASS
# --------------------------------------------- #
def custom_score_2(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    dis_to_use = PLAYER1_DIS if game._player_1 is player else PLAYER2_DIS
    move_dist = dis_to_use.get(str(game.move_count), None)

    opp_dis_to_use = PLAYER1_DIS if game._player_1 is not player else PLAYER2_DIS
    opp_move_dist = opp_dis_to_use.get(str(game.move_count+1), None)

    weighted_move = next((m[1] for m in move_dist if m[0] == list(game.get_player_location(player))), 0.0) if(move_dist is not None) else 0.0
    opp_weighted_move = next((m[1] for m in opp_move_dist if m[0] == list(game.get_player_location(game.get_opponent(player)))), 0.0) if(opp_move_dist is not None) else 0.0

    return game.move_count/2 + weighted_move - opp_weighted_move + float(len(game.get_legal_moves(player)) - len(game.get_legal_moves(game.get_opponent(player))))


# --------------------------------------------- #
# CUSTOM SCORE 3 CLASS
# --------------------------------------------- #
def custom_score_3(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    # TODO: finish this function!
    w, h = game.width / 2., game.height / 2.
    func = lambda i, j: i + float((h - j[0])**2 + (w - j[1])**2)

    own_moves = sum(float((h - j[0])**2 + (w - j[1])**2) for j in game.get_legal_moves(player)) / float(len(game.get_legal_moves(player))) if len(game.get_legal_moves(player)) > 0 else 0.0
    opp_moves = sum(float((h - j[0])**2 + (w - j[1])**2) for j in game.get_legal_moves(game.get_opponent(player))) / float(len(game.get_legal_moves(game.get_opponent(player)))) if len(game.get_legal_moves(game.get_opponent(player))) > 0 else 0.0

    return game.move_count/2 + float(own_moves - opp_moves)


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
        self.start_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

# --------------------------------------------- #
# SEEMS MORE OPTIMISED MINIMAX PLAYER
# --------------------------------------------- #
class MinimaxPlayer(IsolationPlayer):

    def get_move(self, game, time_left):
        self.time_left = time_left
        best_move = (-1, -1)
        try:
            return self.minimax(game, self.search_depth)
        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed
        return best_move

    def getClassName(self):
        return __class__.__name__

    # minimax method
    def minimax(self, game, depth):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        curDepth = self.search_depth - depth

        if self.search_depth is depth:
            depth -= 1
            li = [self.minimax(game.forecast_move(i), depth) for i in legal_moves]

            if len(li) == 0:
                return (-1, -1)

            return legal_moves[li.index(max(li))]

        elif depth == 0 or len(legal_moves) == 0:
            return self.score(game, self)
        else:
            func = max if depth%2 > 0 else min
            depth -= 1
            return func( self.minimax(game.forecast_move(i), depth) for i in legal_moves )


# --------------------------------------------- #
# ALPHABETA CLASS
# --------------------------------------------- #
class AlphaBetaPlayer(IsolationPlayer):

    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10., isIterative=True):
        super().__init__(search_depth, score_fn, timeout)
        self.isIterative = isIterative

    def getClassName(self):
        return __class__.__name__

    def isIterativeDeeping(self):
        return self.isIterative

    def get_move(self, game, time_left):
        self.time_left = time_left
        output = (-1, -1)
        try:
            for depth in range(self.search_depth,100):
                output = self.alphabeta(game, depth)
            self.search_depth = floor(1.05*(self.search_depth + 0.5))
        except SearchTimeout:
            pass
        # return output
        return output


    # set and find alpha
    def maxValue(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        depth -= 1
        curDepth = self.search_depth - depth

        if depth == 0 or len(legal_moves) == 0:
            return self.score(game, self)

        bestVal = float("-inf")
        for i in legal_moves:
            iVal = self.minValue(game.forecast_move(i), depth, alpha, beta)
            bestVal = max(bestVal, iVal)
            if bestVal >= beta:
                return bestVal
            alpha = max(alpha, bestVal)
        return bestVal


    # set and find beta
    def minValue(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        depth -= 1
        curDepth = self.search_depth - depth

        if depth == 0 or len(legal_moves) == 0:
            return self.score(game, self)

        bestVal = float("inf")
        for i in legal_moves:
            iVal = self.maxValue(game.forecast_move(i), depth, alpha, beta)
            bestVal = min(bestVal, iVal)
            if bestVal <= alpha:
                return bestVal
            beta = min(beta, bestVal)
        return bestVal


    # alpah beta pruning
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):

        legal_moves = game.get_legal_moves()
        bestVal = float("-inf")
        tot = []

        for i in legal_moves:
            iVal = self.minValue(game.forecast_move(i), depth, bestVal, beta)
            bestVal = iVal if iVal >= bestVal else bestVal
            tot.append(iVal)

        if len(tot) == 0:
            return (-1, -1)

        return legal_moves[tot.index( max(tot) )]


# --------------------------------------------- #
# ORIGINAL MINIMAX PLAYER
# --------------------------------------------- #
class OrgMinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """
    def get_move(self, game, time_left):
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.orgMinimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def getClassName(self):
        return __class__.__name__

    def minValue(self, game, depth):
        # TIMEOUT if no time left OR BEGINNING OF SEARCH
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        depth -= 1
        curDepth = self.search_depth - depth

        if len(legal_moves) == 0 or depth == 0:
            return self.score(game, self)

        return min( self.maxValue(game.forecast_move(i), depth) for i in legal_moves ) + curDepth

    def maxValue(self, game, depth):
        # TIMEOUT if no time left OR BEGINNING OF SEARCH
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        legal_moves = game.get_legal_moves()
        depth -= 1
        curDepth = self.search_depth - depth

        if len(legal_moves) == 0 or depth == 0:
            return self.score(game, self)

        return max( self.minValue(game.forecast_move(i), depth) for i in legal_moves ) + curDepth

    # minimax method
    def orgMinimax(self, game, depth):

        legal_moves = game.get_legal_moves()
        if len(legal_moves) == 0:
            return (-1, -1)

        tot = [ self.minValue(game.forecast_move(i), depth) for i in legal_moves ]
        bestScore = max(tot)
        # print('scores: ', bestScore, legal_moves[tot.index(bestScore)])
        return legal_moves[tot.index(bestScore)]
