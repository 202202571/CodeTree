arr1=[]
arr2=[]
for i in range(3):
    a,b,c = map(int,input().split())
    arr1.append([a,b,c])

#입력에서 줄바꿈으로 인해 생긴 공백에도 신경을 쓸 것
empty_line = input()

for i in range(3):
    # 3*3 행렬을 요구하므로 입력값이 정확히 3개가 되도록 입력 format 작성
    x,y,z = map(int,input().split())
    arr2.append([x,y,z])

result=[
    [0]*3 for _ in range(3)
]

for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j] * arr2[i][j]

for i in range(3):
    for j in range(3):
        print(result[i][j],end=" ")
    print()