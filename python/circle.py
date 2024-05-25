import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
big_circle_center = (WIDTH // 2, HEIGHT // 2)
big_circle_radius = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circle in a Circle")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


small_circle_radius = 20
small_circle_pos = [WIDTH // 2, HEIGHT // 2 - big_circle_radius + small_circle_radius]
speed = 2
velocity = [speed, speed]


def is_within_big_circle(pos, big_center, big_radius, small_radius):
    dist = math.sqrt((pos[0] - big_center[0])**2 + (pos[1] - big_center[1])**2)
    return dist + small_radius <= big_radius

def reflect_velocity(pos, vel, big_center):
    normal = [pos[0] - big_center[0], pos[1] - big_center[1]]
    normal_magnitude = math.sqrt(normal[0]**2 + normal[1]**2)
    normal = [normal[0] / normal_magnitude, normal[1] / normal_magnitude]
    
    dot_product = vel[0] * normal[0] + vel[1] * normal[1]
    
    new_vel = [
        vel[0] - 2 * dot_product * normal[0],
        vel[1] - 2 * dot_product * normal[1]
    ]
    return new_vel

running = True
clock = pygame.time.Clock()

def increase_speed():
    global speed
    if (speed < big_circle_radius / 2):
        speed += 0.5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    small_circle_pos[0] += velocity[0]
    small_circle_pos[1] += velocity[1]

    if not is_within_big_circle(small_circle_pos, big_circle_center, big_circle_radius, small_circle_radius):
        velocity = reflect_velocity(small_circle_pos, velocity, big_circle_center)
        increase_speed()
        vel_magnitude = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [speed * (velocity[0] / vel_magnitude), speed * (velocity[1] / vel_magnitude)]
        
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, big_circle_center, big_circle_radius, 2)

    pygame.draw.circle(screen, RED, small_circle_pos, small_circle_radius)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
