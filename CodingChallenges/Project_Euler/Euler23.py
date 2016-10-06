#list of abundant numbers
#L1=[12]
#for x in range(13,28123):
#    dsum=1
#    for y in range(2,int(x**.5)+1):
#        if x%y==0: 
#            if y==x**.5:
#                dsum=dsum+y
#            else:
#                dsum=dsum+y+x/y
#    if dsum>x:
#        L1.append(x)
    
#print len(L1)



#make a list of sums of abundant numbers
list1=list()
list2=list()
for x in range(12,28123):
    dsum=1
    for y in range(2,int(x**.5)+1):
        if x%y==0: 
            if y==x**.5:
                dsum=dsum+y
            else:
                dsum=dsum+y+x/y
    if dsum>x:
        list1.append(x)
        for number in list1:
            if x+number<=28123:
            #print x
            #print number
            #print x+number
                list2.append(x+number)

#print len(list1)
list2.sort()
#print list2


list3=[0]
list3.append(list2[0])
i=1
count=list2[0]
while i<len(list2):
    if list2[i]!=list2[i-1]:
        list3.append(list2[i])
        count=count+list2[i]
    i=i+1
#print list3


#answer
print 28123*(28124/2)-count




    
        
   
    