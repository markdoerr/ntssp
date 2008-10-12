import Enemy;
class Data:
    #Singleton
    instance = None;
    def __init__(self):
        #Data members
        self.__formations = [];
        self.__currentFormation = None;
        
    def newFormation(self):
        form = Enemy.Formation();
        self.__formations.append(form);
        if(len(self.__formations) == 1):
            self.setCurrentFormation(0);
        return form;
    
    def getFormation(self,i):
        return self.__formations[i];
    
    def getNbFormation(self):
        return len(self.__formations);
    
    def setCurrentFormation(self,i):
        self.__currentFormation = self.getFormation(i);
        
    def getCurrentFormation(self):
        return self.__currentFormation;
    
    @classmethod    
    def getInstance(cls):
        if(cls.instance is None):
            cls.instance = Data();
        return cls.instance;