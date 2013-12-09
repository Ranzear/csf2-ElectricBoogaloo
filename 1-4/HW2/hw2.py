# Name: Royce Jensen
# Evergreen Login: jenroy30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
n = hw2_test.n
i = 1
result = 0
while (i <= n): # While loop for variety, less-than-or-equal so we include the final value, else we'd have to n+1.
	result += i
	i += 1 # How I would love to be able to 'result += i++'... Oh well
print result

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# Could i = float(0) here or something, but rather keep increment as int and/or unaware if for() cares or will change it back to int.
n = 10
for i in range(2, n+1): # Start with 1/2.
	result = 1 / float(i) # Right-side typing is probably going to drive me insane. http://docs.python.org/2/library/functions.html#float
	print result

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
result = 0
for moose in range(1, n+1):
	result += moose # A moose bit my sister once.
print result


###
### Problem 4
###
 	
# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
result = 1
for theSwarm in range(1, n+1):
	result *= theSwarm
print result # and send the lings.

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
result = 1
i = numlines
while i > 0: # Decrementing loop to avoid string juggling and make the function shorter than this comment explaining it.
	for j in range(0, i): # Yo dawg I heard you like decrementing, 
		result *= i - j # so we subtract an increment from your decrement so you can decrement while you decrement.
	print result
	result = 1 # Reset after printing value.
	i -= 1

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

eulerByIteration = 1 # Initialize at 1 so we don't have to add it later.
for i in range(1, 10): # On second thought... Let's not decrement. 'Tis a silly method.
	factorial = 1
	for j in range(0, i): # Calculate factorial of current increment
		factorial *= i - j 
	eulerByIteration += 1 / float(factorial) # Reciprocal with another complaint about right-side typing.
print eulerByIteration

###
### Collaboration
###

# Python has some pretty decent documentation at http://docs.python.org/2/, just about all I need is syntax reference.

###
### Reflection
###

# Anything worth doing is worth overdoing. Problem 5 can be a little snaggy if you buy the hint to use two for loops;
# decrementing saves a ton of other handling. Loops are my jam (and my jams are usually loops), like when I needed to
# call and embed javascript dependencies in PHP that may have their own dependencies which are all stipulated in MySQL
# and references are tossed in an array which is checked to prevent recursion... Yeah, loops are my thing.
