n = int(input())

arr = list(map(int,input().split()))

sort_arr = sorted(arr)
biggest = sort_arr[0]+sort_arr[2*n-1]
value =0
for i in range(1,2*n):
    value = sort_arr[i]+sort_arr[2*n-1-i]
    if biggest<value:
        biggest = value

print(biggest)
