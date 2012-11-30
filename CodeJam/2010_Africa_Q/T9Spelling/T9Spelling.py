import sys
import collections

button_map = {
    'a' : "2",
    'b' : "22",
    'c' : "222",
    'd' : "3",
    'e' : "33",
    'f' : "333",
    'g' : "4",
    'h' : "44",
    'i' : "444",
    'j' : "5",
    'k' : "55",
    'l' : "555",
    'm' : "6",
    'n' : "66",
    'o' : "666",
    'p' : "7",
    'q' : "77",
    'r' : "777",
    's' : "7777",
    't' : "8",
    'u' : "88",
    'v' : "888",
    'w' : "9",
    'x' : "99",
    'y' : "999",
    'z' : "9999",
    ' ' : "0",
}
class Case :
    def __init__(self, S) :        
        self.desired_messages = list(S)
    def GetIndex(self) :
        ret = ""
        prev_c = '' 
        for c in self.desired_messages :
            if(prev_c == c) :
                ret.append(' ')                
            ret.append(button_map[c])           
        
        return ret
    def Solve(self, idx, fout) :
        (i,j) = self.GetIndex()
        fout.write("Case #%d: %d %d\n" % (idx,i+1,j+1))        
                   
#fin = open("A-small-practice.in")
fin = open(sys.argv[1])
lines = collections.deque(fin.readlines())
N = int(lines.popleft())
fout = open(sys.argv[1][:-2] + "out","w")
for i in range(1,N+1) :
    c = Case(lines.popleft())
    c.Solve(i,fout)    
fout.close()