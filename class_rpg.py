from Hero import Hero
# from Goblin import Goblin
# from Vampire import Vampire
# from Demon import Demon
from Monster import Goblin
from Monster import Hobgoblin
from Monster import Vampire
from Monster import Demon



from random import randint

hero_name = raw_input("What is thy name, brave adventurer?")
the_hero = Hero(hero_name)
# the_hero.cheer_hero()
print "How many monsters are you willing to fight?"
number_of_enemies = int(raw_input("> "))

monsters_objects = []
monsters_objects.append(Goblin())
monsters_objects.appens(Hobgoblin())
monsters_objects.append(Vampire())
monsters_objects.append(Demon())

monsters = []
for i in range(0, number_of_enemies):
	rand = randint(0, len(monsters_objects) - 1)
	monsters.append(monsters_objects[rand])

for monster in monsters:
	print "Brave %s, you have encountered a %s." % (the_hero.name, monster.name)
	#Run game as long as BOTH characters have health
	while monster.health > 0 and the_hero.is_alive():
		print "Your HEALTH: %d and POWER: %d" % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. Fight %s" % monster.name
		print "2. Do nothing"
		print "3. Flee"
		print "4. Drink potion of life"
		print "> ",
		user_input = raw_input()
		if (user_input == "1"):
			#Hero is going to attack
			# the_goblin.health -= the_hero.power
			# the_hero.attack(the_goblin)
			monster.take_damage(the_hero.power)

			print "You have done %d damage to the %s" % (the_hero.power, monster.name)
			if monster.health <= 0:
				print "You have defeated the %s!" % monster.name
				the_hero.xp += monster.xp_value
				the_hero.check_level
		elif user_input == "2":
				#Hero is going to do nothing
				pass
		elif user_input == "3":
			print "Goodbye, coward"
			break
		elif user_input == "4":
			the_hero.increased_health(20)
			print "You have found a potion!"
		else:			
			print "Invalid input %s" % user_input

		if monster.health > 0:
				# hero has attacked (or not) AND goblin is still alive			
			the_hero.health -= monster.power
			print "The %s hits you for %d damage" % (monster.name, monster.power)
			if the_hero.health <= 0:
				print "You have been killed by the %s." % monster.name
		if the_hero.health > 0 and the_hero.health < 5:
			print "You have gone into a rage. Your power has increased!"
			the_hero.power += 5





