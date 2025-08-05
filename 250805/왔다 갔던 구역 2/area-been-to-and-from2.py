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
for i in range(n):
    past_position = position
    position+=distance_arr[i]*direction_arr[i]
    operand = -1 if past_position>=position else 1 
    for j in range(past_position,position,operand):
        grid[j+1000]+=1
        if grid[j+1000]==2:
            result+=1
    


print(result)
    

