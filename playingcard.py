#!/usr/bin/env python
#
#       playingcard.py
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
import pygame
from pygame.locals import *

class Card(pygame.sprite.Sprite):
	
	# property accessors, redundant at this point
	def get_suit(self): return self.suit
	def get_value(self): return self.value
	def get_image(self): 
		return self.image
	
	indeck = True
	deck_position = (0,0)
	table_position = (0,0)
	
	def set_facedown(self):
		self.image = self.back
		self.facedown = True
		
	def set_faceup(self):
		self.image = self.face
		self.facedown = False
	
	# class initializer, needs suit, card value and the image object
	def __init__(self, suit, value, image, backimage):
		pygame.sprite.Sprite.__init__(self)
		screen = pygame.display.get_surface()
		self.suit = suit
		self.value = value
		self.image = image
		self.face = image
		self.back = backimage
		self.rect = self.image.get_rect()
		self.area = screen.get_rect()
		self.facedown = False
	
	# used for moving a card
	def set_location(self, x, y):
		#self.rect.move(x,y)
		self.rect.left = x
		self.rect.top = y
		self.rect.clamp_ip(self.area)   # keep within window
		if (self.indeck == True):
			self.deck_position = (x,y)
			for deck in self.groups():
				self.deck_position = (x,deck.y)
			self.rect.left = self.deck_position[0]
			self.rect.top = self.deck_position[1]
			#self.rect.clamp_ip(self.area)
		else:
			self.table_position = (x,y)
			self.rect.left = self.table_position[0]
			self.rect.top = self.table_position[1]
			self.rect.clamp_ip(self.area)

# The rest of this file is some extra helper stuff
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
