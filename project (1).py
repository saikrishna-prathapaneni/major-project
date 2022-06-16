import itertools
lst=[]
n = int(input("Enter number of ships arraiving : "))
for i in range(0, n):
    ele = input()
    lst.append(ele)
e=int(input("enter the number of docking stations which are empty:"))
if((e==5 and n<=5) or (n<e and e!=0)):
        dic={}
        for i in range(0,e):
            key=input("enter the station number:")
            value=int(input("enter the number of rows empty from the crane"))
            dic[key]=value
        sorted_score= sorted(dic.items(),key = lambda kv: kv[1])
        sorted_score.reverse()
        out=list(itertools.zip_longest(lst,sorted_score))
        print(out)

if((e==5 and n>=5) or (n>e and e!=0)):
    delay=[]
    print('enter all the delays of ships:')
    for i in range(0,n):
        ele=int(input())
        delay.append(ele)
    score1=[]
    for i in range(0,n):
        if(delay[i]==6 or delay[i]==5):
            s1=100
            score1.append(s1)
        if(delay[i]==4 or delay[i]==3):
            s1=90
            score1.append(s1)
        if(delay[i]==2 or delay[i]==1):
            s1=80
            score1.append(s1)
        if(delay[i]==0):
            s1=70
            score1.append(s1)
        if(delay[i]<0):
            s1=0
            score1.append(s1)
    dist=[]
    print("enter the distances of all the ships:")
    for i in range(0,n):
        ele=int(input())
        dist.append(ele)
    score2=[]
    for i in range(0,n):
        if(75<=dist[i]<100):
            s2=60
            score2.append(s2)
        if(50<=dist[i]<75):
            s2=70
            score2.append(s2)
        if(25<=dist[i]<50):
            s2=80
            score2.append(s2)
        if(0<=dist[i]<25):
            s2=90
            score2.append(s2)
    lo=[]
    print("enter the loads of all ships:")
    for i in range(0,n):
        ele=int(input())
        lo.append(ele)
    score3=[]
    for i in range(0,n):
        if(lo[i]<100):
            s3=70
            score3.append(s3)
        if(100<lo[i]<200):
            s3=60
            score3.append(s3)
        if(200<lo[i]<300):
            s3=50
            score3.append(s3)
        if(300<lo[i]<400):
            s3=30
            score3.append(s3)
        if(400<lo[i]<500):
            s3=10
            score3.append(s3)
    score=[score1[i]+score2[i]+score3[i] for i in range(len(score1))]
    out={lst[i]:score[i] for i in range(len(lst))}
    print(out)
if(e==0):
    delay=[]
    print('enter all the delays of ships:')
    for i in range(0,n):
        ele=int(input())
        delay.append(ele)
    score1=[]
    for i in range(0,n):
        if(delay[i]==6 or delay[i]==5):
            s1=100
            score1.append(s1)
        if(delay[i]==4 or delay[i]==3):
            s1=90
            score1.append(s1)
        if(delay[i]==2 or delay[i]==1):
            s1=80
            score1.append(s1)
        if(delay[i]==0):
            s1=70
            score1.append(s1)
        if(delay[i]<0):
            s1=0
            score1.append(s1)
    dist=[]
    print("enter the distances of all the ships:")
    for i in range(0,n):
        ele=int(input())
        dist.append(ele)
    score2=[]
    for i in range(0,n):
        if(75<=dist[i]<100):
            s2=60
            score2.append(s2)
        if(50<=dist[i]<75):
            s2=70
            score2.append(s2)
        if(25<=dist[i]<50):
            s2=80
            score2.append(s2)
        if(0<=dist[i]<25):
            s2=90
            score2.append(s2)
    lo=[]
    print("enter the loads of all ships:")
    for i in range(0,n):
        ele=int(input())
        lo.append(ele)
    score3=[]
    for i in range(0,n):
        if(lo[i]<100):
            s3=70
            score3.append(s3)
        if(100<lo[i]<200):
            s3=60
            score3.append(s3)
        if(200<lo[i]<300):
            s3=50
            score3.append(s3)
        if(300<lo[i]<400):
            s3=30
            score3.append(s3)
        if(400<lo[i]<500):
            s3=10
            score3.append(s3)
    unlo=[]
    print("enter the loads of all ships:")
    for i in range(0,n):
        ele=int(input())
        unlo.append(ele)
    score4=[]
    for i in range(0,n):
        if(unlo[i]<60):
            s4=80
            score4.append(s4)
        if(60<unlo[i]<120):
            s4=70
            score4.append(s4)
        if(120<unlo[i]<180):
            s4=60
            score4.append(s4)
        if(180<unlo[i]<240):
            s4=40
            score4.append(s4)
        if(240<unlo[i]<300):
            s4=10
            score4.append(s4)
    score=[score1[i]+score2[i]+score3[i]+score4[i] for i in range(len(score1))]
    out={lst[i]:score[i] for i in range(len(lst))}
    print(out)
   
        
        

