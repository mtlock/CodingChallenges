# There exist numbers a, b and c such that a^2+b^2=c^2 and a+b+c=1000
# Find the product abc

a=1.0
while a<300:
    b=(-500000+1000*a)/(a-1000)
    if b>int(b):
        a=a+1
        #print b
        #print int(b)
        continue
    elif (a**2)+(b**2)==((1000-(a+b))**2):
        print "yes"
        break
    else:
        a=a+1
prod=a*b*(1000-(a+b))
print a
print b
print (1000-a-b)
print prod