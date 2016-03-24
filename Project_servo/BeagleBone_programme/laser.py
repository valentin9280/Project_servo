import os
import time

class Laser:
	def __init__(self):
		os.system("echo 26 > /sys/class/gpio/export")
		time.sleep(1)
		os.system("echo out > /sys/class/gpio/gpio26/direction")
		time.sleep(1)
		os.system("echo 0  > /sys/class/gpio/gpio26/value")
		pass

	def LaserON(self):
		os.system("echo 1  > /sys/class/gpio/gpio26/value")
		pass

	def LaserOFF(self):
		os.system("echo 0 > /sys/class/gpio/gpio26/value")
		pass
