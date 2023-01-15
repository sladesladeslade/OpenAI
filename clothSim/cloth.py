import pybullet as p
import numpy as np

# Create the simulation
physicsClient = p.connect(p.DIRECT)
p.setGravity(0,0,-10)

# Create a grid of point masses
num_points = 5
points = []
for i in range(num_points):
    for j in range(num_points):
        point = p.createMultiBody(baseMass=1, baseInertialFramePosition=[i, j, 0])
        points.append(point)

# Connect the point masses with distance constraints
for i in range(num_points*num_points):
    if (i+1) % num_points != 0:
        p.createConstraint(points[i], -1, points[i+1], -1, p.JOINT_POINT2POINT, [0,0,0], [1,0,0], [0,0,0])
    if i+num_points < num_points*num_points:
        p.createConstraint(points[i], -1, points[i+num_points], -1, p.JOINT_POINT2POINT, [0,0,0], [0,1,0], [0,0,0])

# Step the simulation
for i in range(1000):
    p.stepSimulation()

# Disconnect and clean up
p.disconnect()
