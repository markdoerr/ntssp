# -*- coding: utf8 -*-
from Affichage.display import *
from Jeu.jeu import *
def input(events): 
   for event in events: 
      if event.type == pygame.QUIT: 
         sys.exit(0) 
      else:
         pass 
         #print event 
class App:
    singleton=None
    def __init__(self):
        App.singleton=self
        pygame.init()
        self.display = Display()
        self.jeu = Jeu(self.display)
    def mainLoop(self):
        while True:
            self.jeu.update()
            self.display.flip()
    @classmethod
    def getSingleton(cls):
        if(cls.singleton is None):
            App()
        return cls.singleton