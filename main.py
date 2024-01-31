# Task: Write unit tests for several functions related to a poker game based on only spades.
# All of the functions will deal with strings from this tuple:
# cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
# These correspond to the cards 2 of Spades, 3 of Spades, and so on through Jack, Queen, King, and Ace of Spaced.
# S2 has numerical value 2. S3 has numerical value 3, and so on. SJ has numerical value 11, SQ has value 12, SK has value 13, and SA has value 14.
# You can type this in a word processing document, or a notepad, or even on paper.
# Write up test cases for each of the following functions. You don’t need to write as many as possible,
# but you need to write enough to give high confidence the function performs correctly.

# def check_straight(card1, card2, card3)
# If the cards passed in are three cards in a sequence, this function returns the greatest value.
# Otherwise it returns 0. For example, check_straight('S5','S6','S7') would return 7.
# check_straight('S6', 'S5', 'S7') would also return 7.  check_straight('S3','SQ','SK') would return 0. Come up with several tests.
"""
def check_3ofa_kind(card1, card2, card3):
If the three cards passed in are all the same, return the value. Otherwise return 0. For example,
check_3ofa_kind('S9', 'S9', 'S9') would return 9. check_3ofa_kind('S2', 'S4', 'S2') would return 0.

def check_royal_flush(card1, card2, card3):
(The code in this function will make use of the check_straight function from earlier,
and will assume it’s been tested already and is functioning correctly.) If the cards passed in are a straight
with the value of 14, then this function returns 14. Otherwise it returns 0. For this one, you only need maybe three tests.
if left wins return -1
if even return 0
if left loses return 1
"""
print("hello")

