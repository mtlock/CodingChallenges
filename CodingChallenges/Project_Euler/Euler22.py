#n1=raw_input("name")
#n2=raw_input("name")
#L=list()
#L.append(n1)
#L.append(n2)
#L.sort()
#print L


L=list()
file=open("E22names.txt")
for line in file:
    line=line.rstrip()
    names=line.split(",")
for name in names:
    name=name[1:-1]
    L.append(name.lower())
L.sort()
D={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

i=1
total=0
for name in L:
    j=0
    count=0
    while j<len(name):
        count=count+D[name[j]]
        j=j+1
    total=total+count*i
    i=i+1
print total



