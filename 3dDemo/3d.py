import pygame
import math

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Game")

# Define camera properties
camera_pos = [0, 0, 0]
camera_rot = [0, 0]

# Define a 3D cube
cube_vertices = [(-1, -1, -1), (-1, 1, -1), (1, 1, -1), (1, -1, -1), (-1, -1, 1), (-1, 1, 1), (1, 1, 1), (1, -1, 1)]
cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle camera movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera_pos[2] += math.sin(math.radians(camera_rot[1]))
        camera_pos[0] -= math.cos(math.radians(camera_rot[1]))
    if keys[pygame.K_s]:
        camera_pos[2] -= math.sin(math.radians(camera_rot[1]))
        camera_pos[0] += math.cos(math.radians(camera_rot[1]))
    if keys[pygame.K_a]:
        camera_pos[0] += math.sin(math.radians(camera_rot[1]))
        camera_pos[2] += math.cos(math.radians(camera_rot[1]))
    if keys[pygame.K_d]:
        camera_pos[0] -= math.sin(math.radians(camera_rot[1]))
        camera_pos[2] -= math.cos(math.radians(camera_rot[1]))
    if keys[pygame.K_UP]:
        camera_rot[0] -= .2
    if keys[pygame.K_DOWN]:
        camera_rot[0] += .2
    if keys[pygame.K_LEFT]:
        camera_rot[1] -= .2
    if keys[pygame.K_RIGHT]:
        camera_rot[1] += .2

    # Clear the screen
    screen.fill((0, 0, 0))

    # Rotate and project the cube vertices
    rotated_vertices = []
    for vertex in cube_vertices:
        x = vertex[0]
        y = vertex[1]
        z = vertex[2]

        # Rotate the vertex around the X axis
        y = y * math.cos(math.radians(camera_rot[0])) - z * math.sin(math.radians(camera_rot[0]))
        z = y * math.sin(math.radians(camera_rot[0])) + z * math.cos(math.radians(camera_rot[0]))

        # Rotate the vertex around the Y axis
        x = x * math.cos(math.radians(camera_rot[1])) - z * math.sin(math.radians(camera_rot[1]))
        z = x * math.sin(math.radians(camera_rot[1])) + z * math.cos(math.radians(camera_rot[1]))

        # Translate the vertex
        x += camera_pos[0]
        y += camera_pos[1]
        z += camera_pos[2]

        # Project the 3D coordinates to 2D screen coordinates
        f = 200 / z
        screen_x = int(x * f + screen.get_width() / 2)
        screen_y = int(y * f + screen.get_height() / 2)
        rotated_vertices.append((screen_x, screen_y))

    # Draw the edges of the cube
    for edge in cube_edges:
        pygame.draw.line(screen, (255, 255, 255), rotated_vertices[edge[0]], rotated_vertices[edge[1]], 2)

    # Update the display
    pygame.display.update()

pygame.quit()