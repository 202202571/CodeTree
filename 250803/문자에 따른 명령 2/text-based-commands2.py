arr = list(input())

dir_mapper = {
    'R':0,
    'L':1,
}

dx,dy=[1,-1,0],[0,0,1]
dir_num=2
x,y=0,0
for i in range(len(arr)):
    if arr[i]=='L':
        dir_num -=1
    elif arr[i]=='R':
        dir_num +=1
    else:
        x,y = x+dx[dir_num],y+dy[dir_num]

print(f"{x} {y}")
