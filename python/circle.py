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

# Function to reflect the velocity
def reflect_velocity(pos, vel, big_center):
    # Calculate normal vector at the collision point
    normal = [pos[0] - big_center[0], pos[1] - big_center[1]]
    normal_magnitude = math.sqrt(normal[0]**2 + normal[1]**2)
    normal = [normal[0] / normal_magnitude, normal[1] / normal_magnitude]
    
    # Calculate dot product
    dot_product = vel[0] * normal[0] + vel[1] * normal[1]
    
    # Calculate reflection vector
    new_vel = [
        vel[0] - 2 * dot_product * normal[0],
        vel[1] - 2 * dot_product * normal[1]
    ]
    return new_vel

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
        # Reflect velocity if collision occurs
        velocity = reflect_velocity(small_circle_pos, velocity, big_circle_center)

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

# Function to reflect the velocity
def reflect_velocity(pos, vel, big_center):
    # Calculate normal vector at the collision point
    normal = [pos[0] - big_center[0], pos[1] - big_center[1]]
    normal_magnitude = math.sqrt(normal[0]**2 + normal[1]**2)
    normal = [normal[0] / normal_magnitude, normal[1] / normal_magnitude]
    
    # Calculate dot product
    dot_product = vel[0] * normal[0] + vel[1] * normal[1]
    
    # Calculate reflection vector
    new_vel = [
        vel[0] - 2 * dot_product * normal[0],
        vel[1] - 2 * dot_product * normal[1]
    ]
    return new_vel

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
        # Reflect velocity if collision occurs
        velocity = reflect_velocity(small_circle_pos, velocity, big_circle_center)

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
