import serial
import os
import time

class Laser:
	def __ini__(self,pin,value):
		os.system("echo "+str(pin)+" > /sys/class/gpio/export")
        time.sleep(2)
        os.system("echo out > /sys/class/gpio/gpio"+str(pin)+"/direction");
        time.sleep(2)
        os.system("echo " + str(value) + " > /sys/class/gpio/gpio"+str(pin)+"/value");

    def LaserOFF(self):
    	os.system("echo " + 0 + " > /sys/class/gpio/gpio"+str(pin)+"/value");

    def LaserON(self):
    	os.system("echo " + 1 + " > /sys/class/gpio/gpio"+str(pin)+"/value");