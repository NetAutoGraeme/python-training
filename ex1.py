from sys import argv

print 'Hello World'
print 'Hello World'
print 'Hello',
print 'World'


print 5 + 2
print 'Now I will count', 5 + 9
print 'Now I will count in floating point numbers', 20.0 + 5.0
print 7.0 / 4.0
print 7 / 4


var1 = 1.73333
print round(var1)


one, two, three, four = argv

five = int(raw_input("Input a value "))

print one
print two
print three
print four
print five

print """Variable one = %s\nVariable two = %s\nVariable three = %s
Variable four = %s\nVariable five = %s
""" % (one, two, three, four, five)

