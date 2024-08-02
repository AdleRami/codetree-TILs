class Agent:
    def __init__(self, codename="", score=0):
        self.codename = codename
        self.score = score

agents = []
for _ in range(5):
    code_name, score = tuple(input().split())
    agents.append(Agent(code_name, int(score)))

min_idx = 0
for i in range(1,5):
    #print(min_idx,agents[i].codename,agents[i].score)
    if agents[min_idx].score > agents[i].score:
        min_idx = i

print(agents[min_idx].codename, agents[min_idx].score)