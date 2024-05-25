import pygame
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circle in a Circle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Circle properties
big_circle_center = (WIDTH // 2, HEIGHT // 2)
big_circle_radius = 200
small_circle_radius = 20

# Small circle initial position and velocity
small_circle_pos = [WIDTH // 2, HEIGHT // 2 - big_circle_radius + small_circle_radius]
velocity = [2, 2]

# Function to check if the small circle is within the big circle
def is_within_big_circle(pos, big_center, big_radius, small_radius):
    dist = math.sqrt((pos[0] - big_center[0])**2 + (pos[1] - big_center[1])**2)
    return dist + small_radius <= big_radius

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the small circle
    small_circle_pos[0] += velocity[0]
    small_circle_pos[1] += velocity[1]

    # Check for collision with the border of the big circle
    if not is_within_big_circle(small_circle_pos, big_circle_center, big_circle_radius, small_circle_radius):
        # Reverse velocity if collision occurs
        if not is_within_big_circle((small_circle_pos[0] - velocity[0], small_circle_pos[1]), big_circle_center, big_circle_radius, small_circle_radius):
            print("1", velocity)
            velocity[0] = -velocity[0]
        if not is_within_big_circle((small_circle_pos[0], small_circle_pos[1] - velocity[1]), big_circle_center, big_circle_radius, small_circle_radius):
            velocity[1] = -velocity[1]

    # Clear screen
    screen.fill(WHITE)

    # Draw big circle
    pygame.draw.circle(screen, BLUE, big_circle_center, big_circle_radius, 2)

    # Draw small circle
    pygame.draw.circle(screen, RED, small_circle_pos, small_circle_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
