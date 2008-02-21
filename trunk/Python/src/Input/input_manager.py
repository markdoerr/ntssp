# -*- coding: utf8 -*-
import pygame
import pygame.event
import sys
def scan():
   events = pygame.event.get()
   for event in events: 
      if event.type == pygame.QUIT: 
         sys.exit(0) 