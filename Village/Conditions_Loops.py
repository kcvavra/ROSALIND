a = 42
b = -38
if a < 10:
  print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'

if a + b == 4:
  print 'printed when a + b equals four'
print 'always printed'

greetings = 1
while greetings <= 3:
  print 'Hello! ' * greetings
  greetings = greetings + 1

names = ['Alice', 'Bob', 'Charley']
for name in names:
  print 'Hello, ' + name

n = 10
for i in range(n):
  print i

print range(5, 12)
