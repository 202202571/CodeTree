n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b)

count = 0
for i in range(n):
    if sorted_a[i]==sorted_b[i]:
        count+=1

if count==3:
    print("Yes")
else:
    print("No")