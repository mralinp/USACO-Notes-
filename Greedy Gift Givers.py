
'''
ID: alinad1
LANG: PYTHON3
PROG: gift1
'''

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
n = list(map(int, fin.readline().split()))[0]
di = {}
bank = {}
for i in range(n):
    tmp = fin.readline().split()[0]
    di[i] = tmp
    bank[tmp] = 0
for i in range(n):
    name = fin.readline().split()[0]
    a, b = list(map(int, fin.readline().split(" ")))
    gift = 0
    if(b!=0):
        gift = int(a/b)
        bank[name] = bank[name] - a + a%b;
    for j in range(b):
        tmp = fin.readline().split()[0]
        bank[tmp] = bank[tmp]+gift
for i in range(n):
    tmp = ""
    tmp = str(di[i]) + " " + str(bank[di[i]]) + "\n"
    fout.write(tmp)

