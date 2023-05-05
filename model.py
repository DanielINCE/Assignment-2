# Import statements
import my_modules.agentframework as af
import my_modules.io as io 

# Import time
import time

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

# Set the pseudo-random seed for reproducibility
import random
rn = random.random()
print(rn)
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Define variables
def(n_row, n_col, environment)

# Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 3

n_iterations = 100

# Initialise agents
agents = []
for i in range(n_iterations):
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
for i in range(n_iterations):
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
import random
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
import math
def pythag(x,y):
    sum = x * x + y * y
    z = math.sqrt(sum)

    return(z)

(solution) = pythag(3,4)

print(solution)

import matplotlib.pyplot as plt
import operator

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = min(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = min(agents, key=operator.itemgetter(1))
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

# Set time variable
start = time.perf_counter()

# Initialise min_distance

min_distance = math.inf
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
if i < j:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        min_distance = min(min_distance, distance)
        print("min_distance", min_distance)

print("i", i, "j", j)

# calculate and report a time interval
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Apply movement constraints.
if agents[i][0] < x_min:
    agents[i][0] = x_min
if agents[i][1] < y_min:
    agents[i][1] = y_min
if agents[i][0] > x_max:
    agents[i][0] = x_max
if agents[i][1] > y_max:
    agents[i][1] = y_max
    
# Plot environment
plt.imshow(environment)

# initialise 'x_max' 
x_max = n_cols - 1
    
# initialise 'y_max' 
y_max = n_rows - 1

# Flip the y-axis
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)

# Initialise Agents
def __init__(self, i, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    i : Integer
        To be unique to each instance.
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.
    Returns
    -------
    None.
    """
    self.i = i
    tnc = int(n_cols / 3)
    self.x = random.randint(tnc - 1, (2 * tnc) - 1)
    tnr = int(n_rows / 3)
    self.y = random.randint(tnr - 1, (2 * tnr) - 1)


# Define Agents
def __init__(self, i, environment, n_rows, n_cols):
"""
The constructor method.

Parameters
----------
i : Integer
    To be unique to each instance.
environment : List
    A reference to a shared environment
n_rows : Integer
    The number of rows in environment.
n_cols : Integer
    The number of columns in environment.

Returns
-------
None.

"""
self.i = i
self.environment = environment
tnc = int(n_cols / 3)
self.x = random.randint(tnc - 1, (2 * tnc) - 1)
tnr = int(n_rows / 3)
self.y = random.randint(tnr - 1, (2 * tnr) - 1)
self.store = 0

# Agent class
def eat(self):
    if self.environment[self.y][self.x] >= 10:
        self.environment[self.y][self.x] -= 10
        self.store += 10