import time
import math
import AngleServo

class Figure:
    def __init__(self, i):
        self.i = i
        self.zeroHorizontal = -90;
        self.zeroVertical = -90;
        pass
    
    def DessinerCercle(self):
        for nb in range(0, 5):
            for f in range(0, 360, 5):
                angle = f * 2 * math.pi / 360.0
                self.i.Angle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)

    def DeplacerVers(self, X, Y):
        self.i.AngleHorizontal(X + self.zeroHorizontal)
        self.i.AngleVertical(Y + self.zeroVertical)

    def init(self):
        self.DeplacerVers(0 , 0)

    def Position(self):
        return self.i.servoHorizontal.Angle_info() - self.zeroHorizontal , self.i.servoVertical.Angle_info() - self.zeroVertical

    def DeplacerDe(self,X,Y):
        pos = self.Position()
        self.DeplacerVers(pos[O]+X , pos[1] + Y)

    def line(self, X ,Y):
        Xpos = int(self,Position())
        Ypos = int(self,Position())
        res = math.sqrt((X -Xpos)**2 + (Y - Ypos)**2)
        for i in range (0,int(res)):
            a = i
            if i > res:
                a = res
            self.DeplacerVers(int((Xpos - X)-res*a) , int((Ypos - Y)/res*a))
    
    def DessinerCarre(self):
        for nb in range(0, 5):
            self.DeplacerVers(50, 50)
            self.Line(50, 90)
            self.Line(90, 90)
            self.Line(90, 50)
            self.Line(50, 50)

    def DessinerTriangle(self):
        for nb in range(0,4):
            self.DeplacerVers()
        pass