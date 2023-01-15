import pygame
import math

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Inverse Kinematics Arm")

# Set arm parameters
arm1_length = 100
arm2_length = 75

# Set initial arm position
arm1_x = 400
arm1_y = 300
arm1_angle = math.pi/2

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
    dx = target_x - arm1_x
    dy = target_y - arm1_y
    angle1 = math.atan2(dy, dx)

    # Constrain angle to be between pi/4 and -pi + pi/4
    angle1 = max(math.pi/4, min(angle1, math.pi - math.pi/4))

    # Calculate position for second joint
    arm2_x = arm1_x + arm1_length * math.cos(arm1_angle)
    arm2_y = arm1_y + arm1_length * math.sin(arm1_angle)

    # Calculate angle for second joint
    dx = target_x - arm2_x
    dy = target_y - arm2_y
    angle2 = math.atan2(dy, dx)

    # Constrain angle to be between pi/2 and -pi/2
    angle2 = max(-math.pi/2, min(angle2, math.pi/2))
    arm2_angle = arm1_angle + angle1 + angle2

        # Draw arm on screen
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (arm1_x, arm1_y), (arm2_x, arm2_y), 5)
    pygame.draw.line(screen, (255, 0, 0), (arm2_x, arm2_y), (target_x, target_y), 5)
    pygame.draw.circle(screen, (0, 255, 0), (int(arm2_x), int(arm2_y)), 10, 0)
    # Draw target
    pygame.draw.circle(screen, (0, 255, 0), (target_x, target_y), 10)

    # Update display
    pygame.display.update()

# Quit pygame and exit program
pygame.quit()