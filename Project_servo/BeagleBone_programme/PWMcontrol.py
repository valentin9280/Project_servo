import serial
import os
import time


def activePWM():
    os.system("echo am33xx_pwm > /sys/devices/bone_capemgr.8/slots")
    time.sleep(2)

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


class PWM:
    def __init__(self, broche, duty, period):
        os.system("echo bone_pwm_"+broche+" > /sys/devices/bone_capemgr.8/slots")
        time.sleep(2)
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/pwm_test_"+broche+"/period")
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/pwm_test_"+broche+"/duty")
        time.sleep(1)
        writeFile("/sys/devices/ocp.3/pwm_test_"+broche+"/run", str(1))
        
    def duty(self, duty):
        writeFile("/sys/devices/ocp.3/pwm_test_"+broche+"/duty", str(duty))
        
    def duty_info(self):
        return readFile("/sys/devices/ocp.3/pwm_test_"+broche+"/duty")

    def period(self, period):
        writeFile("/sys/devices/ocp.3/pwm_test_"+broche+"/period", str(period))
        
