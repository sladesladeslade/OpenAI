import pygame
import math

# Initialize pygame and create a window
pygame.init()
screen = pygame.display.set_mode((1600, 1200))
pygame.display.set_caption("Drifting Game")

# Load car image
car_img = pygame.image.load("C:\\Users\\spbro\\ChatGPT\\driftingGame\\car.png")
small_car_img = pygame.transform.scale(car_img, (car_img.get_width() // 2, car_img.get_height() // 2))
small_car_img = pygame.transform.rotate(small_car_img, 90)

# Set initial car position
car_x = 400
car_y = 500

# Set car's turning angle
car_angle = 90

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle arrow key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_angle += 5
    if keys[pygame.K_RIGHT]:
        car_angle -= 5
    if keys[pygame.K_UP]:
        car_x += math.cos(math.radians(car_angle)) * 1
        car_y += math.sin(math.radians(car_angle)) * 1
    if keys[pygame.K_DOWN]:
        car_x -= math.cos(math.radians(car_angle)) * 1
        car_y -= math.sin(math.radians(car_angle)) * 1

    # Draw car on screen
    screen.fill((0, 0, 0))
    rotated_car = pygame.transform.rotate(small_car_img, car_angle)
    screen.blit(rotated_car, (car_x, car_y))

    # Update display
    pygame.display.update()

# Quit pygame and exit program
pygame.quit()