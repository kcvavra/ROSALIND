# Two positive integers, and and b, such that a< b <10000
# Return the sum of all odd integers from a through b

# initialize sum variable, s
s = 0

# set a and b
a = 4898
b = 9222

# perform the function, using the c as the element being tested in for loop
for c in range(a, b):
    if c % 2 ==1:
        s = s + c

print s
