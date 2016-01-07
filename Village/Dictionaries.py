# Given a string s, how many times does each word (case sensitive) occur in string?

# String s below:
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

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
