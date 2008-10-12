class EffectType:
    Circle = 0;
    Switch = 1;
    Rotate = 2;
    Arc = 3;
    Zero = 4;

MAX_POINTS = 10000;
MAX_ENEMIES_IN_FORMATION=20;
OUT_SCREEN = (-500,-500);
class EnemyPath:
    def __init__(self,effect = EffectType.Zero,BezierSpline,speed,timeBeetweenEnemies):
        self.effect = effect;
        self.BezierSpline = BezierSpline;
        self.speed = speed;
        self.timeBeetweenEnemies = timeBeetweenEnemies;
        self.__t = 0;
        self.__max = int(MAX_POINTS/self.speed);
        self.__lastEnemy=0;
        self.__interTime=0;
    #num (enemy number in the formation )
    def getNextPoint(self,num):
        next = OUT_SCREEN;
        if(num <= self.__lastEnemy):
            next = self.BezierSpline.getPoint(self.__t,self.__max);
            self.__t = self.__t + 1;
        self.__interTime = self.__interTime + 1;
        if(self.__interTime == self.timeBeetweenEnemies):
            self.__lastEnemy = max(self.__lastEnemy + 1,MAX_ENEMIES_IN_FORMATION);
        return next;


class CirclePath(EnemyPath):
    def __init__(self):
        return;

class SwitchPath(EnemyPath):
    def __init__(self):
        return;

class RotatePath(EnemyPath):
    def __init__(self):
        return;
    
class ArcPath(EnemyPath):
    def __init__(self):
        return;