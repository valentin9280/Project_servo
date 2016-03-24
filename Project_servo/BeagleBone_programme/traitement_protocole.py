from laser import *
from figure import *


class Traitement_protocole:
		def __init___(self):
				pass

		def traitement_trame(self,data):
				self.l = Laser()
				self.f = Figure()
				print("Running")
				command = ord(data[0])
				octet1 = ord(data[1])
				octet2 = ord(data[2])
				print(command)
				print(octet1)
				print(octet2)

				if command == 49:
					print("Move")
					if octet1 == 52:
						self.figure.init()
					elif octet1 == 49:
						angle1 = 0
					elif octet1 == 50:
						angle1 = 15
					elif octet1 == 51:
						ange1 = -15
					if octet2 == 49:
						angle2 = 0
					elif octet2 == 50:
						angle2 = 15
					elif octet2 == 51:
						angle2 = -15
					self.f.DeplacerDe(ange1,angle2)
				elif command == 50:
					if octet1 == 49:
						print("Laser OFF")
						self.l.LaserOFF()
				        elif octet1 == 50:
						print("Laser ON")
						self.l.LaserON()
				elif command == 51:
				     print("Figure")
				     if octet1 == 49:
				        self.f.DessinerCarre()
				     elif octet1 == 50:
				     	self.f.DessinerCercle()
				     elif octet1 == 51:
				     	self.figure.DessinerTriangle()


