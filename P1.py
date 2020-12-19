#import statements
import sys

#sets a default value to be 10 if no number argument is given
def PrintNum(num=10):
    #tries the loop and prints the numbers
    try:
        for i in range(1, num+1):
            print(i, end=" ")
        #returns when the all the numbers are printed
        return 0
    #if it encounters a problem it will be caught here
    except Exception:
        #returns 1 if there is a failure
        return 1

#checks the number of arguments given, if it has number given as the argument
if len(sys.argv) == 2:
    PrintNum(int(sys.argv[1]))
else:
    #calls it without the argument
    PrintNum()