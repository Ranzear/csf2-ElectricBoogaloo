# Name: Royce Jensen
# Evergreen Login: jenroy30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available

###
### Problem 1
###

# Extract A, B, and C of x^2-5.86x+8.5408
a = 1
b = -5.86
c = 8.5408

# Positive quadratic
pos = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
# Negative quadratic
neg = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a

# Solutions rounded to sig figs, to list, to string.
sol1 = str([round(pos,2), round(neg,2)])

print "Problem 1 solution follows:"
print sol1

###
### Problem 2
###

# Import the stuffs and screw namespace
from hw1_test import *

# Concatenate to solution with newlines
sol2 = str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d)+'\n'+str(e)+'\n'+str(f)

print "\nProblem 2 solution follows:"
print sol2

###
### Problem 3
###

# Evaluate solution 3
sol3 = str((a and b) or (not c) and not (d or e or f))

print "\nProblem 3 solution follows:"
print sol3

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
