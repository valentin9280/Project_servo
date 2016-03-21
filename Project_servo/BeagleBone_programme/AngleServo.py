from PWMcontrol import *

class angleServo:
    def __init__(self, broche):
        self.PWM = PWM(broche, 1500000, 200000000)
        self.PWM.duty(1500000)
        self.PWM.period(20000000)


    def Angle(self, angle):
        if angle >= -90 or angle <= 90:
            d = (angle + 90) * (1000000 / 180) + 1000000
            self.PWM.duty(d)

    def Angle_info(self):
        d = int(self.PWM.duty_info())
        angle = (d - 1000000) / (1000000 / 180) - 90
        return angle