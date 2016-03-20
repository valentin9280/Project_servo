import serial
import os
import time

def writeFile(fichier, data):
    f = open(fichier, 'w')
    f.write(data)
    time.sleep(0.01)
    f.close()

def readFile(fichier):
    f = open(fichier, 'r')
    data = f.read()
    time.sleep(0.01)
    f.close()
    return data

def activePWM():
	os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.8/slots")
    time.sleep(2)

    class PWM:
    def __init__(self, channel, duty, period):
        os.system("echo bone_pwm_"+channel+" > /sys/devices/bone_capemgr.8/slots")
        time.sleep(2)
        self.name = self.getNameChannel(channel)
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/pwm_test_"+channel+"/period")
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/pwm_test_"+channel+"/duty")
        time.sleep(1)
        writeFile("/sys/devices/ocp.3/pwm_test_"+channel+"/run", str(1))
        
    def set_duty(self, duty):
        writeFile("/sys/devices/ocp.3/pwm_test_"+channel+"/duty", str(duty))

    def set_period(self, period):
        writeFile("/sys/devices/ocp.3/pwm_test_"+channel+"/period", str(period))

    def set_polarity(self, polarity):
        writeFile("/sys/devices/ocp.3/pwm_test_"+channel+"/polarity", str(polarity))
        
    def get_duty(self):
        return readFile("/sys/devices/ocp.3/pwm_test_"+channel+"/duty")
        
    def get_period(self):
        return readFile("/sys/devices/ocp.3/pwm_test_"+channel+"/period")
