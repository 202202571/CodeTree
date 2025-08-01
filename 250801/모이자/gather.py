#입력
n = int(input())

#n개의 지점에 대해 거주자 수 입력받기
resident = list(map(int,input().split()))

#최소 이동거리 합
min_dist= []
for i in range(n):
    total =0
    #A,B,C,D,E의 각 지점에서의 거리 구하기
    for j in range(n):
        dist = resident[j]*abs(i-j)
        total+=dist

    min_dist.append(total)

result = min_dist[0]
for i in range(1,n):
    if result>min_dist[i]:
        result = min_dist[i]

print(result)
    