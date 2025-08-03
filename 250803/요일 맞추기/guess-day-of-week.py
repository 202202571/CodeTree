m1,d1,m2,d2 = map(int,input().split())

num_of_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

day=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
index = 1
diff = 0
#이전인 경우(달부터 차이나는 case)
if m1>m2:
    diff = num_of_month[m2]-d2+d1
    for i in range(m2+1,m1):
        diff += num_of_month[i]
    index = (7-(diff-index))%7

#이후인 경우(달부터 차이나는 case)
elif m1<m2:
    diff = num_of_month[m1]-d1+d2
    for i in range(m1+1,m2):
        diff+=num_of_month[i]
    index = (index+diff)%7

#달은 같은데 다른 일이 다른 경우
else:
    diff = abs(d1-d2)
    if index-diff>=0:
        index = (index-diff)%7
    else:
        index = (7-(diff-index))%7

    
    
print(day[index])
    
