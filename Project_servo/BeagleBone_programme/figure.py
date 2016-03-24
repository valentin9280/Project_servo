import time
import math
from AngleServo import angleServo
import ServoControl

class Figure:
    def __init__(self):
        self.zeroHorizontal = -90;
        self.zeroVertical = -90;
	self.ServoControl =ServoControl.servoControl()
        pass
    
    def DessinerCercle(self):
        for nb in range(0, 5):
            for f in range(0, 360, 5):
                angle = f * 2 * math.pi / 360.0
                self.AngleServo.Angle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)

    def DeplacerVers(self, X, Y):
        self.ServoControl.AngleHorizontal(X + self.zeroHorizontal)
        self.ServoControl.AngleVertical(Y + self.zeroVertical)

    def init(self):
        self.DeplacerVers(0 , 0)

    def Position(self):
        return self.Angle_info() - self.zeroHorizontal , self.Angle_info() - self.zeroVertical

    def DeplacerDe(self,X,Y):
        pos = self.Position()
        self.DeplacerVers(pos[O]+X , pos[1] + Y)

    def line(self, X ,Y):
        Xpos = int(self.Position())
        Ypos = int(self.Position())
        res = math.sqrt((X -Xpos)**2 + (Y - Ypos)**2)
        for i in range (0,int(res)):
            a = i
            if i > res:
                a = res
            self.DeplacerVers(int((Xpos - X)-res*a) , int((Ypos - Y)/res*a))
    
    def DessinerCarre(self):
        for nb in range(0, 5):
            self.DeplacerVers(50, 50)
            self.line(50, 90)
            self.line(90, 90)
            self.line(90, 50)
            self.Line(50, 50)

    def DessinerTriangle(self):
        for nb in range(0,4):
            self.DeplacerVers()
        pass
