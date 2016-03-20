import time
import math

class Dessiner:
    def __init__(self, t):
        self.t = t
        self.zeroH = -90;
        self.zeroV = -90;
        pass
    
    def DessinerCercle(self):
        for nb in range(0, 5):
            for f in range(0, 360, 5):
                angle = f * 2 * math.pi / 360.0
                self.t.setAngle(int(math.cos(angle) * 25.0), int(math.sin(angle) * 25.0))
                time.sleep(0.01)

    def moveTo(self, X, Y):
        self.t.setAngleHorizontal(X + self.zeroH)
        self.t.setAngleVertical(Y + self.zeroV)
        
    def moveFrom(self, X, Y):
        a = self.getPosition()
        self.moveTo(a[0] + X, a[1] + Y)
        
    def getPosition(self):
        return self.t.servoHorizontal.getAngle() - self.zeroH, self.t.servoVertical.getAngle() - self.zeroV
    
    def DessinerCarre(self):
        for nb in range(0, 5):
            self.moveTo(75, 75)
            self.drawLine(75, 105)
            self.drawLine(105, 105)
            self.drawLine(105, 75)
            self.drawLine(75, 75)

    def DessinerTriangle(self):
