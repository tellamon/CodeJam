import sys
import collections

class Case :
    def __init__(self, C, I, P) :
        self.C = int(C)
        self.I = int(I)
        self.P = map(int, P.split())        
        assert (self.I == len(self.P))  
    def GetResult(self) :
        for i in range(0,len(self.P)-1):
            for j in range(i+1,len(self.P)):
                if(self.C == (self.P[i] + self.P[j])) :                    
                    return (i,j)

        assert(0) # Not to be reached.
    def Solve(self, idx, fout) :
        (i,j) = self.GetResult()
        fout.write("Case #%d: %d %d\n" % (idx,i+1,j+1))        
                   
#fin = open("A-small-practice.in")
fin = open(sys.argv[1])
lines = collections.deque(fin.readlines())
N = int(lines.popleft())
fout = open(sys.argv[1][:-2] + "out","w")
for i in range(1,N+1) :
    c = Case(lines.popleft(),lines.popleft(),lines.popleft())
    c.Solve(i,fout)    
fout.close()