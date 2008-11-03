import Enemy;
from EnemyPath import *;
class Data:
    #Singleton
    instance = None;
    def __init__(self):
        #Data members
        self.__groups = [];
        self.__paths = [];
        self.__currentFormation = None;
        self.__monsters = [];
    def getMonster(self,i):
        return self.__monsters[i];
    
    def newMonster(self,life,size,position):
        monster = Enemy.Enemy(life,size,position);
        self.__monsters.append(monster);
    
    def deleteMonster(self,index):
        self.__monsters.pop(index);
    
    def getNbMonster(self):
        return len(self.__monsters);
    def newGroup(self,enemies):
        group = Enemy.Group();
        for e in enemies:
            group.AddEnemy(e);
        self.__groups.append(group);
        return group;
    def deleteGroup(self,i):
        self.__groups.pop(i);
    def getGroup(self,i):
        return self.__groups[i];
    
    def getNbGroups(self):
        return len(self.__groups);
    
    def setCurrentFormation(self,i):
        self.__currentFormation = self.getFormation(i);
        
    def getCurrentFormation(self):
        return self.__currentFormation;
    
    def newEnemyPath(self,effect,speed,timeBeetweenEnemies):
        path = EnemyPath(effect,speed,timeBeetweenEnemies);
        self.__paths.append(path);
        return path;
    def getEnemyPath(self,index):
        return self.__paths[index];
    def getNbEnemyPath(self):
        return len(self.__paths);
    def deleteEnemyPathByIndex(self,index):
        self.__paths.pop(index);
    def deleteEnemyPath(self,path):
        k=0;
        for i in self.__paths:
            if(i == path):
                self.__paths.pop(k);
            k = k + 1;
    @classmethod    
    def getInstance(cls):
        if(cls.instance is None):
            cls.instance = Data();
        return cls.instance;