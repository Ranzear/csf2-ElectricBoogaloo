import random

dog = {'excite':0}
squirrel = {'visible':False,'scarce':True}
car = {'visible':True,'scarce':False,'position':-40}
sawsquirrel = False
barks = {'car':0,'squirrel':0}

def carmove(car):
	car['position'] += 1
	if car['position'] > 40:
		car['visible'] = False

	if car['position'] == 0:
		print 'Vroom!'

def barkat(thing):
	print 'Arf!'
	if thing['scarce']:
		thing['visible'] = False
		barks['squirrel'] += 1
	else:
		barks['car'] += 1
	dog['excite'] = dog['excite'] / 10

while squirrel['visible']:
	sawsquirrel = True
	dog['excite'] += 1
	if dog['excite'] > random.randrange(40,312)z:
		barkat(squirrel)

while car['visible']:
	carmove(car)
	dog['excite'] += 1
	if dog['excite'] > random.randrange(7,70):
		barkat(car)

if barks['squirrel'] > 0:
	print "Squirrel = " + str(squirrel['visible'])

if barks['car'] > 0:
	print "Barks at car: " + str(barks['car'])
