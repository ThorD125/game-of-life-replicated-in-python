import pygame as py_game
import math
import random
import threading

py_game.init()

WIDTH, HEIGHT = 800, 600
speed = 2
line_width = 5


big_circle_center = (WIDTH // 2, HEIGHT // 2)
big_circle_radius = 200

screen = py_game.display.set_mode((WIDTH, HEIGHT))
py_game.display.set_caption("Bouncing Circle in a Circle")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CURRENT_COLOR = BLUE

small_circle_radius = 20
small_circle_pos = [WIDTH // 2, HEIGHT // 2 -
                    big_circle_radius + small_circle_radius]
velocity = [speed, speed]

clock = py_game.time.Clock()
angle = math.pi / 5
collision_point = None

def play_sound(mp3_file, volume=0.5):
    def _play():
        py_game.mixer.init()
        py_game.mixer.music.load(mp3_file)
        py_game.mixer.music.set_volume(volume)
        py_game.mixer.music.play()
        while py_game.mixer.music.get_busy():
            py_game.time.Clock().tick(10)
    sound_thread = threading.Thread(target=_play)
    sound_thread.start()

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

def increase_speed():
    global speed
    if (speed < big_circle_radius / 2):
        speed += 0.5

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
def calculate_line_points(big_center, big_radius, angle):
    x = big_center[0] + big_radius * math.cos(angle)
    y = big_center[1] + big_radius * math.sin(angle)
    return (x, y)


def draw_line(circle_position, width):
    if collision_point:
        py_game.draw.line(screen, CURRENT_COLOR, collision_point, circle_position, width)

def calculate_collision_point(pos, big_center, big_radius, small_radius):
    normal = [pos[0] - big_center[0], pos[1] - big_center[1]]
    normal_magnitude = math.sqrt(normal[0]**2 + normal[1]**2)
    
    global collision_point
    collision_point = [
        big_center[0] + (big_radius) * (normal[0] / normal_magnitude),
        big_center[1] + (big_radius) * (normal[1] / normal_magnitude)
    ]
    
running = True
while running:
    for event in py_game.event.get():
        if event.type == py_game.QUIT:
            running = False

    small_circle_pos[0] += velocity[0]
    small_circle_pos[1] += velocity[1]

    if not is_within_big_circle(small_circle_pos, big_circle_center, big_circle_radius, small_circle_radius):
        calculate_collision_point(small_circle_pos, big_circle_center, big_circle_radius, small_circle_radius)        
        velocity = reflect_velocity(
            small_circle_pos, velocity, big_circle_center)
        increase_speed()
        vel_magnitude = math.sqrt(velocity[0]**2 + velocity[1]**2)
        velocity = [speed * (velocity[0] / vel_magnitude),
                    speed * (velocity[1] / vel_magnitude)]
        CURRENT_COLOR = random_color()
        play_sound("sound/lq.mp3")


    screen.fill(BLACK)

    draw_line(small_circle_pos, line_width)
    py_game.draw.circle(screen, CURRENT_COLOR,
                    big_circle_center, big_circle_radius, line_width)

    py_game.draw.circle(screen, WHITE, small_circle_pos, small_circle_radius)
    py_game.display.flip()
    clock.tick(60)
    
py_game.quit()
