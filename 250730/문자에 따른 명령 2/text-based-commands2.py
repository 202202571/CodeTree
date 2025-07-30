arr = list(input())

dir_mapper = {
    'R':0,
    'L':1,
}

dx,dy=[1,-1,0],[0,0,1]
dir_num=2
x,y=0,0
for i in range(len(arr)):
    if arr[i]!='F':
        dir_num = dir_mapper[arr[i]]
    else:
        x,y = x+dx[dir_num],y+dy[dir_num]

print(f"{x} {y}")
