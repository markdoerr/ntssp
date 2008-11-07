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
    
    def updateIds(self,vect):
        i = 0;
        for v in vect:
            v.id = i;
            i = i+1;
    def newMonster(self,life,size,position):
        monster = Enemy.Enemy(life,size,position);
        self.__monsters.append(monster);
        self.updateIds(self.__monsters);
    
    def deleteMonster(self,index):
        monster = self.__monsters.pop(index);
        groups = self.getGroupsForEnemy(monster);
        for group in groups:
            groups.DeleteEnemy(monster);
        self.updateIds(self.__monsters);
    
    def getNbMonster(self):
        return len(self.__monsters);
    def newGroup(self,enemies):
        group = Enemy.Group();
        for e in enemies:
            group.AddEnemy(e);
        self.__groups.append(group);
        self.updateIds(self.__groups);
        return group;
    def deleteGroup(self,i):
        self.__groups.pop(i);
        self.updateIds(self.__groups);
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
        self.updateIds(self.__paths);
        return path;
    def getGroupsForEnemy(self,enemy):
        groups=[];
        for group in self.__groups:
            if(groups.ContainsEnemy(enemy)):
                groups.append(group);
        return groups;
    def getGroupsForPath(self,path):
        groups=[];
        for group in self.__groups:
            if(group.ContainsPath(path)):
                groups.append(group);
        return groups;
    def getEnemyPath(self,index):
        return self.__paths[index];
    def getNbEnemyPath(self):
        return len(self.__paths);
    def deleteEnemyPathByIndex(self,index):
        path = self.__paths.pop(index);
        groups = self.getGroupsForPath(path);
        for group in groups:
            groups.DeleteEnemy(path);
        self.updateIds(self.__paths);
    def deleteEnemyPath(self,path):
        self.__paths.remove(path);
        groups = self.getGroupsForPath(path);
        for group in groups:
            groups.DeleteEnemy(path);
        self.updateIds(self.__paths);
    @classmethod    
    def getInstance(cls):
        if(cls.instance is None):
            cls.instance = Data();
        return cls.instance;