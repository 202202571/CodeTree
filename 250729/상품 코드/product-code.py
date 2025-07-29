class Item:
    def __init__(self,name="codetree",code=50):
        self.name=name
        self.code=code
    
    def __str__(self):
        return f"product {self.code} is {self.name}"

item_name,item_code=input().split()
item_code=int(item_code)

item1 = Item()
item2 = Item(item_name,item_code)

print(item1)
print(item2)