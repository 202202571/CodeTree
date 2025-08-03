#입력
n,b = tuple(map(int,input().split()))

#변환 과정
result =[]
while True:
    if n<b:
        break
    result.append(n%b)
    n=n//b

result.append(n)
#출력
for elem in result[::-1]:
    print(elem,end="")