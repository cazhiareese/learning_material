Printing
print('Hello')

# Variable declaration
c = 10
a = 1

# Control structures
if c == 0:
    print('Oh no')
else:
    print('Yey')

if c == 10 and a == 1:
    print('OK')


for i in range(c):
	print(i)

print('==========================================================')
print('Multiplication table')
counter = 0
while counter < c:
    counter2 = 1
    while counter2 < c:
        print(counter * counter2, end=' ')
        counter2 = counter2 + 1

    print('\n')

    counter = counter + 1

print('==========================================================')
print('Triangle')
 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *

counter3 = 1

while counter3 < c:
    print('* ')

    counter4 = 0

    while counter4 < counter3:
        print('* ', end=' ')
        counter4 = counter4 + 1

    counter3 = counter3 + 1


print('==========================================================')
print('Reverse Triangle')

#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
# * * * * * *

counter5 = 1

while counter5 < c:
    
    counter6 = 0

    while counter6 < c:
        if c - counter6 < counter5:
            print('*', end= ' ')
        else: 
            print(' ', end= ' ')


        counter6 = counter6 + 1


    print('\n')
    counter5 = counter5 + 1



