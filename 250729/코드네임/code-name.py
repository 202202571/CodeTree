class Agent:
    def __init__(self,name="", score=0):
        self.name=name
        self.score=score
    
    def __str__(self):
        return f"{self.name} {self.score}"

agents =[]

for _ in range(5):
    name,score = input().split()
    score = int(score)
    agents.append(Agent(name,score))

least = agents[0].score
index = 0
for i in range(5):
    if least > agents[i].score:
        least = agents[i].score
        index=i

print(agents[index])
    

