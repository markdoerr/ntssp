from Jeu.script import *
from Xml.handlers import *
class BombScript(Script):
    script=None
    def __init__(self,t,perso,app):
        super(BombScript,self).__init__(t[0],t[1])
        self.perso = perso
        self.started=False
        self.sprites[0].surfaces[12:14]=self.sprites[0].surfaces[12:14]*5
        self.first=True
        self.app = app
        self.sprites[0].setCoord(self.perso.side.left+(self.perso.side.width-self.sprites[0].display_rect.width)/2,self.perso.side.top+(self.perso.side.height-self.sprites[0].display_rect.height)/2)
    def update(self):
       if(self.first):
           self.__n=0
           self.app.jeu.stage.background.setBrightEffectAll(60,60,60)
           self.sons[0].play()
           self.first=False
       if(self.__n==1):
           self.app.jeu.stage.background.resetAll()
           self.app.jeu.stage.background.setBrightEffectAll(80,80,80)
       self.sprites[0].update()
       self.started = not (self.sprites[0]).end()
       if(not self.started):
           self.app.jeu.stage.background.resetAll()
       self.__n+=1
    def start(self):
        if(not self.started):
            self.first=True
            self.started=True
    @classmethod
    def getSingleton(cls,app,perso):
       if(cls.script is None):
           sc = getScriptFromXML("F:\Twinkle Star Sprites\Python\data\Persos\LoadRan\Scripts\BombScript.xml",app.display.backbuffer)
           bs = BombScript(sc,perso,app)
           cls.script=bs
       return cls.script

def newScript(app,perso):
    bs=BombScript.getSingleton(app,perso)
    bs.start()
def update():
    if(BombScript.script is not None and BombScript.script.started):
        BombScript.script.update()
def load(app,perso):
    BombScript.getSingleton(app,perso)
def isActive():
    return BombScript.script is not None and BombScript.script.started