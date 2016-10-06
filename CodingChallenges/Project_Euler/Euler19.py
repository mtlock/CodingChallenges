#How many sundays fell on the first of the month from January 1, 1900 through December 31, 2000

#D[i] equals the numeric day of the week, and the initial
#data listed below is for the year 1900

D=dict()
D[1]=2
D[2]=5
D[3]=5
D[4]=1
D[5]=3
D[6]=6
D[7]=1
D[8]=4
D[9]=7
D[10]=2
D[11]=5
D[12]=7

count=0

i=1
while i<=100:
    if i%4==0:
        D[1]=(D[1]+1)%7
        D[2]=(D[2]+1)%7
        if D[1]==1 or D[2]==1:
            count=count+1
        j=3
        while j<=12:
            D[j]=(D[j]+2)%7
            if D[j]==1:
                count=count+1
            j=j+1
    elif i>2 and (i-1)%4==0:
        D[1]=(D[1]+2)%7
        D[2]=(D[2]+2)%7
        if D[1]==1 or D[2]==1:
            count=count+1
        j=3
        while j<=12:
            D[j]=(D[j]+1)%7
            if D[j]==1:
                count=count+1
            j=j+1
    else:
        j=1
        while j<=12:
            D[j]=(D[j]+1)%7
            if D[j]==1:
                count=count+1
            j=j+1
    i=i+1

print count
    
        
