class Area:
    def __init__(self,name,address,region):
        self.name=name
        self.address=address
        self.region=region
    
    def __str__(self):
        return f"name {self.name}\naddr {self.address}\ncity {self.region}"


n = int(input())

areas = []
for _ in range(n):
    name,address,region = input().split()
    areas.append(Area(name,address,region))

#여러개의 정보를 담고 있는 객체 리스트의 경우, lambda 함수를 활용하여 무엇을 우선순위를 높게 두어
#이를 기반으로 정렬할 것인지 생각할 것(문제 해결의 핵심!)
areas = sorted(areas, key = lambda x:x.name)

print(areas[n-1])


    

    

