a,b,c = map(int,input().split())

day,hour,minute=11,11,11

elapsed_time=0
while True:
    if day>=a and hour >=b and minute>=c:
        break
    
    elapsed_time+=1
    minute+=1
    
    if minute==60:
        hour+=1
        minute=0
    if hour==24:
        day+=1
        hour=0

if elapsed_time==0:
    elapsed_time=-1

print(elapsed_time)


    


    