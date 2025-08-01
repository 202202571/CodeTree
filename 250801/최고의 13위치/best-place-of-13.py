#입력
n = int(input())

board =[
    list(map(int,input().split())) for _ in range(n)
]

maximum=0
for i in range(n):
    for j in range(n-2):
        maximum = max(maximum,board[i][j]+board[i][j+1]+board[i][j+2])

print(maximum)