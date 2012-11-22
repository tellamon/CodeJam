
class Case :
    def __init__(self, C, I, P) :
        self.C = int(C)
        self.I = int(I)
        self.P = map(int, P.split())
        pass
    def __repr__(self) :
        return str(self.C)
    def GetIndex(self) :
        for i in range(0,len(self.P)-1):
            for j in range(i+1,len(self.P)):
                #print self.C, self.P[i], self.P[j]
                if(self.C == (self.P[i] + self.P[j])) :                    
                    return (i,j)

        raise Exception("NOT TO BE REACHED")
    def Solve(self, idx, fout) :
        (i,j) = self.GetIndex()
        outstr = "Case #%d: %d %d\n" % (idx,i+1,j+1)
        fout.write(outstr)
                   
#f = open("A-small-practice.in")
f = open("A-large-practice.in")

lines = f.readlines()

lines.reverse()
N = int(lines.pop())

fout = open("solution.txt","w")
for i in range(1,N+1) :
    c = Case(lines.pop(),lines.pop(),lines.pop())
    c.Solve(i,fout)    
fout.close()