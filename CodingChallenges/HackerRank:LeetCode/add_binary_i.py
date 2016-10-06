#Given 2 binary strings, return their sum (also a binary string)



def addbinary(s1,s2):
    n1=int(s1)
    n2=int(s2)
    falsesum=list(str(n1+n2))
    sum=''
    i=len(falsesum)-1
    while i>=0:
        if falsesum[i]=='0' or falsesum[i]=='1':
            sum=falsesum[i]+sum
        elif falsesum[i]=='2':
            if i>0:
                sum='0'+sum
                falsesum[i-1]=str(int(falsesum[i-1])+1)
            else:
                sum='10'+sum
        else:
            if i>0:
                sum='1'+sum
                falsesum[i-1]=str(int(falsesum[i-1])+1)
            else:
                sum='11'+sum
        i-=1
    return sum




s1=raw_input("enter the first string: ")
s2=raw_input("enter the second string: ")
print addbinary(s1,s2)