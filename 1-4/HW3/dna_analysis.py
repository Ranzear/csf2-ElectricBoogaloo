# Name: Royce Jensen
# Evergreen Login: jenroy30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys

# Time module for performance interest, uncomment with lines ~37, ~94
# from time import time


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]

# File extension check, because I got bored.
if filename.split('.')[len(filename.split('.'))-1] != 'fastq':
    print "Sorry, this script only handles .fastq format."
    sys.exit(2)

# A file object from which data can be read.
inputfile = open(filename)
# (I really wanted to add a try/except block on this, but open() throws its own)

# For performance interest
# start_time = time()

# Count of lines read for validation against original. Uncomment lines ~64, ~93
# linescounted = 0

# Count invalid pairs in total, or False to count only valid ATGC pairs
count_invalid = True

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0

# Reads .fastq files by format specifics instead of guessing where the useful
# data is. Added per-line counting instead of strip-and-load gymnastics.

# http://en.wikipedia.org/wiki/FASTQ_format

# When parsing, this activates counting on the next line to be read.
readnext = False

# Enumerate is super handy, but seriously what the hell, python? I can't just 
# have the file lines indexed nicely?
# http://docs.python.org/2/library/functions.html#enumerate
for i, line in enumerate(inputfile):
    if readnext == True: # Previous line started with an '@'
        # linescounted += 1 # For line count check.
        for bp in line.rstrip():
            if bp == 'C' or bp == 'G':
                total_count += 1 # Increment total count only on valid counts
                gc_count += 1
            elif bp == 'A' or bp == 'T':
                total_count += 1
                at_count += 1
            elif count_invalid == True:
                total_count += 1
        readnext = False
    elif readnext == False and line[0] == '@': # Read first character of line.
        readnext = True # Count pairs in next line

# This now takes about twelve seconds to count two types, versus almost a minute
# to count just one.

# divide the gc_count and ac_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content

# Extra count checking
# print 'G/C pairs', gc_count
# print 'A/T pairs', at_count

# print 'lines counted', linescounted
# print 'in ', time() - start_time, "seconds"
