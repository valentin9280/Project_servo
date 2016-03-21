import laser
import figure


class traitement_protocole():
		def __init___(self):
			pass

			def traitement_trame(data):
				command = data[0]
				octet1 = data[1]
				octet2 = date[2]

				if command == 49:
					self.MoveMoteur(octet1 , octet2)	
				elif command == 50:
					if octet1 == 49:
						self.laser.laserOFF()
					elif octer2 == 50:
						self.laser.LaserON()
				elif command == 51:
				     if octet1 == 49:
				     	self.figure.DessinerCarre()
				     elif octet1 == 50:
				     	self.figure.DessinerCercle()
				     elif octet1 == 51:
				     	self.figure.DessinerTriangle()
				elif command == 52:
						self.figure.init()



