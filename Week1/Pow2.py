import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
print(int((-b+(b*b-4*a*c)**0.5)/2), '\n', int((-b-(b*b-4*a*c)**0.5)/2))
