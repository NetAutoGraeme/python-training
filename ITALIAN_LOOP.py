import random

#functions
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def option1():
    randomvar = random.randint(0,9))
    temp = LIST1[1]
    print '\nWhat is the Italian translation for >>> %s\n' % LIST1[1]
    raw_input('Press Enter for answer...')
    print '\nAnswer is >>> %s' % LIST1[2]

#Phrase Lists
PARENTLIST = [LIST1, LIST2, LIST3]
LIST1 = [1, 'hello', 'Ciao']
        
#script

print '''
\n\n\n
\t\t\tITALIAN PHRASE TRAINING
\t\t\t=======================
'''

print '''
\n\n\n
This script allows the user to improve their Italian Phrases.
Elle Woods uses this script when travelling to meet Vincenzo in Tuscony
and swears by it ;-)
\n\n\n
Script Options...
1) Randomly generated phrases
2) Complete phrase list
3) Wildcard ???
'''

command = raw_input('Select an option: ')
if RepresentsInt(command) == True:
   command2 = int(command)
else:
    print 'Sorry incorrect entry'

if command2 == 1:
    option1()
elif command2 == 2:
    print '2'
elif command2 == 3:
    print '3'
else:
    print 'Does not compute'
