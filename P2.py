import sys
import os

def CallProgram(*args):
    #checks the program name
    if args[0] == "P1":
        if len(args) == 2:
            #if number argument given then runs it with that
            x = os.system("python P1.py " + args[1])     
            if x == 0:
                print("Yes")
                return 0
            else:
                print("No")
                return 1   
        else:
            #runs it without the number argument
            x = os.system("python P1.py")
            #checks the return value and prints the correct number
            if x == 0:
                print("Yes")
                return 0
            else:
                print("No")
                return 1
    #if the program is P2
    elif args[0] == "P2":
        print("In P2")
        #runs the program with parameter
        os.system("python P2.py P2")
    
#checks if this file is ran
if __name__ == "__main__":
    #gets the program name
    program = sys.argv[1]
    #checks the number of arguments to see if second parameter is given
    if len(sys.argv) == 3:
        #gets the number
        num = sys.argv[2]
        #calls the function
        CallProgram(program, num)
    else: CallProgram(program)