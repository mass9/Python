from itertools import*
import pprint

FACE_CARD = ('J','K','Q','A')
SUITS = ('H','D','C','S')

DECK = list(product(chain(range(2,11),FACE_CARD),SUITS,))

for card in DECK:
    print('{:>2}{}'.format(*card),end = ' ')
    if card[1] == SUITS[-1]:
        print()
