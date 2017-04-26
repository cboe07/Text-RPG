class Monster(object):
	def __init__(self, name, health = 10):
		self.name = name
		self.health = health
		self.power = 5
		
	def take_damage(self, damage):
		self.health -=damage
	def is_alive(self):
		return self.health > 0

class Goblin(Monster):
	def __init__(self):
		super(Goblin,self).__init__("Goblin", 16)
		# self.health = 6
		self.power = 2
		self.name = "Goblin"
		self.xp_value = 5

	# def take_damage(self, damage):
	# 	self.health -=damage

	# def is_alive(self):
	# 	return self.health > 0

class Hobgoblin(Goblin):
	def __init__(self):
		super(Goblin, self).__init__()
		self.power = 3
		self.name = "Hobgoblin"

class Vampire(Monster):
	def __init__(self):
		super(Vampire, self).__init__("Vampire")
		self.health = 12
		self.power = 4
		self.name = "Vampire"
		self.xp_value = 10

class Demon(Monster):
	def __init__(self):
		super(Demon,self).__init__("Demon")
		self.health = 15
		self.power = 4
		self.name = "Demon"
		self.xp_value = 10




