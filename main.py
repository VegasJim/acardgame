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
    screen = pygame.display.set_mode((1024,768))
    pygame.display.set_caption('Card Game')
    
    # create a drawing surface
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((81,127,41))
    
    # display surface
    screen.blit(background, (0,0))
    pygame.display.flip()
    
    # setup a deck, with various options
    deck = Deck()                           # default card theme, base class
    #deck = BorderedDeck()                  # different card theme
    #deck = EukreDeck()                     # customized deck for Eukre
    #deck.cascade_cards(10,10)              # cascade cards from top left to
                                            # bottom right
    deck.shuffle()                          # randomize cards in deck
    deck.slide_cards(18,32)                 # slide cards from left to right
    #deck.stack_cards(10,10)                # stack cards one atop the other
    #deck.flip_deck()                       # flip deck over
    #deck.remove_jokers()                   # delete joker cards from deck
    
    # some flags to track deck/card state
    incard = False                          # is cursor within bounds of a card
    insprite = None                         # sprite/card being moved
    hoversprite = None                      # sprite/card being hovered over
    dragging = False                        # is card being dragged
    mousedown = False                       # mouse is down
    (mx, my) = (0, 0)                       # track mouse position
    
    grid_size = 12                          # set to 1 for no snapping
    selrect = None
    
    # main game loop
    while 1:
        #pygame.time.delay(30)
        for event in pygame.event.get():
            # when window is closed or escape key pressed, exit main function
            if (event.type == QUIT or 
                (event.type == KEYUP and event.key == K_ESCAPE)):
                return 0
            # when mouse is moving
            elif event.type == pygame.MOUSEMOTION:
                (mx, my) = event.pos
                fx = round(mx / grid_size) * grid_size
                fy = round(my / grid_size) * grid_size
                if insprite and dragging:
                    insprite.rect.centerx = fx
                    insprite.rect.centery = fy
                    insprite.rect.clamp_ip((10,10,600,600))
                else:
                    for sprite in deck.sprites():
                        # grab the first card in the list being hovered
                        if sprite.rect.collidepoint(mx, my) and not dragging:
                            incard = True
                            hoversprite = sprite
                            selstart = None
                            selrect = None
                            break
                        # otherwise nothing is being hovered
                        else:
                            incard = False
                            insprite = None
                            hoversprite = None
                                
                            
            # when a mouse button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mx, my) = event.pos
                mousedown = True
                selstart = (mx,my)
                selrect = None
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
        
        draw_deck(screen,deck)
        if insprite:
            draw_status_area(screen,mx,my, grid_size,insprite,None)
        elif hoversprite:
            draw_status_area(screen,mx,my, None,None,hoversprite)
        else:
            draw_status_area(screen,mx,my,None,None,None)
        # draw a box around the card being hovered
        if hoversprite:
            pygame.draw.rect(screen,(183,183,183),hoversprite.rect.inflate(4,4),1)
        if insprite:
            pygame.draw.rect(screen,(255,0,0),insprite.rect.inflate(4,4),1)
            
        pygame.display.flip()

def draw_deck(screen,deck):
    # Create a font
    font = pygame.font.Font(None, 18)

    # Render the text
    text = font.render('Deck of Cards', True, (255, 255, 255))

    # Create a rectangle
    textRect = text.get_rect()

    # Center the rectangle
    textRect.top = 12
    textRect.left = 12
    
    deck.deck_rectangle = (10,10,720,98)
    
    pygame.draw.rect(screen, (255,255,255), (10,10,702,98), 1)

    # Blit the text
    screen.blit(text, textRect)

def draw_status_area(screen, mx, my, grid_size,card,hovercard):
    font = pygame.font.Font(None,16)
    
    text_status_title = font.render('STATUS:', True, (255,255,255))
    text_status_rect = text_status_title.get_rect()
    text_status_rect.top = 500
    text_status_rect.left = 10
    
    text_mouse = font.render('Mouse Position: ' + str(mx) + ' x ' + str(my), True, (255,255,255))
    text_mouse_rect = text_mouse.get_rect()
    text_mouse_rect.top = 520
    text_mouse_rect.left = 10

    if card:
        suitname = CardSuits.get_suit_name(card.get_suit())
        valuename = CardValues.get_value_name(card.get_value())
        text_card_val = font.render('Card: ' + valuename + ' of ' + suitname, True, (255,255,255))
        text_card_val_rect = text_card_val.get_rect()
        text_card_val_rect.top = 540
        text_card_val_rect.left = 10
        screen.blit(text_card_val, text_card_val_rect)

    if hovercard:
        suitname = CardSuits.get_suit_name(hovercard.get_suit())
        valuename = CardValues.get_value_name(hovercard.get_value())
        text_card_val = font.render('Card: ' + valuename + ' of ' + suitname, True, (255,255,255))
        text_card_val_rect = text_card_val.get_rect()
        text_card_val_rect.top = 540
        text_card_val_rect.left = 10
        screen.blit(text_card_val, text_card_val_rect)
    
    if grid_size:
        fx = int(round(mx / grid_size) * grid_size)
        fy = int(round(my / grid_size) * grid_size)
        
        text_card_pos = font.render('Card Position: ' + str(fx) + ' x ' + str(fy), True, (255,255,255))
        text_card_pos_rect = text_card_pos.get_rect()
        text_card_pos_rect.top = 560
        text_card_pos_rect.left = 10
        screen.blit(text_card_pos, text_card_pos_rect)
    
    
    screen.blit(text_status_title, text_status_rect)
    screen.blit(text_mouse, text_mouse_rect)

if __name__ == '__main__': main()
