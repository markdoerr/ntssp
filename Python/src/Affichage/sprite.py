# -*- coding: utf8 -*-
import pygame,pygame.rect
from Affichage.effect import *
from Constantes.DisplayConstantes import *
from Affichage.resourcecache import *
def loadImage(f):
    if(isinstance(f,pygame.surface.Surface)):
        return f
    return get_image(f).convert(8)
class Sprite(pygame.sprite.Sprite,DefaultEffects):
    def __init__(self,frames,screen,speed):
        pygame.sprite.Sprite.__init__(self)
        frames = [loadImage(f) for f in frames]
        for f in frames:
            f.set_colorkey(COLOR_KEY)
        DefaultEffects.__init__(self,frames)
        self.screen=screen
        self.currentFrame=0
        self.x=-500
        self.y=-500
        self.display_rect=frames[0].get_rect()
        self.rect=self.display_rect.inflate(-(self.display_rect.width-self.display_rect.width*0.80),-(self.display_rect.height-self.display_rect.height*0.80))
        self.rect.top=-500
        self.rect.left=-500
        self.display_rect.top=-500
        self.display_rect.left=-500
        self.__cdelay=0
        self.setSpeed(speed)
        self.changed=True
        self.container=None
        self.isEnd=False
        self.clippingArea=None
    def setContainer(self,o):
        self.container=o
    def setCoord(self,x,y):
        x = int(x)
        y = int(y)
        xo = x-self.x
        yo = y-self.y
        self.x=x
        self.y=y
        self.rect.move_ip(xo,yo)
        self.display_rect.move_ip(xo,yo)
    def setCoordCenter(self,x,y):
        x = x - self.display_rect.width/2
        y = y - self.display_rect.height/2
        self.setCoord(x,y)
    def setSpeed(self,fps):
        self.speed=fps
        self.__fdelay=float(FPS)/float(fps)
    def clone(self):
        return Sprite(self.surfaces,self.screen,self.speed)
    def updateFrame(self):
        self.isEnd=False
        if(self.__cdelay <= 0):
            self.__cdelay+=self.__fdelay
            self.currentFrame+=1
            self.changed=True
        self.__cdelay-=1
        if(self.currentFrame == len(self.surfaces)):
            self.currentFrame=0
            self.isEnd=True
    def end(self):
        return self.isEnd
    def setClippingArea(self,clippingArea):
        self.clippingArea=clippingArea
    def update(self):
        if(self.clippingArea is not None):
            r = self.display_rect.move(0,0)
            self.display_rect = self.display_rect.clip(self.clippingArea)
        else:
            r = self.display_rect
        self.changed=False
        self.screen.blit(self.surfaces[self.currentFrame],(self.display_rect.left,self.display_rect.top),pygame.rect.Rect(self.display_rect.left - self.x,self.display_rect.top-self.y,self.display_rect.width,self.display_rect.height))
        self.updateFrame()
        self.display_rect=r
    def __scale(self,width,height):
        surfs = []
        for f in self.surfaces:
            surfs.append(pygame.transform.scale(f,(width,height)))
        s = Sprite(surfs,self.screen,self.speed)
        s.currentFrame = self.currentFrame
        return s
    def scale(self,zoom):
        return self.__scale(self.display_rect.width*zoom,self.display_rect.height*zoom)
    def rotate(self,angle):
        surfs = []
        for f in self.surfaces:
            surfs.append(pygame.transform.rotate(f,angle))
        s = Sprite(surfs,self.screen,self.speed)
        s.currentFrame = self.currentFrame
        return s