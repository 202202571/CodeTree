#입력
r,c = map(int,input().split())

board = [
    list(input().split()) for _ in range(r)
]

count = 0
for i in range(r):
    for j in range(c):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if board[0][0]=='W' and board[i][j]=='B' and board[k][l]=='W' and board[4][4]=='B':
                    count+=1
                if board[0][0]=='B' and board[i][j]=='W' and board[k][l]=='B' and board[4][4]=='W':
                    count+=1


print(count)

