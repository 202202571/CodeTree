#입력

n = int(input())

#키(n개 만큼)
height = list(map(int,input().split()))

count=0
for i in range(n):
        
    for j in range(i+1,n):
        for k in range(j+1,n):
            if height[i]<=height[j] and height[j]<=height[k]:
                count+=1

print(count)

