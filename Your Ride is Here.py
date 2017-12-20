
'''
ID: alinad1
LANG: PYTHON3
PROG: ride
'''

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
a = fin.readline().split()[0]
b = fin.readline().split()[0]
print (a)
print (b)
aa = 1
bb = 1
for i in a:
    aa *= ord(i) - ord('A') + 1
for i in b:
    bb *= ord(i) - ord('A') + 1
if (bb%47 == aa % 47):
    fout.write("GO\n")
else:
    fout.write("STAY\n")
