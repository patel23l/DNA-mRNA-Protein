import sys
import os

def CallProgram(*args):
    try:
        if args[0] == "P1":
            if len(args) == 2:
                os.system("python P1.py " + args[1])        
            else:
                os.system("python P1.py")
        elif args[0] == "P2":
            print("...in P2")
            os.system("python P2.py P2")
        
        print("yes")
        return 0
    except Exception:
        print("no")
        return 1

if __name__ == "__main__":
    program = sys.argv[1]
    if len(sys.argv) == 3:
        num = sys.argv[2]
        CallProgram(program, num)
    else: CallProgram(program)