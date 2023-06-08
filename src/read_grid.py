import numpy as np

domain_file = './PruebasGrid/FixedGoalInitialState/navigation_1_grid.net'

SMALL_ENOUGH = 0.02
GAMMA = 0.9
NOISE = 0.1

all_states = []
rewards = {}
actions = {}
policy = {}
V={}

with open(domain_file, 'r') as file:
    lines = file.readlines()
    nrows = len(lines)
    ncols = len(lines[0].strip().split())
    grid = np.zeros((nrows, ncols))
    for i in range(nrows):
        tokens = lines[i].strip().split()
        for j in range(ncols):
            all_states.append((i,j))
            if tokens[j] == "1":
                grid[i][j] = 1
                rewards[(i,j)] = -1
                V[(i,j)]= -1
                
            if tokens[j] == "2":
                grid[i][j] = 2
                rewards[(i,j)] = 1
                V[(i,j)] = 0
            elif tokens[j] == "3":
                grid[i][j] = 3
                V[(i,j)]= 1
            else:
                rewards[(i,j)] = 0
                V[(i,j)] = 0
                actions[(i,j)] = ('L', 'U', 'D', 'R')
                if (i == 0):
                    actions[(i,j)] = ('L', 'D', 'R')
                if (i == nrows - 1):
                    actions[(i,j)] = ('L', 'U', 'R')
                if (j == 0):
                    actions[(i,j)] = ('U', 'R', 'D')
                if (j == ncols  - 1):
                    actions[(i,j)] = ('U', 'L', 'D')
                if (i == 0 and j == 0):
                    actions[(i,j)] = ('D', 'R')
                if (i == 0 and j == ncols - 1):
                    actions[(i,j)] = ('D', 'L')
                if (i == (nrows - 1) and j == 0):
                    actions[(i,j)] = ('U', 'R')
                if (i == (nrows - 1) and j == ncols - 1):
                    actions[(i,j)] = ('L', 'U')

for s in actions.keys():
    policy[s] = np.random.choice(actions[s])

iteration = 0
while True:
    biggest_change = 0
    for s in all_states:
        if s in policy:

            old_v = V[s]
            new_v = 0

            for a in actions[s]:
                if a == 'U':
                    nxt = [s[0]-1, s[1]]
                if a == 'D':
                    nxt = [s[0]+1, s[1]]
                if a == 'L':
                    nxt = [s[0], s[1]-1]
                if a == 'R':
                    nxt = [s[0], s[1]+1]

                #Choose a new random action to do (transition probability)
                random_1=np.random.choice([i for i in actions[s] if i != a])
                if random_1 == 'U':
                    act = [s[0]-1, s[1]]
                if random_1 == 'D':
                    act = [s[0]+1, s[1]]
                if random_1 == 'L':
                    act = [s[0], s[1]-1]
                if random_1 == 'R':
                    act = [s[0], s[1]+1]

                #Calculate the value
                nxt = tuple(nxt)
                act = tuple(act)
                v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + (NOISE * V[act])))
                if v > new_v: #Is this the best action so far? If so, keep it
                    new_v = v
                    policy[s] = a

    #Save the best of all actions for the state
            V[s] = new_v
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))
            print(s, biggest_change)

#See if the loop should stop now
    if biggest_change < SMALL_ENOUGH:
        break
    iteration += 1

print(policy)

line_grid = ""
for i in range(nrows):
    for j in range(ncols):
        
        if((i!=0 and j!=19) and (i!=19 and j!=0)):
            line_grid += policy[(i,j)] + " "
    print(line_grid + '\n')
    line_grid = ""