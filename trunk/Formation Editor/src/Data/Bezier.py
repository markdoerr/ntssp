#Simple point class
class Point:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def __eq__(self,o):
        return o.x == self.x and o.y == self.y;
            
        
#Cubic Bezier Curve
class CubicBezier:
    def __init__(self,p1,p2,p3,p4):
        self.points = [];
        self.points.append(p1);
        self.points.append(p2);
        self.points.append(p3);
        self.points.append(p4);
    #returns (x,y) tuple (-1,-1) if error
    def getPoint(self,t):
        x=-1
        y=-1
        if(t >= 0 and t <= 1):
            #Square
            t2 = t*t;
            #Cube
            t3 = t2*t;
            
            #Coeff 
            a = (-t3+3*t2-3*t+1);
            b = (3*t3-6*t2+3*t);
            c = (3*t2-3*t3);
            d = t3;
            
            #calcul
            x = a * self.points[0].x + b * self.points[1].x + c * self.points[2].x + d * self.points[3].x; 
            y = a * self.points[0].y + b * self.points[1].y + c * self.points[2].y + d * self.points[3].y; 
        
        return (x,y)
    
class BezierSpline:
    def __init__(self):
        self.__curves=[];
    
    def getCurveCount(self):
        return len(self.__curves);
    def getCurve(self,index):
        if(index >= 0 and index < self.getCurveCount()):
            return self.__curves[index];
        return None;
    #if last point of the spline does not match with the first of c add nothing
    def addCurve(self,c):
        #Not first Curve
        if(len(self.__curves)>0):
            if(self.__curves[-1].points[-1] != c.points[0]):
                return;
        self.__curves.append(c);
    #t from 0 to max, returns (x,y)
    def getPoint(self,t,max):
        c = max/len(self.__curves);
        n = int(t / c);
        return self.__curves[n].getPoint(t);