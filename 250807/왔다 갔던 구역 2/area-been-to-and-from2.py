#입력
n = int(input())
#초기 위치
position=0
directions = {
    'L':-1,
    'R':1
}
distance_arr =[]
direction_arr = []
for _ in range(n):
    distance,direction = input().split()
    distance=int(distance)
    distance_arr.append(distance)
    direction_arr.append(directions[direction])
grid = [0]*2001
result = 0

operand,position=0,0

for i in range(n):
    past_position = position
    position+=distance_arr[i]*direction_arr[i]
    #음수, 양수를 모두 고려해야할 때는 start,end 변수를 선언하여 min,max를 조정하며 start,end의 대소관계를 확실히 하기
    start = min(past_position,position)
    end = max(past_position,position)
    operand = -1 if start>=end else 1
    for j in range(start,end,operand):
        grid[j+1000]+=1


for elem in grid:
    if elem>=2:
        result+=1
    
print(result)
    


    

