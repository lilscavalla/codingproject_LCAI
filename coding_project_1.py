
import sys, re

sampleString = "This has a 9 in it"

iWordRegex = re.compile("[a-zA-Z]*i[a-zA-Z]*")

iWords = iWordRegex.findall(sampleString)

sys.stdout.write("Here are all the words that matched: ")

for thing in iWords:
    sys.stdout.write("%s " % thing)