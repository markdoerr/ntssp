# -*- coding: utf8 -*-
import pygame, sys,os
from Affichage.effect import *
from Affichage.resourcecache import *
class Background(DefaultEffects):
    def __init__(self,image,screen):
        self.back_surface = get_image(image).convert(8)
        surfs=[]
        surfs.append(self.back_surface)
        DefaultEffects.__init__(self,surfs)
        self.screen = screen
        self.rects=[]
        self.y = 0
    def scroll(self):
        self.rects=[]
        if(self.y <= -240):
            self.y = self.back_surface.get_height() + self.y
        if(self.y < 0):
            r = pygame.Rect(0,0,320,0)
            r.y = self.back_surface.get_height() + self.y
            r.height = self.back_surface.get_height() - r.y
            self.rects.append(r)
            r1 = pygame.Rect(0,0,320,240-r.height)
            self.rects.append(r1)
        else:
            r = pygame.Rect(0,self.y,320,240)
            self.rects.append(r)
        self.y = self.y - 3
    def update(self):
        self.scroll()
        height = 0
        for r in self.rects:
            self.screen.blit(self.back_surface,(0,height),r)
            height += r.height 
if __name__ == '__main__':
    # Import Psyco if available
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass