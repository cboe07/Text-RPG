class Hero(object):
	def __init__(self, name = "Incognito"):
		self.name = name
		self.health = 15
		self.power = 5
		self.max_health = self.health
		self.xp = 0
		self.level = 1

	def check_level(self):
		if self.xp > 3:
			self.level = 2
			self.level_up()

	def level_up(self):
		print "Thou hast leveled up %s! Thy hp is now %d and thy power is now %d" %(self.name, self.max_health, self.power)
		self.max_health += 10
		self.heath = self.max_health
		self.power += 5


	def cheer_hero(self):
		print "Fight hard, %s" % self.name

	def is_alive(self):
		return (self.health > 0)
		# if(self.health > 0):
		# 	return True
		# else:
		# 	return False

	def attack(self, who_to_attack):
		who_to_attack.health -= self.power

	def increased_health(self, amount):
		self.health += amount 
		if self.health > self.max_health:
			self.health = self.max_health

	
