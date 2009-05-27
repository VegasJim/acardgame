import sys,os
import pygame
from pygame.locals import *


class Card(pygame.sprite.Sprite):
    
    # property accessors, redundant at this point
    def get_suit(self): return self.suit
    def get_value(self): return self.value
    def get_image(self): return self.image
    
    # class initializer, needs suit, card value and the image object
    def __init__(self, suit, value, image):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.suit = suit
        self.value = value
        self.image = image
        self.rect = self.image.get_rect()
        self.area = screen.get_rect()
    
    # used for moving a card
    def set_location(self, x, y):
        #self.rect.move(x,y)
        self.rect.left = x
        self.rect.top = y
        self.rect.clamp_ip(self.area)   # keep within window


# object represents a deck of cards
class CardDeck(pygame.sprite.Group):
    theme = 'white'        # change on derived classes for new deck styles
    back_id = 'back01'      # back style, same as above
    def __init__(self):
        """ Initializes all the cards in the deck using the selected theme """
        pygame.sprite.Group.__init__(self)
        # store all card objects
        self.add(
            Card(CardSuits.CLUBS, CardValues.TWO, self.get_card_image('c_2')),
            Card(CardSuits.CLUBS, CardValues.THREE, self.get_card_image('c_3')),
            Card(CardSuits.CLUBS, CardValues.FOUR, self.get_card_image('c_4')),
            Card(CardSuits.CLUBS, CardValues.FIVE, self.get_card_image('c_5')),
            Card(CardSuits.CLUBS, CardValues.SIX, self.get_card_image('c_6')),
            Card(CardSuits.CLUBS, CardValues.SEVEN, self.get_card_image('c_7')),
            Card(CardSuits.CLUBS, CardValues.EIGHT, self.get_card_image('c_8')),
            Card(CardSuits.CLUBS, CardValues.NINE, self.get_card_image('c_9')),
            Card(CardSuits.CLUBS, CardValues.TEN, self.get_card_image('c_10')),
            Card(CardSuits.CLUBS, CardValues.JACK, self.get_card_image('c_j')),
            Card(CardSuits.CLUBS, CardValues.QUEEN, self.get_card_image('c_q')),
            Card(CardSuits.CLUBS, CardValues.KING, self.get_card_image('c_k')),
            Card(CardSuits.CLUBS, CardValues.ACE, self.get_card_image('c_a')),

            Card(CardSuits.DIAMONDS, CardValues.TWO, self.get_card_image('d_2')),
            Card(CardSuits.DIAMONDS, CardValues.THREE, self.get_card_image('d_3')),
            Card(CardSuits.DIAMONDS, CardValues.FOUR, self.get_card_image('d_4')),
            Card(CardSuits.DIAMONDS, CardValues.FIVE, self.get_card_image('d_5')),
            Card(CardSuits.DIAMONDS, CardValues.SIX, self.get_card_image('d_6')),
            Card(CardSuits.DIAMONDS, CardValues.SEVEN, self.get_card_image('d_7')),
            Card(CardSuits.DIAMONDS, CardValues.EIGHT, self.get_card_image('d_8')),
            Card(CardSuits.DIAMONDS, CardValues.NINE, self.get_card_image('d_9')),
            Card(CardSuits.DIAMONDS, CardValues.TEN, self.get_card_image('d_10')),
            Card(CardSuits.DIAMONDS, CardValues.JACK, self.get_card_image('d_j')),
            Card(CardSuits.DIAMONDS, CardValues.QUEEN, self.get_card_image('d_q')),
            Card(CardSuits.DIAMONDS, CardValues.KING, self.get_card_image('d_k')),
            Card(CardSuits.DIAMONDS, CardValues.ACE, self.get_card_image('d_a')),

            Card(CardSuits.HEARTS, CardValues.TWO, self.get_card_image('h_2')),
            Card(CardSuits.HEARTS, CardValues.THREE, self.get_card_image('h_3')),
            Card(CardSuits.HEARTS, CardValues.FOUR, self.get_card_image('h_4')),
            Card(CardSuits.HEARTS, CardValues.FIVE, self.get_card_image('h_5')),
            Card(CardSuits.HEARTS, CardValues.SIX, self.get_card_image('h_6')),
            Card(CardSuits.HEARTS, CardValues.SEVEN, self.get_card_image('h_7')),
            Card(CardSuits.HEARTS, CardValues.EIGHT, self.get_card_image('h_8')),
            Card(CardSuits.HEARTS, CardValues.NINE, self.get_card_image('h_9')),
            Card(CardSuits.HEARTS, CardValues.TEN, self.get_card_image('h_10')),
            Card(CardSuits.HEARTS, CardValues.JACK, self.get_card_image('h_j')),
            Card(CardSuits.HEARTS, CardValues.QUEEN, self.get_card_image('h_q')),
            Card(CardSuits.HEARTS, CardValues.KING, self.get_card_image('h_k')),
            Card(CardSuits.HEARTS, CardValues.ACE, self.get_card_image('h_a')),

            Card(CardSuits.SPADES, CardValues.TWO, self.get_card_image('s_2')),
            Card(CardSuits.SPADES, CardValues.THREE, self.get_card_image('s_3')),
            Card(CardSuits.SPADES, CardValues.FOUR, self.get_card_image('s_4')),
            Card(CardSuits.SPADES, CardValues.FIVE, self.get_card_image('s_5')),
            Card(CardSuits.SPADES, CardValues.SIX, self.get_card_image('s_6')),
            Card(CardSuits.SPADES, CardValues.SEVEN, self.get_card_image('s_7')),
            Card(CardSuits.SPADES, CardValues.EIGHT, self.get_card_image('s_8')),
            Card(CardSuits.SPADES, CardValues.NINE, self.get_card_image('s_9')),
            Card(CardSuits.SPADES, CardValues.TEN, self.get_card_image('s_10')),
            Card(CardSuits.SPADES, CardValues.JACK, self.get_card_image('s_j')),
            Card(CardSuits.SPADES, CardValues.QUEEN, self.get_card_image('s_q')),
            Card(CardSuits.SPADES, CardValues.KING, self.get_card_image('s_k')),
            Card(CardSuits.SPADES, CardValues.ACE, self.get_card_image('s_a')),

            Card(CardSuits.BLACK_JOKER, CardValues.JOKER, self.get_card_image('jk_b')),
            Card(CardSuits.RED_JOKER, CardValues.JOKER, self.get_card_image('jk_r')) 
        )
        # set back style for cards
        self.back = self.get_card_back_image(self.back_id)
    
    # arrange cards from top left to bottom right
    def cascade_cards(self,x,y,distance=10):
        for sprite in self.sprites():
            sprite.set_location(x,y)
            x = x + distance
            y = y + distance
    
    # arrange cards from left to right in straight line
    def slide_cards(self,x,y,distance=12):
        for sprite in self.sprites():
            sprite.set_location(x,y)
            x = x + distance
                
    def get_card_image(self,id):
        """ Builds a cross-platform, theme-specific path name for the card image """
        path = os.path.join('cards', self.theme)
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
        path = os.path.join('cards','backs')
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

