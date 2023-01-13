import pygame
import random

# Initialize pygame
pygame.init()

# Set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Blu-ray DVD logo Python")

# Load the image
dvd_image = pygame.image.load("dvd_logo.png")

# Set the size of the image
dvd_image = pygame.transform.scale(dvd_image, (100, 50))

# Get the image rect
dvd_rect = dvd_image.get_rect()

# Set the DVD logo properties
dvd_rect.center = (size[0]/2, size[1]/2)
dvd_speed_x = 2
dvd_speed_y = 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the DVD logo
    dvd_rect.x = round(dvd_rect.x + dvd_speed_x)
    dvd_rect.y = round(dvd_rect.y + dvd_speed_y)

    # Check for collision with the edges of the screen
    if dvd_rect.left < 0 or dvd_rect.right > size[0]:
        dvd_speed_x = -dvd_speed_x
    if dvd_rect.top < 0 or dvd_rect.bottom > size[1]:
        dvd_speed_y = -dvd_speed_y

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw the DVD logo
    screen.blit(dvd_image, dvd_rect)

    # Update display
    pygame.display.flip()
    pygame.time.wait(30) # add a delay of 30 milliseconds

# Quit pygame
pygame.quit()