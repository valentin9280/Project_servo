
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
						self.Laser("OFF")
					elif octer2 == 50:
						self.Laser("ON")
				elif command == 51:
				     if octet1 == 49:
				     	self.Dessiner("carre")
				     elif octet1 == 50
				     	self.Dessiner("cercle")
				     elif octet1 == 51
				     	self.Dessiner("triangle")
				elif command == 52:
						self.init()

						
			def MoveMoteur(self,sens1,sens2):
				self.MoveMoteur(sens1,sens2)

			def Laser
				self.Laser(etat)

			def Dessiner
				self.Dessiner(forme)

			def init
				self.init()




