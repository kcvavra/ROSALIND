# Create Read/Write Script for the ROSALIND System based on Instructions
# Sample file is at RWSample.txt
# Problem file is at RWProblem.txt (not uploaded to repository)

# Open file into variable f
f = open('RWProblem.txt', 'r')

# Initiate line number variable, lineNum. lineNum is 1-based numbering
lineNum = 1

# Create a for loop in each line, and use the remainder function to
# determine whether the line index is even or odd. If even, print contents
# of line. After if statement, add one to lineNum
for line in f:
    if lineNum%2 == 0:
        out = line.strip()
        print out
    lineNum += 1
