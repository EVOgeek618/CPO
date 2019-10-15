import sys
arg = int(sys.argv[1])
for i in range(1, arg+1):
    print(' '*(arg-i)+'#'*(i))
