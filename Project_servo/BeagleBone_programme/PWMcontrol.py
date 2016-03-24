import os
import time


def activatePWM():
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
	self.name_channel = self.nameChannel(broche)
        os.system("echo " + str(period) + " > /sys/devices/ocp.3/"+self.name_channel+"/period")
        os.system("echo " + str(duty) + " > /sys/devices/ocp.3/"+self.name_channel+"/duty")
        time.sleep(1)
        writeFile("/sys/devices/ocp.3/"+self.name_channel+"/run", str(1))
        
    def duty(self, duty):
        writeFile("/sys/devices/ocp.3/"+self.name_channel+"/duty", str(duty))
        
    def duty_info(self):
        return readFile("/sys/devices/ocp.3/"+self.name_channel+"/duty")

    def period(self, period):
        writeFile("/sys/devices/ocp.3/"+self.name_channel+"/period", str(period))
        
    def nameChannel(self,broche):
	a = os.popen("ls /sys/devices/ocp.3 | grep pwm_test_"+broche)
	return a.read()[:-1]
