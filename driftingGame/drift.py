import pygame
import os

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Drifting Game")

# Load car image
car_img = pygame.image.load("C:\\Users\\spbro\\ChatGPT\\driftingGame\\car.png")

# Set initial car position
car_x = 400
car_y = 500

# Set car velocity (drifting effect)
car_velocity = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move car based on velocity
    car_x += car_velocity

    # Check for drifting input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_velocity -= 0.5
    if keys[pygame.K_RIGHT]:
        car_velocity += 0.5

    # Draw car on screen
    screen.fill((0, 0, 0))
    screen.blit(car_img, (car_x, car_y))

    # Update display
    pygame.display.update()

# Quit pygame and exit program
pygame.quit()
