import random, time
from pprint import pprint

names = ['Joe', 'George', 'Kong', 'Coco', 'Larry', 'Curly', 'Moe', 'Shemp', 'Aaron', 'Antione', 'Ayako', 'Carmelo', 'Dario', 'Davis', 'Deane', 'Dot', 'Earle', 'Emilio', 'Eugene', 'Guillermo', 'Hank', 'Ina', 'Jaime', 'Jerrold', 'Jorge', 'Jude', 'Leonore', 'Lourdes', 'Manny', 'Marvin', 'Nagan', 'Ross', 'Sanford', 'Tiny', 'Tom', 'Carlton', 'Raymundo', 'Antone', 'Adolfo', 'Joel', 'Dana', 'Rigoberto', 'Jeff', 'Humberto', 'Mohammed', 'Billie', 'Derrick', 'Rey', 'Wes', 'Reuben', 'Markus', 'Oscar', 'Rodrick', 'Eugenio', 'Sylvester', 'Demarcus', 'Dar1in', 'Elwood', 'Tyson', 'Ron', 'Tuan', 'Emil', 'Jamel', 'Marcus', 'Roland', 'Brian', 'Zackary', 'Omar', 'Randell', 'Quintin', 'Brooks', 'Roosevelt', 'Ramiro', 'Odell', 'Hai', 'Bradford', 'Alva', 'Nick', 'Luciano', 'Theo', 'Xavier', 'Glenn', 'Aubrey', 'Jermaine']

monkeys = []
duelists = []
dead = []

class Utensil(object):
	def __init__(self, weight, damage):
		self.weight = weight
		self.damage = damage

	def whack(self, target):
		print "You did " + str(self.damage) + " points of damage to " + target + "!"

class Mom():
	def __init__(self, Utensil):
		phone_number = None
		work_number  = None
		home_address = None
		email_addy   = None
		self.weapon = Utensil

	def nag(self, target):
		print "Clean your room, " + target + "!"

	def brandish(self, target):
		self.weapon.whack(target)

frying_pan = Utensil(4, 7)

glenda = Mom(frying_pan)

# glenda.brandish('Horatio')
# glenda.nag('Horatio')

class Monkey(object):
	def __init__(self, name):
		self.bladeLength = random.randint(2,8) + random.randint(1,4)
		self.agility = random.randint(5,11)
		self.health = random.randint(22,45) - self.agility * 2
		self.name = name
		self.target = self
		self.kills = 0
		self.damageDealt = 0

	def __eq__(self, other):
	    return self.name == other.name

	def fight(self, arena):
		if self.health <= 0:
			self.die(arena)
			return
		while self.target == self and len(arena) > 1:
			self.target = random.choice(arena)
		if self.target != self:
			self.attack(self.target)
			self.target = self

	def attack(self, target):
		roll = random.randint(1,13)
		if roll + 7 - self.bladeLength >= target.agility or roll == 13:
			target.health -= self.bladeLength
			self.damageDealt += self.bladeLength
			if target.agility > 2:
				target.agility -= 1
			print self.name, 'stabbed', target.name, 'with his', self.bladeLength, 'inch knife!'
			self.target = self
			target.target = self
		else:
			print target.name, 'dodged', str(self.name)+'\'s', 'attack!'
			self.target = self

	def die(self, arena):
		print self.name, 'was killed by', self.target.name
		if self.bladeLength > self.target.bladeLength + 3:
			self.target.bladeLength = self.bladeLength
			print self.target.name, 'picked up', str(self.name)+'\'s', self.bladeLength, 'inch knife!'
		if self.target != self:
			self.target.kills += 1
		self.target = self
		dead.append(self)
		arena.remove(self)

def populate(monkeys, n):
	freshmeat = []
	for i in range(n):
		name = random.choice(names)
		freshmeat.append(Monkey(name))
	monkeys += freshmeat

def deathmatch():
	while len(monkeys) > 1:
		random.shuffle(monkeys)
		for monkey in monkeys:
			monkey.fight(monkeys)
			# time.sleep(0.05)
			# time.sleep(random.random()+.20)
	# winner()

def winner():
	for monkey in monkeys:
		plural = ''
		if monkey.kills != 1:
			plural = 's'
		print monkey.name, 'survived with', monkey.kills, 'kill'+plural+'!'

def duel():
	global duelists
	duelists = []
	while len(duelists) <= 1 and len(monkeys) > 0:
		entrant = random.choice(monkeys)
		duelists.append(entrant)
		monkeys.remove(entrant)
	while len(duelists) > 1:
		random.shuffle(duelists)
		for monkey in duelists:
			monkey.fight(duelists)
			time.sleep(random.random()/3+.05)
	for duelist in duelists:
		monkeys.append(duelist)

def tournament():
	while len(monkeys) > 1:
		duel()
		if len(monkeys) > 1:
			print len(monkeys), 'monkeys remaining!'

def dump():
	for monkey in monkeys:
		pprint(vars(monkey))
	for monkey in dead:
		pprint(vars(monkey))

def stats():
	superdead = random.choice(monkeys)
	mostdamage = random.choice(monkeys)
	mostkills = random.choice(monkeys)

	anywhere = dead + monkeys

	for monkey in anywhere:
		if monkey.health < superdead.health:
			superdead = monkey
		if monkey.damageDealt > mostdamage.damageDealt:
			mostdamage = monkey
		if monkey.kills > mostkills.kills:
			mostkills = monkey

	print 'Most dead:', superdead.name, '('+str(superdead.health)+')'
	print 'Most damage:', mostdamage.name, '('+str(mostdamage.damageDealt)+')'
	print 'Most kills:', mostkills.name, '('+str(mostkills.kills)+')'

populate(monkeys, 2)
# deathmatch()
# tournament()
duel()
winner()
# dump()
stats()
