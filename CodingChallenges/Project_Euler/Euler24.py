#millionth lexicographic permutation of 0-9

#0-----  9!
#1-----  9!
#2*9!=725760
#20------ 8!
#21------ 8!
#23----- 8!
#24------ 8!
#25------ 8!
#26------ 8!
#2*9!+6*8!=967680
#270-----7!
#271-----7!
#273-----7!
#274-----7!
#275-----7!
#276-----7!
#2*9!+6*8!+6*7!=997920
#2780-----6!
#2781-----6!
#2*9!+6*8!+6*7!+2*6!=999360
#27830-----5!
#27831-----5!
#27834-----5!
#27835-----5!
#27836-----5!
#2*9!+6*8!+6*7!+2*6!+5*5!=999960
#278390-----4!
#2*9!+6*8!+6*7!+2*6!+5*5!+4!=999984
#2783910-----3!
#2783914-----3!
#2*9!+6*8!+6*7!+2*6!+5*5!+4!+2*3!=999996
#27839150-----2!
#27839154-----2!
#gets to millionth number

#2783915460

#D1 is dictionary of factorials 0-9
D1={0:1}
number=1
while number<=9:
    temp=number
    fact=1
    while temp>0:
        fact=fact*temp
        temp=temp-1
    D1[number]=fact
    number=number+1

#D2 is the dictionary of how many of each factorial can have before you get to 1000000
D2=dict()
sum=0
number=9
while number>=0:
    D2[number]=(1000000-sum)/D1[number]
    sum=sum+D2[number]*D1[number]
    if sum>=1000000:
        break
    else:
        number=number-1
#print D2

L=[0,1,2,3,4,5,6,7,8,9]
number=9
term=""
while number>2:
    term=term+str(L[D2[number]])
    del L[D2[number]]
    number=number-1
print term+"460"
    
        
          
    