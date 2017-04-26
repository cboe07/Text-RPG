from Monster import Monster
class Demon(object):
	def __init__(self):
		super(Demon,self).__init__("Demon")
		self.health = 15
		self.power = 4
		self.name = "Demon"
		self.xp_value = 10

	def take_damage(self, damage):
		self.health -=damage

	def is_alive(self):
		return self.health > 0