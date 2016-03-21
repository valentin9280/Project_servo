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
					if octet1 == 52:
						self.figure.init()
					elif octet1 == 49:
					angle1 = 0
					elif octet1 == 50:
					angle1 = 15
					elif octet1 == 51:
					ange1 = -15
					if octer2 == 49:
					angle2 = 0
					elif octet2 == 50:
					angle2 = 15
					elif octet2 == 51
					angle2 = -15
					self.figure.sDeplacerDe(ange1,angle2)

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
						



