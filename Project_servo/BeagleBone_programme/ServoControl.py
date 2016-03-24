import PWMcontrol
import laser
import figure
import AngleServo

class servoControl:
    def __init__(self):
        PWMcontrol.activatePWM()
        self.servoHorizontal =AngleServo.angleServo("P9_14")      #GPIO 23
        self.servoVertical = AngleServo.angleServo("P8_13")     #GPIO 22
       
    
    def AngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.Angle(angleHorizontal)
    
    def AngleVertical(self, angleVertical):
        self.servoVertical.Angle(angleVertical)
