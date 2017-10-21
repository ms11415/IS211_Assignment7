#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 7, The Game of Pig"""

import random
import sys

random.seed(0)

class Player(object):
    def __init__(self, name):
        self.score = 0
        self.answer = None
        self.name = name

    def decide(self):
        self.answer = raw_input('(r)oll or (h)old?\n'
                                'Type your choice: ')

    def update_score(self, value):
        self.score += value

class Die(object):

    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class Game(object):

    def __init__(self):
        self.current_player = 0
        self.round_score = 0
        self.total_score = 0

    def announce_turn(self, current_player):
        print 'It is now Player {}\'s turn'.format(current_player.name)

    def update_round_score(self, value):
        self.round_score += value

    def clear_round_score(self):
        self.round_score = 0

def main():

    Pig = Game()
    Die1 = Die()

    playerlist = [Player('1'), Player('2')]

    while Pig.total_score < 100:
        # announce which player is playing
        Pig.announce_turn(playerlist[Pig.current_player])
        # ask player to decide whether to roll or hold
        playerlist[Pig.current_player].decide()

        if playerlist[Pig.current_player].answer == 'r':
            value = Die1.roll()
            print '-' * 40, '\nYou rolled a {}'.format(value)

            if value == 1:
                # subtracts the round score from the player score, to forfeit points
                playerlist[Pig.current_player].score -= Pig.round_score
                print 'You forfeit points earned this round.\nYour score ' \
                      'reverts to {}.'.format(playerlist[Pig.current_player].score)
                print 'Your turn is over.\n', '-' * 40
                # ends turn and sets other player as active
                Pig.current_player = 1 if Pig.current_player == 0 else 0
                # resets round score to 0
                Pig.clear_round_score()

            if 2 <= value <= 6:
                # updates round score based on dice roll
                Pig.update_round_score(value)
                # updates player score based on dice roll
                playerlist[Pig.current_player].update_score(value)
                print 'Your score for this round is {}'.format(Pig.round_score)
                print 'Your new score is {}'.format(playerlist[Pig.current_player].score)
                print '-' * 40
                # updates total game score if player score reaches new high
                if playerlist[Pig.current_player].score > Pig.total_score:
                    Pig.total_score = playerlist[Pig.current_player].score

        elif playerlist[Pig.current_player].answer == 'h':
            print '-' * 40, '\nYour score remains at {}'.format(playerlist[Pig.current_player].score)
            print 'Your turn is now over.\n', '-' * 40
            # updates overall game score if player score reaches new high
            if playerlist[Pig.current_player].score > Pig.total_score:
                Pig.total_score = playerlist[Pig.current_player].score
            #  ends turn and sets other player as active
            Pig.current_player = 1 if Pig.current_player == 0 else 0
            # resets round score to 0
            Pig.clear_round_score()

        else:
            # intercepts invalid input and provides direction
            print '-' * 40, '\n Invalid choice, type \'r\' or \'h\'.\n', '-' * 40

    print 'Game over.'
    sys.exit()

if __name__ == '__main__':
    main()