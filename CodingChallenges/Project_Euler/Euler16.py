#find the sum of the digits in the number 2**1000
D=dict()
power=1
D[1]=2
while power<=256:
    D[2*power]=D[power]*D[power]
    power=2*power
val=D[512]*D[256]*D[128]*D[64]*D[32]*D[8]
string_val=str(val)
sum=0
for d in string_val:
    sum=sum+int(d)
print sum

