#입력
a = input()
arr = list(a)

count =0
for i in range(len(a)):
    if arr[i]=="(":
        for elem in arr[i+1::]:
            if elem==")":
                count+=1

print(count)

