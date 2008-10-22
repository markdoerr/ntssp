#simple Enemy class
class Enemy:
    #life (int), size(int), position (2-tuple of int correspond to x,y coord)
    def __init__(self,life,size,position,enemyPaths):
        #Life from 1 to 5 correspond to certain color
        self.life = life;
        
        #Size from 1 to 5
        self.size = size;
        
        #Position
        self.x = position[0];
        self.y = position[1];
        
        self.enemyPaths = enemyPaths;
        
    def toString(self):
        return "Enemy : " + str(self.life) +", "+str(self.size);
        
class Formation:
    def __init__(self):
        #table of enemies
        self.enemies = [];
    
    def animate(self):
        num = 0;
        for enemy in self.enemies:
            #this enemy finished
            if(len(enemy.enemyPaths) == 0):
                num = num + 1;
                continue;
            
            coord = None;
            while(coord is None):              
                coord = enemy.enemyPaths[0].getNext(num);
                
                #Current path end
                if(coord is None):
                    enemy.enemyPaths.pop(0);
            
            enemy.x = coord[0];
            enemy.y = coord[1];
            num = num + 1;