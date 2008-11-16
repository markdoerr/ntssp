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
        if(i>=0 and i<len(self.__monsters)):
           return self.__monsters[i];
        return None;
    def newMonster(self,life,size,position):
        monster = Enemy.Enemy(life,size,position);
        self.__monsters.append(monster);
    
    def deleteMonster(self,index):
        monster = self.__monsters.pop(index);
        groups = self.getGroupsForEnemy(monster);
        for group in groups:
            groups.DeleteEnemy(monster);
    
    def getNbMonster(self):
        return len(self.__monsters);
    def newGroup(self,enemies,effectType,speed,diffTime):
        group = Enemy.Group(effectType,speed,diffTime);
        for e in enemies:
            group.AddEnemy(e);
        self.__groups.append(group);
        return group;
    def deleteGroup(self,i):
        self.__groups.pop(i);
    #TODO change this
    def getGroups(self):
        return self.__groups;
    def getGroup(self,i):
        if(i >= 0 and i < len(self.__groups)):
           return self.__groups[i];
        else:
            return None;
    
    def getNbGroups(self):
        return len(self.__groups);
    
    def setCurrentFormation(self,i):
        self.__currentFormation = self.getFormation(i);
        
    def getCurrentFormation(self):
        return self.__currentFormation;
    
    def newEnemyPath(self):
        path = EnemyPath();
        self.__paths.append(path);
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
    def GroupUp(self,group):
        index = self.__groups.index(group);
        if(index > 0):
            tmp = self.__groups[index-1];
            self.__groups[index-1] = group;
            self.__groups[index] = tmp;
            return index - 1;
        return index;
    def GroupDown(self,group):
        index = self.__groups.index(group);
        if(index < self.getNbGroups()-1):
            tmp = self.__groups[index+1];
            self.__groups[index+1] = group;
            self.__groups[index] = tmp;
            return index + 1;
        return index;
    def getEnemyPath(self,index):
        if(index >= 0 and index < len(self.__paths)):
            return self.__paths[index];
        return None;
    def getNbEnemyPath(self):
        return len(self.__paths);
    def deleteEnemyPathByIndex(self,index):
        path = self.__paths.pop(index);
        groups = self.getGroupsForPath(path);
        for group in groups:
            group.DeletePath(path);
    def deleteEnemyPath(self,path):
        self.__paths.remove(path);
        groups = self.getGroupsForPath(path);
        for group in groups:
            group.DeletePath(path);
    @classmethod    
    def getInstance(cls):
        if(cls.instance is None):
            cls.instance = Data();
        return cls.instance;