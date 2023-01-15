import pymunk
import pymunk.pygame_util

# Create the simulation
space = pymunk.Space()
space.gravity = (0,0)

# Create a grid of point masses
num_points = 5
points = []
for i in range(num_points):
    for j in range(num_points):
        point = pymunk.Body(mass=float("999"), moment=0)
        point.position = (i, j)
        space.add(point)
        points.append(point)

# Connect the point masses with distance constraints
for i in range(num_points*num_points):
    if (i+1) % num_points != 0:
        constraint = pymunk.PinJoint(points[i], points[i+1], (0,0), (1,0))
        space.add(constraint)
    if i+num_points < num_points*num_points:
        constraint = pymunk.PinJoint(points[i], points[i+num_points], (0,0), (0,1))
        space.add(constraint)

# Step the simulation
for i in range(1000):
    space.step(1/60)