class BorderedCardDeck(CardDeck):
    theme = 'bordered'

class OrnamentalCardDeck(CardDeck):
    theme = 'ornamental'

class WhiteCardDeck(CardDeck):
    theme = 'white'

class SimpleCardDeck(CardDeck):
    theme = 'simple'

# EXTRA DATA/HELPER STUFF

class CardSuits:
    """ Predefined "constants" for card suits and jokers """
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3
    RED_JOKER = 4
    BLACK_JOKER = 5
    
    def get_suit_name(suit):
        if suit == 0: return 'Clubs'
        elif suit == 1: return 'Diamonds'
        elif suit == 2: return 'Hearts'
        elif suit == 3: return 'Spades'
        elif suit == 4: return 'Red Jokers'
        elif suit == 5: return 'Black Jokers'
    
    get_suit_name = staticmethod(get_suit_name)

class CardValues:
    """ Predefined "constants" for card value names """
    JOKER = 0
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    
    def get_value_name(value):
        if value == 0: return 'Joker'
        elif value == 2: return 'Two'
        elif value == 3: return 'Three'
        elif value == 4: return 'Four'
        elif value == 5: return 'Five'
        elif value == 6: return 'Six'
        elif value == 7: return 'Seven'
        elif value == 8: return 'Eight'
        elif value == 9: return 'Nine'
        elif value == 10: return 'Ten'
        elif value == 11: return 'Jack'
        elif value == 12: return 'Queen'
        elif value == 13: return 'King'
        elif value == 14: return 'Ace'

    get_value_name = staticmethod(get_value_name)
