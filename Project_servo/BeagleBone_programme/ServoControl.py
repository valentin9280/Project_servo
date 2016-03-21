import PWMcontrol
import laser
import figure
import AngleServo

class ServoControl:
    def __init__(self):
        PWM.activatePWM()
        self.figure = Figure(self)
        self.servoHorizontal = AngleServo("P8_13")      #GPIO 23
        self.servoVertical = AngleServo("P8_29")     #GPIO 22
        self.laser = laser(46)              #GPIO 46
       
    
    def AngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.Angle(angleHorizontal)
    
    def AngleVertical(self, angleVertical):
        self.servoVertical.Angle(angleVertical)