import random

f = open('madlibs\madlibs.txt')
madlibText = f.readlines()

madlib = random.choice(madlibText)
#print(madlib)

if (madlib.find("thing")>=0):

    occurences = madlib.count("thing")
    inputs=[]

    for x in range(occurences):
        noun = input('Enter a thing: ')
        inputs.append(noun)
        madlib = madlib.replace("thing", noun, 1)

else:

    occurences = madlib.count("blank")
    inputs=[]

    for x in range(occurences):
        noun = input("Enter a blank: ")
        inputs.append(noun)
        madlib = madlib.replace("blank", noun, 1)


print(madlib)
