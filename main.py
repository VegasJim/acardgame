#!/usr/bin/env python
#
#       main.py - Card Game Launcher Script
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
from deckofcards import *

def main():
	""" Main game function """
    
	# init lib and screen
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption('Card Game')
	
	# create a drawing surface
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((81,127,41))
	
	# display surface
	screen.blit(background, (0,0))
	pygame.display.flip()
	
	# setup a deck, with various options
	#deck = CardDeck()             # default card theme, base class
	#deck = BorderedCardDeck()     # different card theme
	deck = EukreDeck()             # customized deck for Eukre
	#deck.cascade_cards(10,10)		        # cascade cards from top left to
                                            # bottom right
	deck.shuffle()                          # randomize cards in deck
	deck.slide_cards(10,10)                 # slide cards from left to right
	#deck.stack_cards(10,10)                # stack cards one atop the other
	#deck.flip_deck()                       # flip deck over
	#deck.remove_jokers()                   # delete joker cards from deck
	
    # some flags to track deck/card state
	incard = False		                    # is cursor within bounds of a card
	insprite = None		                    # sprite/card being moved
	hoversprite = None	                    # sprite/card being hovered over
	dragging = False		                # is card being dragged
	mousedown = False	                    # mouse is down
	(mx, my) = (0, 0)	                    # track mouse position
	
	# main game loop
	while 1:
		for event in pygame.event.get():
            # when window is closed or escape key pressed, exit main function
			if (event.type == QUIT or 
                (event.type == KEYUP and event.key == K_ESCAPE)):
				return 0
            # when mouse is moving
			elif event.type == pygame.MOUSEMOTION:
				(mx, my) = event.pos
				if insprite and dragging:
					insprite.rect.centerx = mx
					insprite.rect.centery = my
				else:
					for sprite in deck.sprites():
                        # grab the first card in the list being hovered
						if sprite.rect.collidepoint(mx, my) and not dragging:
							incard = True
							hoversprite = sprite
							break
                        # otherwise nothing is being hovered
						else:
							incard = False
							insprite = None
            # when a mouse button is clicked
			elif event.type == pygame.MOUSEBUTTONDOWN:
				(mx, my) = event.pos
				mousedown = True
                # determine first card being clicked on
				for sprite in deck.sprites():
					if sprite.rect.collidepoint(mx, my):
						incard = True
						insprite = sprite
						hoversprite = None
						dragging = True
						insprite.rect.centerx = mx
						insprite.rect.centery = my
						deck.bring_to_front(insprite)
						break
					else:
						incard = False
						insprite = None
            # when mouse button is no longer pressed
			elif event.type == pygame.MOUSEBUTTONUP:
				(mx, my) = event.pos
				mousedown = False
				dragging = False
            # flip deck when 'f' key is pressed
			elif (event.type == KEYUP) and (event.key == K_f):
				deck.flip_deck()
            # shuffle deck when 's' key is pressed
			elif (event.type == KEYUP) and (event.key == K_s):
				deck.shuffle()
            # reset/shuffle/slide cards out when 'r' is pressed
			elif (event.type == KEYUP) and (event.key == K_r):
				deck.shuffle()
				deck.slide_cards(10, 10)

		screen.blit(background, (0,0))
		deck.clear(screen, background)
		deck.update(deck.draw(screen))
        
        # draw a box around the card being hovered
		if hoversprite:
			pygame.draw.rect(screen,(183,183,183),hoversprite.rect.inflate(4,4),1)
		pygame.display.flip()

if __name__ == '__main__': main()
