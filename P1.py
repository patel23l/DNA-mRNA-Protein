import sys

def PrintNum(num=10):
    try:
        for i in range(1, num+1):
            print(i, end =" ")
        return 0
    except Exception:
        return 1

if len(sys.argv) == 2:
    PrintNum(int(sys.argv[1]))
else:
    PrintNum()