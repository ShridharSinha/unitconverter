f = open("Conversions.txt", "r")
S=f.read()
x = S.split('\n')
del(x[0])
for a in x:
    if(a==''):
        x.remove('')
e=[]
while len(x)>0:
    a=[x[0].split(' ')[1],x[0].split(' ')[4],x[0].split(' ')[3]]
    #print(a)
    #print(x)
    e.append(a)
    del x[0]
def poss(u1,c,d):
    b=[]
    for arr in e:
        if(u1 in arr):
            if((arr[1-arr.index(u1)] not in b)and arr[1-arr.index(u1)] not in c):
                b.append(arr[1-arr.index(u1)])
            if(arr[1-arr.index(u1)] not in c):
                c.append(arr[1-arr.index(u1)])
        d.append(b)
    return c
def findpath(u1,u2,c,d):
    b=[]
    if(u2 in c):
        return d
    if len(b)==0:
        b.append(u1)
    if len(c)==0:
        c.append(u1)
    for arr in e:
        if(u1 in arr):
            if((arr[1-arr.index(u1)] not in b)and arr[1-arr.index(u1)] not in c):
                b.append(arr[1-arr.index(u1)])
            if(arr[1-arr.index(u1)] not in c):
                c.append(arr[1-arr.index(u1)])
        d.append(b)
    for i in range(c.index(u1)+1,len(c)):
        if(c[i] == u2):
            break
        findpath(c[i],u2,c,d)
    if(u2 in c):
        return d
    return 0

def convert(n,u1,u2,coeff,i):
    for arr in e:
        if(u1 in arr and u2 in arr and u1!=u2):
            if(arr[0]==u1):

                coeff*=(float(arr[2]))
                return(coeff*n)
            else:
                coeff*=1/float(arr[2])
                return(n*coeff)
    if(len(u1.split('/'))==1 and len(u2.split('/'))==1):
        if(u1 == u2):
            return(n*coeff)   
        g=findpath(u1,u2,[],[])
        if(g==0):
            return("no conversion")
        new_k = []
        for elem in g:
            if elem not in new_k:
                new_k.append(elem)
        g = new_k
        for arr in e:
            if(g[len(g)-1][0] in arr and u2 in arr):
                if(arr.index(u2)==0):
                    v=-1
                else:
                    v=1
                coeff*=float(arr[2])**(v)
        return(convert(n,u1,g[len(g)-1][0],coeff,i))
    elif(len(u1.split('/'))==len(u2.split('/')) and (len(u2.split('/'))!=1)):
        while(i<len(u1.split('/'))):
            if(i%2==0):
                v=1
            else:
                v=-1
            if(convert(n,u1.split('/')[i],u2.split('/')[i],coeff,i)!="no conversion"):
                coeff*=(float(convert(n,u1.split('/')[i],u2.split('/')[i],1,i))/n)**v
            else:
                return "no conversion"
            i+=1
        return(coeff*n)
    elif(len(u1.split('/'))!=1 and (len(u2.split('/'))==1)):
        qe=poss(u2,[],[])
        #print(qe)
        for a in qe:
            #print(a)
            if(len(a.split('/'))!=1):
                coeff*=convert(n,u2,a,1,i)/n
                return(convert(n,u1,a,coeff,i))
            return("no conversion")
    elif(len(u2.split('/'))!=1 and (len(u1.split('/'))==1)):
        qe=poss(u1,[],[])
        #print(qe)
        for a in qe:
            #print(a)
            if(len(a.split('/'))!=1):
                coeff*=convert(n,u1,a,1,i)/n
                return(convert(n,a,u2,coeff,i))
            return("no conversion")
print("enter number of units to be converted")
no=float(input())
print("enter type of units to be converted")
v2=input()
print("enter type of units to be converted to")
v1=input()
g=convert(no,v2,v1,1,0)
if(g==None or g=="no conversion"):
    print(g)
else:
    print(str(no)+" "+str(v2)+" is equal to "+str(g)+" "+str(v1))



