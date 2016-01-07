# Given a string s, how many times does each word (case sensitive) occur in string?

# String s below:
s = "We tried list and we tried dicts also we tried Zen"

# Use line split to split the white spaces in the string:
splitS = s.split()
# !!! Different than the strip() command, which only removes the \n line ending.

print splitS

# Initialize an empty dictionary, d:
d = {}

# Create a for loop testing whether word in splitS is in dictionary:
for word in splitS:
    if word in d:
        # if the word is in d, then add 1
        d[word] += 1
    else:
        # if the word is not in d, then create 1
        d[word] = 1
print d

# Now to get the dictionary output in pretty format:
# ordered by entry and count in d
for entry, count in d.items():
    print entry, count
