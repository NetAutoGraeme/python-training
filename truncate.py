from sys import argv
# - *- coding: utf- 8 - *-

filename = raw_input('Filename > ')

delete_contents = open(filename, 'r+')
view_contents = delete_contents.read()
print '\n###FILE CONTENTS###\n%s\n###FILE CONTENTS###' % view_contents
print '\nTruncating/deleting the contents of the file!!!'
delete_contents = open(filename, 'w')
delete_contents.truncate()

print 'Contents deleted. Done!'

delete_contents.close()
