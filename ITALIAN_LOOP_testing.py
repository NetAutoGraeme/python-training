import random

#functions
#=========

# Function checks raw_input to see if this is a valid integer and returns a true or false
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Function to Option 1 of script
def option1():
    #user specified number of questions to be asked
    answer_no = int(raw_input('How many questions would you like to answer: '))
    i = 1
    # loop upto the user specified amount
    while i <= answer_no:
        #obtain random integer value between values listed
        randomvar = random.randint(0,12)
        # set var 'temp' to be element of PARENTLIST. See phrase lists
        temp = PARENTLIST[randomvar]
        # Print argument 2 in randomly selected list
        print '\nWhat is the Italian translation for >>> %s\n' % temp[1]
        raw_input('Press Enter for answer...')
        # Print argument 3 in randomly selected list
        print '\nAnswer is >>> %s\n\n' % temp[2]
        i = i + 1
    else:
        quit()
    

def option2():
    for i in range(0, 13):
        temp = PARENTLIST[i]
        # Print argument 2 in randomly selected list
        print '\nWhat is the Italian translation for >>> %s\n' % temp[1]
        raw_input('Press Enter for answer...')
        # Print argument 3 in randomly selected list
        print '\nAnswer is >>> %s' % temp[2]

#Phrase Lists
#============

#Define phrases as lists. The number is used for listing/random generation. Arg 2 is the English
#word, Arg 3 is the Italian word
LIST1 = [1, 'hello', 'Ciao']
LIST2 = [2, 'Thank you', 'Grazie']
LIST3 = [3, 'Beautiful', 'Belissimo']
LIST4 = [4, 'You\'re Welcome', 'Prego']
LIST5 = [5, 'Please', 'Per favore']
LIST6 = [6, 'Yes', 'Si']
LIST7 = [7, 'No', 'No']
LIST8 = [8, 'Excuse Me/Pardon Me', 'Mi scusi']
LIST9 = [9, 'I don\'t speak Italian very well', 'Non parlo molto bene Italiano']
LIST10 = [10, 'Do you speak English?', 'Parla inglese']
LIST11 = [11, 'How much does that cost (sg./pl.)?', 'Quanto costa/costano?']
LIST12 = [12, 'Goodbye', 'Arrivederci']
LIST13 = [13, 'Check please', 'Il conto, per favore']
#PARENTLIST must maintain all phrase lists to be used as elements
PARENTLIST = [LIST1, LIST2, LIST3, LIST4, LIST5, LIST6, LIST7, LIST8, LIST9, LIST10,
 LIST11, LIST12, LIST13]
        
#script
#======

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

# Below allows user to specify an integer and test whether this is true or false (string)
# Depending on the option the various function is then performed!
command = raw_input('Select an option: ')
if RepresentsInt(command) == True:
   command2 = int(command)
else:
    print 'Sorry incorrect entry'

if command2 == 1:
    option1()
elif command2 == 2:
    option2()
elif command2 == 3:
    print '\t*** Pick your prize @ http://www.mulberry.com/gb/shop/women/bags *** '
else:
    print 'Does not compute'
