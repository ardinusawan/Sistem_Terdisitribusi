import sys


def printme():
    # print('hello');
    return 1


def write():
    # print('Creating new text file')

    # name = input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt
    name = 'wawan'
    try:
        file = open(name,'w')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python



