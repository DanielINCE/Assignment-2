# Import Statements
import random
import matplotlib.pyplot as plt
import operator
import math
import pandas as pd
import my_modules.agentframework as agentframework
import my_modules.io as io

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 10

# Initialise agents
agents = []
for i in range(n_agents):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Move agents
for i in range(n_agents):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)
    
# Append to the list agents
agents.append([agents[0][0],agents[0][1]])

# Initialise variable x0
agents[0][0] = random.randint(0, 99)
print("agents[0][0]", agents[0][0])

# Initialise variable y0
agents[0][1] = random.randint(0, 99)
print("agents[0][1]", agents[0][1])
agents.append([agents[0][0], agents[0][1]])

# Set the pseudo-random seed for reproducibility
rn = random.random()
print(rn)
random.seed(1)

# Initialise variable x1
x1 = 1
print("x1", x1)

# Initialise variable y1
y1 = 1
print("y1", y1)

# Change x1 and y1 randomly
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
x0 = 0
print("x0", x0)
y0 = 0
print("y0", y0)
x1 = 3
print("x1", x1)
y1 = 4
print("y1", y1)


# Calculate the Euclidean distance between (x0, y0) and (x1, y1)

def pythag(x,y):
    sum = x * x + y * y
    z = math.sqrt(sum)

    return(z)

(solution) = pythag(3,4)

print(solution)


# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()

# Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))

# Define 'Get Distance'
def get_distance(x0, y0, x1, y1):
  
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Return the Sum the squared differences square rooted.
    return ((dx * dx) + (dy * dy)) ** 0.5

# Initialise max_distance
max_distance = 0
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)
        
# Define Agents
class Agent():
    pass

# Define Agent Class
def __str__(self):
    return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ")"


# Initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(agentframework.Agent())
    print(agents[i])
print(agents)

# Initialise variables
class Agent:
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        