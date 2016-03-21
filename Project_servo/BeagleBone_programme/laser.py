import os
import time

class Laser:
	def __init__(self,pin):
		self.pin=pin
		os.system("echo "+str(pin)+" > /sys/class/gpio/export")
		time.sleep(1)
		os.system("echo out > /sys/class/gpio/gpio"+str(self.pin)+"/direction")
		time.sleep(1)
		os.system("echo 0  > /sys/class/gpio/gpio"+str(self.pin)+"/value")
		pass

	def LaserON(self):
		os.system("echo 1  > /sys/class/gpio/gpio"+str(self.pin)+"/value")
		pass

	def LaserOFF(self):
		os.system("echo 0 > /sys/class/gpio/gpio"+str(self.pin)+"/value")
		pass