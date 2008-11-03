#simple Enemy class
class Enemy:
    #life (int), size(int), position (2-tuple of int correspond to x,y coord)
    def __init__(self,life,size,position):
        #Life from 1 to 5 correspond to certain color
        self.life = life;
        
        #Size from 1 to 5
        self.size = size;
        
        #Position
        self.x = position.x;
        self.y = position.y;
        
    def toString(self):
        return "Enemy : " + str(self.life) +", "+str(self.size);
        
class Group:
    def __init__(self):
        #table of enemies
        self.enemies = [];
        self.paths = [];
    def AddEnemy(self,enemy):
        self.enemies.append(enemy);
    def AddPath(self,path):
        self.paths.append(path);