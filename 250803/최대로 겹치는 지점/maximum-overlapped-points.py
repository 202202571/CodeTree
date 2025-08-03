#입력(선분의 개수)
n = int(input())

#직선(초기 값)
straight_line = [0]*101

for _ in range(n):
    x1,x2 = tuple(map(int,input().split()))
    for i in range(x1,x2+1):
        straight_line[i]+=1
    
answer = max(straight_line)

print(answer)

