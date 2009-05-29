#!/usr/bin/env python
#
#       deckofcards.py
#       
#       Copyright 2009 Matthew Brush <mbrush@leftclick.ca>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import os
import random
import pygame
from pygame.locals import *
from playingcard import *

# object represents a deck of cards
class Deck(pygame.sprite.LayeredUpdates):
    """ 
    This is the base Deck class from which more customized decks
    can be inherited.
    """
    theme = 'white'         # change on derived classes for new deck styles
    back_id = 'back01'      # back style, same as above
    
    deck_rectangle = (0,0,0,0)
    
    deck_size = "medium"    # small=25px, medium=50px, large=200px wide
    
    def __init__(self,jokers=False):
        """ 
        Initializes all the cards in the deck using the selected theme 
        """
        pygame.sprite.LayeredUpdates.__init__(self)
        self.reload_ordered()
 
    # the default top left point of the deck
    (x,y) = (18,32)
    
    def reload_ordered(self):
        """ Loads a standard deck in a logical order. """
        self.empty()
        # store all card objects
        self.add(
            Card(CardSuits.CLUBS, CardValues.TWO, self.get_card_image('c_2'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.THREE, self.get_card_image('c_3'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.FOUR, self.get_card_image('c_4'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.FIVE, self.get_card_image('c_5'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.SIX, self.get_card_image('c_6'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.SEVEN, self.get_card_image('c_7'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.EIGHT, self.get_card_image('c_8'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.NINE, self.get_card_image('c_9'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.TEN, self.get_card_image('c_10'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.JACK, self.get_card_image('c_j'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.QUEEN, self.get_card_image('c_q'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.KING, self.get_card_image('c_k'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.CLUBS, CardValues.ACE, self.get_card_image('c_a'), self.get_card_back_image(self.back_id)),

            Card(CardSuits.DIAMONDS, CardValues.TWO, self.get_card_image('d_2'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.THREE, self.get_card_image('d_3'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.FOUR, self.get_card_image('d_4'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.FIVE, self.get_card_image('d_5'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.SIX, self.get_card_image('d_6'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.SEVEN, self.get_card_image('d_7'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.EIGHT, self.get_card_image('d_8'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.NINE, self.get_card_image('d_9'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.TEN, self.get_card_image('d_10'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.JACK, self.get_card_image('d_j'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.QUEEN, self.get_card_image('d_q'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.KING, self.get_card_image('d_k'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.DIAMONDS, CardValues.ACE, self.get_card_image('d_a'), self.get_card_back_image(self.back_id)),

            Card(CardSuits.HEARTS, CardValues.TWO, self.get_card_image('h_2'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.THREE, self.get_card_image('h_3'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.FOUR, self.get_card_image('h_4'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.FIVE, self.get_card_image('h_5'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.SIX, self.get_card_image('h_6'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.SEVEN, self.get_card_image('h_7'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.EIGHT, self.get_card_image('h_8'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.NINE, self.get_card_image('h_9'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.TEN, self.get_card_image('h_10'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.JACK, self.get_card_image('h_j'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.QUEEN, self.get_card_image('h_q'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.KING, self.get_card_image('h_k'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.HEARTS, CardValues.ACE, self.get_card_image('h_a'), self.get_card_back_image(self.back_id)),

            Card(CardSuits.SPADES, CardValues.TWO, self.get_card_image('s_2'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.THREE, self.get_card_image('s_3'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.FOUR, self.get_card_image('s_4'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.FIVE, self.get_card_image('s_5'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.SIX, self.get_card_image('s_6'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.SEVEN, self.get_card_image('s_7'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.EIGHT, self.get_card_image('s_8'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.NINE, self.get_card_image('s_9'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.TEN, self.get_card_image('s_10'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.JACK, self.get_card_image('s_j'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.QUEEN, self.get_card_image('s_q'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.KING, self.get_card_image('s_k'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.SPADES, CardValues.ACE, self.get_card_image('s_a'), self.get_card_back_image(self.back_id)),

            Card(CardSuits.BLACK_JOKER, CardValues.JOKER, self.get_card_image('jk_b'), self.get_card_back_image(self.back_id)),
            Card(CardSuits.RED_JOKER, CardValues.JOKER, self.get_card_image('jk_r'), self.get_card_back_image(self.back_id)) 
        )
        # set back style for cards
        self.back = self.get_card_back_image(self.back_id)
   
    def shuffle(self):
        """ 
        Randomizes the order of the cards in the deck.
        TODO: check if there is a better way to do this.
        """
        c = []                      # create dictionary
        c.extend(self.sprites())    # make a copy of the cards
        random.shuffle(c)           # randomize the dictionary
        self.empty()                # delete all cards from deck
        self.add(c)                 # add the randomized copy back in
        
    def flip_deck(self):
        for sprite in self.sprites():
            if sprite.facedown:
                sprite.set_faceup()
            else:
                sprite.set_facedown()

    def set_facedown(self):
        """ Turn all cards in deck face-down. """
        for sprite in self.sprites():
            sprite.set_facedown()

    def set_faceup(self):
        """ Turn all cards in deck face-up. """
        for sprite in self.sprites():
            sprite.set_faceup()
            
    def bring_to_front(self, card):
        """ Moves the specified card to the top layer. """
        self.move_to_front(card)
    
    def remove_jokers(self):
        """ Remove both jokers from the deck. """
        for card in self.sprites():
            if card.get_value() == CardValues.JOKER:
                self.remove(card)

    def cascade_cards(self,x,y,distance=10):
        """ Layout the cards from the top left to the bottom right. """
        for sprite in self.sprites():
            sprite.set_location(x,y)
            x = x + distance
            y = y + distance

    def slide_cards(self,x,y,distance=12):
        """ 
        Layout cards from the left to the right in a straight line. 
        TODO: add a horizontal/vertical argument and draw accordingly.
        """
        for sprite in self.sprites():
            sprite.set_location(x,y)
            x = x + distance

    def stack_cards(self, x, y):
        """ Stack all the cards one on top of the other. """
        for sprite in self.sprites():
            sprite.set_location(x,y)
 
    def get_card_image(self,id):
        """ Builds a cross-platform, theme-specific path name for the card image """
        path = os.path.join('cards',self.deck_size, self.theme)
        path = os.path.join(path, self.theme + '_' + id + '.png')
        try:
            image = pygame.image.load(path)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error, message:
            print 'Cannot load image: ', path
            raise SystemExit, message
        return image
    
    def get_card_back_image(self,id):
        """ Builds a cross-platform path to the card back image """
        path = os.path.join('cards',self.deck_size,'backs')
        path = os.path.join(path,id + '.png')
        try:
            image = pygame.image.load(path)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except pygame.error, message:
            print 'Cannot load image: ', path
            raise SystemExit, message
        return image


# The following are example decks inherited from the main deck object

class BorderedDeck(Deck):
    """ Standard deck of cards with a Bordered theme. """
    theme = 'bordered'

class OrnamentalDeck(Deck):
    """ Standard deck of cards with an Ornamental theme. """
    theme = 'ornamental'

class WhiteDeck(Deck):
    """ Standard deck of cards with a White theme. """
    theme = 'white'

class SimpleDeck(Deck):
    """ Standard deck of cards with a Simple theme. """
    theme = 'simple'

class EukreDeck(Deck):
    """ A Eukre (card game) deck with the default theme. """
    
    def __init__(self):
        Deck.__init__(self)
        self.remove_jokers()
        count = 0
        for card in self.sprites():
            if (card.get_value() != CardValues.NINE and
                    card.get_value() != CardValues.TEN and
                    card.get_value() != CardValues.JACK and
                    card.get_value() != CardValues.QUEEN and
                    card.get_value() != CardValues.KING and
                    card.get_value() != CardValues.ACE):
                self.remove(card)
                count = count + 1
        self.shuffle()
