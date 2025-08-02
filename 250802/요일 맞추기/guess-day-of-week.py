m1,d1,m2,d2 = map(int,input().split())

num_of_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

day=["Sun","Mon","Tue","Wed","Thur","Fri","Sat"]
index = 0
while m1==m2 and d1==d2:
    if m1<m2:
        d1+=1
    elif m1>m2:
        d1-=1
    else:
        if d1>d2:
            d1-=1
        elif d1<d2:
            d1+=1

    if d1>num_of_month[m1]:
        m1+=1
        d1=1

    if d1==0:
        m1-=1
        d1=num_of_month[m1]
    
    index = (index+1)%7

print(day[index])
    
