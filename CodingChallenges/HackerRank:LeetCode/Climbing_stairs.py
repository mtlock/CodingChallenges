#Climbing a staircase with n steps
#Can take 1 or 2 steps at a time
#How many distinct ways can you get to the top

n=int(raw_input("Enter the number of stairs "))

a=1
b=2
if n==1:
    print a
elif n==2:
    print b
else:
    for i in range(3,n+1):
        temp = a + b
        a = b
        b = temp
    print b