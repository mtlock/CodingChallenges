#ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP
#FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX
#27
#APMCTKBUKYRGZPAUVZEBVUXRGDVITOYXWQWRVCSXESMEHQLHPDJQWETAWQVSBRRNRRFDLFTRXOTKQHFTYAZSGBORDNAMUAJTPVOKERLVOLEALDQQLUDCUIRXJHQEZBRWYPFJXNTPELEZHNJILIZVZLYQJDFYSYQNRFFAOYXHQBQVRLFDIIOGWKQIZGVELYOUKZBKMHVYGIKIPSEMWSCWYOJTHOQKMLBAIZYNAKYNCXKDTTESODDAEAHKCDHCJYAHERACMLYQHXIRDFUSRTZDNVHSYFKCSPPYSLHOGIBTNUJTZQWVTHKUNDNWZADMATSUXEISCACQNQXIHNTXGCZUGIGBDONYTUXAXFINAYGZJVDCTZCWPGFNQDPERUCNJUXIFDSQHULYPZRNUOKMLMMQAJMLKCHJMEFJVRYZIPFQOBSDPAITHGMNKROCWJEGESCGOIUOQHOYUEQNPJPBMCNRZUHOSQNSUNCSTVQVWFGMUFJZGMEUVUPH
#JUVSDRRSHFGSSLLLZEPJDVAWDPKQBKUHHOZFFXKQMGAACZUYOMNPHWGTYZWQGSMNYXWNFYNOIVVMPZXUNKJQYBYJINBOHXUWIVRTVLEKCOPDMTKTGDBWECDAVPMLHQLERZHDVZJZODPSAPGSRWJXNGFEBQBLTLNDIEGFHEGHJWFOIYXRUJMODSNXUFWBIJJMXTFMUKQEYPNBTZFEJNLDNWCGQLVUQUKGZHJOKZNPMUYEQLEYNNORKJQAMSTHTBCCPQTTCPRZATWNJQJXPODRXKIWDOFUBZVSDTAPFRMXJBJMUGVRZOCDUIPXVEGMRQNKXDKNWXMTNDJSETAKVSYMJISAREEJPLRABMXJSRQNASOJNEEVAMWCFJBCIOCKMHCMYCRCGYFNZKNALDUNPUSTSWGOYHOSWRHWSMFGZDWSBXWXGVKQPHGINRKMDXEVTNNZTBJPXYNAXLWZSBUMVMJXDIKORHBIBECJNKWJJJSRLYQIKKPXSNUT
#155
#OUDFRMYMAW
#AWHYFCCMQX
#2

import sys

a=raw_input("enter a string: ").strip()
b=raw_input("enter a string: ").strip()



#def reduce(x,y):
#    L=[]
#    for charx in y:
#        for chary in x:
        
#            if charx!=chary or charx in L:
#                continue
#            else:
#                L.append(charx)
#    return (x,y,L)       


#def reduce(x,y):
#    L=[]
#    min=len(y)
#    for char in x:
#        if char in L:
#            continue
#        else:
#            try:
#                if y.index(char)<min:
#                    min=y.index(char)
#                    L.append(char)
#            except:
#                x.replace(char,'')     
#                pass   
#    for char in y:
#        if char in L:
#            continue
#        else:
#           y.replace(char,'')       
#    return (x,y,L)





L=[]
for chara in a:
    if chara in L:
        continue
    else:
        try:
            b.index(chara)
            L.append(chara)
        except:
            b.replace(chara,'')
            
            
            
            

def reduce(x,y):
    L1=[]
    min=len(y)
    for char in L:
        if char in L1:
            continue
        else:
            try:
                y.index(char)
                L1.append(char)
            except:
                x.replace(char,'')     
                #pass   
    #for char in y:
        #if char in L:
            #continue
        #else:
           #y.replace(char,'')       
    return (x,y,L1)



a,b,L=reduce(a,b)
if len(L)==0:
    print 0
else:
    La=[a]
    Lb=[b]
    n1=0
    n2=0
    i=0
    max=len(L)
    while max>0:
        m1=n1
        m2=n2
        Dx={}
        Dy={}
        k=0
          
        tempa=La
        tempb=Lb
        max=0
        La=[]
        Lb=[]
        j=0
        while j<len(tempa):
            if len(tempa[j])<=m1 and len(tempb[j])<=m2:
                j=j+1
                continue
            elif len(tempa[j])>m1 and len(tempb[j])>m2:
                m1=len(tempa[j])
                m2=len(tempb[j])
            x,y,L1=reduce(tempa[j],tempb[j])
            if len(L1)>max:
                max=len(L1)
            n1=0
            n2=0
            for char in L1:
                if len(x[x.index(char)+1:])<=Dx.get(char,0):
                    if len(y[y.index(char)+1:])<=Dy.get(char,0):
                        continue
                elif len(x[x.index(char)+1:])>Dx.get(char,0):
                    if len(y[y.index(char)+1:])>Dy.get(char,0):
                        Dx[char]=len(x[x.index(char)+1:])
                        Dy[char]=len(y[y.index(char)+1:])
                ta=x[x.index(char)+1:]
                tb=y[y.index(char)+1:]
                if len(ta)<n1 and len(tb)<n2:
                    continue
                elif len(ta)>n1 and len(tb)>n2:
                    n1=len(ta)
                    n2=len(tb)
                La.append(ta)
                Lb.append(tb)
                
                #La.append(x[x.index(char)+1:])
                #Lb.append(y[y.index(char)+1:])
                #if len(x[x.index(char)+1:])>n1 and len(y[y.index(char)+1:])>n2:
                #    n1=len(x[x.index(char)+1:])
                #    n2=len(y[y.index(char)+1:])
            j=j+1   
           
        i=i+1
    #print i-1
    print i
     