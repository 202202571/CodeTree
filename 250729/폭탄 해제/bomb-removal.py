class Bomb:
    def __init__(self,code,color,candle):
        self.code = code
        self.color = color
        self.candle =candle
    
    def __str__(self):
        return f"code : {self.code}\ncolor : {self.color}\nsecond : {self.candle}"

unlock_code,color,candle = input().split()
candle = int(candle)
unlock_bomb = Bomb(unlock_code,color,candle)

print(unlock_bomb)

