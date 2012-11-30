import sys

fin = open(sys.argv[1])
lines = fin.readlines()
N = int(lines[0])
fout = open(sys.argv[1][:-2] + "out","w")
for i in range(1,N+1) :
    l = lines[i].split()
    l.reverse()    
    fout.write("Case #%d: %s\n" % (i, " ".join(l)))    
fout.close()