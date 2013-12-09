# Name: Royce Jensen
# Evergreen Login: jenroy30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 4: DNA analysis (Part 2)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
# Or run it without arguments to find and process all .fastq files in the /data subfolder!

##  LIBRARIES  ##

# The sys module supports reading files, command-line arguments, etc.
import sys
import os

# Glob module for getting a 
import glob

# Time module for performance interest
from time import time
start_time = time()

# Count of lines read for validation against original.
# linescounted = 0

# Count invalid pairs in total, or False to count only valid ATGC pairs
count_invalid = True

# Bool for whether to output to console or /results
batch = False
# batchlist is internal list of file names to batch process, or just one for non-batch
batchlist = []
# You need to specify a file name, else we glob and process the entire data subfolder
if len(sys.argv) < 2:
    print "Processing /data folder!"
    os.chdir('./data')
    batchlist = glob.glob('*.fastq')
    batch = True
else:
    filename = sys.argv[1]
    if filename.split('.')[len(filename.split('.'))-1] != 'fastq':
        print "Sorry, this script only handles .fastq files."
        sys.exit(2)
    batchlist.append(sys.argv[1])

if not batchlist:
    print 'No file(s) found!'
    sys.exit(2)

# Number of files processed.
processed = 0

# Reads .fastq files by format specifics instead of guessing where the useful
# data is. Added per-line counting instead of strip-and-load gymnastics.

# http://en.wikipedia.org/wiki/FASTQ_format


##   BEGIN MAIN LOOP  ##
for filename in batchlist:

    # Total nucleotides seen so far.
    total_count = 0
    # Sequence count, including invalids if count_invalids = False
    seq_count = 0
    # Number of G nucleotides seen so far.
    g_count = 0
    # Number of C nucleotides seen so far.
    c_count = 0
    # Number of A nucleotides seen so far.
    a_count = 0
    # Number of t nucleotides seen so far.
    t_count = 0

    inputfile = open(filename)
    processed += 1
    print 'Processing', filename

    # When parsing, this activates counting on the next line to be read.
    readnext = False


    # I swear enumerate() makes this faster.
    for i, line in enumerate(inputfile):
        if readnext == True: # Previous line started with an '@'
            # linescounted += 1 # For line count check.
            for bp in line.rstrip():
                if bp == 'G':
                    total_count += 1 # Increment total count on valid counts
                    g_count += 1
                elif bp == 'C':
                    total_count += 1
                    c_count += 1
                elif bp == 'A':
                    total_count += 1
                    a_count += 1
                elif bp == 'T':
                    total_count += 1
                    t_count += 1
                elif count_invalid == True:
                    total_count += 1 # Increment total count on invalid counts
                seq_count += 1
            readnext = False
        elif readnext == False and line[0] == '@': # Read first character of line.
            readnext = True # Count pairs in next line
    if total_count:
        # divide the gc_count and ac_count by the total_count
        gc_content = float(g_count+c_count) / total_count
        at_content = float(a_count+t_count) / total_count

        # Calculate AT/GC ratio using valid counts.
        at_gc_ratio = float(a_count+t_count)/float(g_count+c_count)
        
        if gc_content >= 0.6:
            gc_class = 'high GC content'
        elif gc_content < 0.4:
            gc_class = 'low GC content'
        else:
            gc_class = 'moderate GC content'
       
        inputfile.close()
        results = ''
        results += ('GC-content: ' + str(gc_content) + '\n')
        results += ('AT-content: ' + str(at_content) + '\n')
        results += ('G count: ' + str(g_count) + '\n')
        results += ('C count: ' + str(c_count) + '\n')
        results += ('A count: ' + str(a_count) + '\n')
        results += ('T count: ' + str(t_count) + '\n')
        results += ('Sum count: ' + str(g_count+c_count+a_count+t_count) + '\n')
        results += ('Total count: ' + str(total_count) + '\n')
        results += ('seq length: ' + str(seq_count) + '\n')
        results += ('AT/GC Ratio: ' + str(at_gc_ratio) + '\n')
        results += ('GC Classification: ' + gc_class + '\n')

        if batch:
            resfile = open(filename.split('.')[0]+'_results.txt', 'w')
            resfile.write(results)
            resfile.close()
        else:
            print results
    else:
        print 'Invalid .fastq file!'
##  END MAIN LOOP  ##

print 'Processed', processed, 'files in', time() - start_time, 'seconds.'
