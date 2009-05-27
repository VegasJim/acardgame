#!/usr/bin/env python

import sys,os
import pygame
from pygame.locals import *
import cardgame


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
    
    # make deck object and arrange it
    deck = cardgame.CardDeck()
    #deck = cardgame.BorderedCardDeck()  # different card theme
    #deck.cascade_cards(10,10)           # different arrangement
    deck.slide_cards(10,10)
    
    # messy flags, need simplification
    incard = False          # within bounds of a card
    insprite = None         # sprite/card being moved
    hoversprite = None      # sprite/card being hovered over
    dragging = False        # card being dragged
    mousedown = False       # mouse is down
    (mx, my) = (0, 0)       # track mouse position
    
    # main game loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return 0
            elif event.type == pygame.MOUSEMOTION:
                (mx, my) = event.pos
                if insprite != None and dragging == True:
                    insprite.rect.centerx = mx
                    insprite.rect.centery = my
                    
                    # todo: snap card to other cards
                    
                else:
                    for sprite in deck.sprites():
                        if sprite.rect.collidepoint(mx, my) and dragging == False:
                            incard = True
                            hoversprite = sprite
                            break
                        else:
                            incard = False
                            insprite = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mx, my) = event.pos
                mousedown = True
                for sprite in deck.sprites():
                    if sprite.rect.collidepoint(mx, my):
                        incard = True
                        insprite = sprite
                        hoversprite = None
                        dragging = True
                        insprite.rect.centerx = mx
                        insprite.rect.centery = my
                        break
                    else:
                        incard = False
                        insprite = None

            elif event.type == pygame.MOUSEBUTTONUP:
                (mx, my) = event.pos
                mousedown = False
                insprite = None
                dragging = False
        screen.blit(background, (0,0))
        deck.clear(screen, background)
        deck.update()
        deck.draw(screen)
        #### TODO: problems arise when dragging cards over each other, fix it
        if incard == True and insprite != None and hoversprite == None:
            insprite.update()
            cardsprite = pygame.sprite.RenderPlain(insprite)
            cardsprite.update()
            cardsprite.draw(screen)
        if incard == True and hoversprite != None and insprite == None:
            hoversprite.update()
            cardsprite = pygame.sprite.RenderPlain(hoversprite)
            cardsprite.update()
            cardsprite.draw(screen)
        if insprite != None:
            pygame.draw.rect(screen,(183,183,183),insprite.rect.inflate(4,4),1)
        if hoversprite != None:
            pygame.draw.rect(screen,(183,183,183),hoversprite.rect.inflate(4,4),1)
        pygame.display.flip()

def load_png(name):
	""" Load image and return image object"""
	fullname = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
        	print 'Cannot load image:', fullname
        	raise SystemExit, message
	return image, image.get_rect()
    
    
def print_deck_data():
    # testing; print deck data
    deck = cardgame.CardDeck()
    for card in deck.cards:
        print cardgame.CardValues.get_value_name(card.get_value()) + ' of ' + \
            cardgame.CardSuits.get_suit_name(card.get_suit())
        print 'Image: ' + card.get_image()
    
if __name__ == '__main__': main()
