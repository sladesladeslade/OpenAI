import pygame
import math

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Inverse Kinematics Arm")

# Set arm parameters
arm_length1 = 100
arm_length2 = 75

# Set initial arm position
arm_x1 = 400
arm_y1 = 300
arm_x2 = arm_x1 + arm_length1
arm_y2 = arm_y1

# Set target position
target_x = 600
target_y = 400

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle arrow key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        target_x -= 5
    if keys[pygame.K_RIGHT]:
        target_x += 5
    if keys[pygame.K_UP]:
        target_y -= 5
    if keys[pygame.K_DOWN]:
        target_y += 5

    # Calculate angle for first joint
    dx = target_x - arm_x1
    dy = target_y - arm_y1
    angle1 = math.atan2(dy, dx)

    # Calculate position for second joint
    arm_x2 = arm_x1 + arm_length1 * math.cos(angle1)
    arm_y2 = arm_y1 + arm_length1 * math.sin(angle1)

    # Calculate angle for second joint
    dx = target_x - arm_x2
    dy = target_y - arm_y2
    angle2 = math.atan2(dy, dx)

    # Draw arm on screen
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (arm_x1, arm_y1), (arm_x2, arm_y2), 5)
    pygame.draw.line(screen, (255, 0, 0), (arm_x2, arm_y2), (target_x, target_y), 5)

    # Draw target
    pygame.draw.circle(screen, (0, 255, 0), (target_x, target_y), 10)

    # Update display
    pygame.display.update()

# Quit pygame and exit program
pygame.quit()
