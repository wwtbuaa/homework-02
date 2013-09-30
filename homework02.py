import sys

def maxsum_h(num,y1,x1):
    temp=[0]*x1
    s=0
    a=-1000000
    for q in range(y1):
        for i in range(y1):
            for j in range(i,y1):
                for k in range(x1):
                    temp[k]+=int(num[(j+q)%y1][k])
                    if(s+temp[k]<temp[k]):
                        s=0
                    s+=temp[k]
                    if(a<s):
                        a=s
                s=0
            s=0
            temp=[0]*x1
        s=0
        temp=[0]*x1
    return a

def maxsum_v(num,y1,x1):
    temp=[0]*x1
    s=0
    a=-1000000
    for t in range(x1):
        for i in range(y1):
            for j in range(i,y1):
                for k in range(x1):
                    temp[(k+t)%x1]+=int(num[j][(k+t)%x1])
                    if(s+temp[(k+t)%x1]<temp[(k+t)%x1]):
                        s=0
                    s+=temp[(k+t)%x1]
                    if(a<s):
                        a=s
                s=0
            s=0
            temp=[0]*x1
        s=0
        temp=[0]*x1
    return a

def maxsum_vh(num,y1,x1):
    temp=[0]*x1
    s=0
    a=-1000000
    for q in range(y1):
        for t in range(x1):
            for i in range(y1):
                for j in range(i,y1):
                    for k in range(x1):
                        temp[(k+t)%x1]+=int(num[(j+q)%y1][(k+t)%x1])
                        if(s+temp[(k+t)%x1]<temp[(k+t)%x1]):
                            s=0
                        s+=temp[(k+t)%x1]
                        if(a<s):
                            a=s
                    s=0
                s=0
                temp=[0]*x1
            s=0
            temp=[0]*x1
    return a

def maxsum(num,y1,x1):
    temp=[0]*x1
    s=0
    a=-1000000
    for i in range(y1):
        for j in range(i,y1):
            for k in range(x1):
                temp[k]+=int(num[j][k])
                if(s+temp[k]<temp[k]):
                    s=0
                s+=temp[k]
                if(a<s):
                    a=s
            s=0
        s=0
        temp=[0]*x1
    return a

def searchthrough(x,y,num,now_sum):
    global max_sum,pointgroup,min_x,min_y,visited
    max_sum = max(max_sum, now_sum)
    for i in [[0,-1],[1,0],[0,1],[-1,0]]:
        if x+i[0]>=min_x and x+i[0]<n1 and y+i[1]>=min_y and y+i[1]<n2 and visited[(x+i[0])%n1,(y+i[1])%n2]==0 and [(x+i[0])%n1,(y+i[1])%n2,num[(x+i[0])% n1][(y+i[1])%n2]] not in pointgroup:
            pointgroup.append([(x + i[0]) % n1, (y + i[1]) % n2, num[(x + i[0]) % n1][(y + i[1]) % n2]])
    if pointgroup == []:
        return
    pointgroup = sorted(pointgroup, key=lambda x: x[2])
    nextpoint = pointgroup.pop()
    if now_sum + nextpoint[2] > 0: 
        visited[nextpoint[0], nextpoint[1]] = 1
        searchthrough(nextpoint[0],nextpoint[1],num,now_sum + nextpoint[2])
        visited[nextpoint[0], nextpoint[1]] = 0
    else:
        return

def maxsum_a(num,x1,y1):    
    global min_x,min_y,max_sum,visited
    min_x = 0
    min_y = 0
    max_sum = 0
    now_sum = 0
    startpointx = []
    startpointy = []
    pointgroup = [] 
    for i in range(0,x1):
        for j in range(0,y1):
            visited[i,j] = 0
    for i in range(0,x1):
        for j in range(0,y1):
            if num[i][j] > 0:
                startpointx.append(i)
                startpointy.append(j)
    for pointx in startpointx:
        pointy = startpointy.pop()
        visited[pointx, pointy] = 1
        searchthrough(pointx,pointy,num,num[pointx][pointy])
    return max_sum

def maxsum_vha(num,x1,y1):   
    global min_x,min_y,max_sum,visited
    min_x = -n1
    min_y = -n2
    max_sum = 0
    now_sum = 0
    startpointx = []
    startpointy = []
    pointgroup = [] 
    for i in range(0,x1):
        for j in range(0,y1):
            visited[i,j] = 0
    for i in range(0,x1):
        for j in range(0,y1):
            if num[i][j] > 0:
                startpointx.append(i)
                startpointy.append(j)
    for pointx in startpointx:
        pointy = startpointy.pop()
        visited[pointx, pointy] = 1
        searchthrough(pointx,pointy,num,num[pointx][pointy])
    return max_sum

num=[]
V=H=A=False
if "\\v" in sys.argv[1:]:
    V=True
if "\\h" in sys.argv[1:]:
    H = True
if "\\a" in sys.argv[1:]:
    A = True
filename=sys.argv[-1]
f=open(filename,"r")
l=f.readline()
l=l.strip('\n').strip(",")
x=l
l=f.readline()
l=l.strip('\n').strip(",")
y=l
for i in range(int(x)):
    for j in range(int(y)):
        l=f.readline()
        l=l.strip('\n').split(",")
        num.append(l)
if V!=True and H!=True and A==True:
    max_sum=maxsum_a(num,int(x),int(y))
elif V==True and H!=True and A != True:
    max_sum = maxsum_v(num,int(x),int(y))
elif V!=True and H==True and A != True:
    max_sum = maxsum_h(num,int(x),int(y))
elif V==True and H==True and A != True:
    max_sum = maxsum_vh(num,int(x),int(y))
elif V==True and H==True and A == True:
    max_sum = maxsum_vha(num,int(x),int(y))
else:
    max_sum = maxsum(num,int(x),int(y))
print max_sum 