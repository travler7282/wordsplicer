import argparse
import itertools

# parse command line arguments
# -i is the input file that contains a list of words to combine
# -o is the output file that the combined words will be saved to
# -c is the word count, this is the number of words to combine, this is limited to 4
#    but this value can be increased if you would like, it will just take more space on the disk and
#    in memory. 
parser = argparse.ArgumentParser()
parser.add_argument('-i', metavar='in-file', type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file', type=argparse.FileType('wt'))
parser.add_argument('-c', metavar='word-count', type=int)

# try parsing the command line arguments
try:
    results = parser.parse_args()
except IOError as msg:
    parser.error(str(msg))
    exit(-1)

# validate that c is between 1 and 5
if results.c < 0 or results.c > 5:
    print("ERROR: The wordcount (-c) parameter must be between 1 and 5 and is required.")
    exit(-2)

# create the wordlist list
wordlist = list()

# read the words from the input file and append them to the wordlist list
for line in results.i:
    wordlist.append(line.strip('\n').strip('\r'))

# for each word read into the wordlist list, combine with the other words and place results
# into another list of tuples
result = list(itertools.combinations(wordlist, 3))
for combination in result:
    for word in combination:
        results.o.write(word)
    results.o.write("\n")

