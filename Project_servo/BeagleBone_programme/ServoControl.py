from servo import *
from shape import *
from led import *
import PWMcontrol
import laser
import figure
import AngleServo

class Turret:
    def __init__(self):
        pwm.activatePWM()
        elf.figure = Dessiner(self)
        self.servoBas = Servo("P8_13")      #GPIO 23
        self.servoHaut = Servo("P8_29")     #GPIO 22
        self.laser = laser(46)              #GPIO 46
       
        
    def setAngle(self, angleVertical, angleHorizontal):
        self.servoVertical.setAngle(angleVertical)
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.setAngle(angleHorizontal)
    
    def setAngleVertical(self, angleVertical):
        self.servoVertical.setAngle(angleVertical)
    
    def addAngleVertical(self, angleVertical):
        self.servoVertical.setAngle(angleVertical + self.servoVertical.getAngle())

    def addAngleHorizontal(self, angleHorizontal):
        self.servoHorizontal.setAngle(angleHorizontal + self.servoHorizontal.getAngle())

    def draw(self, forme):
        self.turnOnLaser()
        if forme == "square":
            self.shape.drawSquare()
        elif forme == "circle":
            self.shape.drawCircle()
        elif forme == "spiral":
            self.shape.drawSpiral()
        self.turnOffLaser()
            
    def turnOnLaser(self):
        self.laser.turnOn()
    
    def turnOffLaser(self):
        self.laser.turnOff()