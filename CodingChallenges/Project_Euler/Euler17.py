

#first find the sum of all letters 

#number of times each digit appears in 1-99
D=dict()
i=1
while i<=999:
    string=str(i)
    k=0
    while k<=len(string)-1:
        D[int(string[k])]=D.get(int(string[k]),0)+1
        k=k+1
    i=i+1
#print "The number of times each digit appear in the numbers 1-999 is"
#print D

  
#separate into hundres, tens, ones for 1-999
D2=dict()
i=1
hundreds=0
onehundred=0
while i<=999:
    string=str(i)
    if len(string)==1:
        #ones=ones+1
        D2[int(string)]=1
    elif len(string)==2:
        #tens=tens+1
        str0=int(string[0])*10
        str1=int(string[1])
        if int(string[0])==1:
            D2[int(string)]=D2.get(int(string),0)+1
        elif str1>0:
            D2[str1]=D2[str1]+1
            D2[str0]=D2.get(str0,0)+1
        else:
            D2[str0]=D2.get(str0,0)+1   
    else:
        str0=int(string[0])*100
        str1=int(string[1])*10
        str2=int(string[2])
        if int(string[1])==1:
            D2[int(string[1:3])]=D2.get(int(string[1:3]),0)+1
            D2[str0]=D2.get(str0,0)+1
        elif int(string[1])==0 and str2==0:
            D2[str0]=D2.get(str0,0)+1
        elif str2>0:
            if int(string[1])==0:
                D2[str2]=D2[str2]+1
                D2[str0]=D2.get(str0,0)+1
            else:
                D2[str2]=D2[str2]+1
                D2[str1]=D2[str1]+1
                D2[str0]=D2.get(str0,0)+1
        else:
            D2[str0]=D2.get(str0,0)+1 
            D2[str1]=D2[str1]+1
    i=i+1


list=[(k,v) for k,v in D2.items()]
print "The number of times each hundres, tens and ones appears in the numbers 1-999 is"
print sorted(list)

