numbers = []
low_num = int(raw_input("Define the lowest range value > "))
high_num = int(raw_input("Define the uppermost range value > "))
step_num = int(raw_input("Define the step value > "))

def while_func(i, x, y):
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + y
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_func(low_num, high_num, step_num)

print "The numbers: "

for num in numbers:
    print num
