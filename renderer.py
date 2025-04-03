import pygame
import math
import random

WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom 3D Renderer with Player Controls")

player_x, player_y, player_z = 0, 1, -5 
player_yaw, player_pitch = 0, 0 
jump_velocity = 0.5
player_velocity_y = 0
gravity = -0.02
speed = 0.1
sensitivity = 0.2

keys = {}

def project(x, y, z):
    dx = x - player_x
    dy = y - player_y
    dz = z - player_z

    rad_yaw = math.radians(player_yaw)
    transformed_x = dx * math.cos(rad_yaw) - dz * math.sin(rad_yaw)
    transformed_z = dx * math.sin(rad_yaw) + dz * math.cos(rad_yaw)

    rad_pitch = math.radians(player_pitch)
    transformed_y = dy * math.cos(rad_pitch) - transformed_z * math.sin(rad_pitch)
    transformed_z = dy * math.sin(rad_pitch) + transformed_z * math.cos(rad_pitch)


    if transformed_z <= 0:
        return None
    
    scale = 500 / max(transformed_z, 0.1)
    screen_x = WIDTH // 2 + transformed_x * scale
    screen_y = HEIGHT // 2 - transformed_y * scale

    return int(screen_x), int(screen_y)

def draw_line(x1, y1, z1, x2, y2, z2, color=(255, 255, 255)):
    p1 = project(x1, y1, z1)
    p2 = project(x2, y2, z2)
    if p1 and p2:
        pygame.draw.line(screen, color, p1, p2, 2)

def update_movement():
    global player_x, player_y, player_z, player_yaw ,player_pitch, player_velocity_y, on_ground

    rad_yaw = math.radians(player_yaw)
    if keys.get(pygame.K_w, False):
        player_x += math.sin(rad_yaw) * speed
        player_z += math.cos(rad_yaw) * speed
    if keys.get(pygame.K_s, False):
        player_x -= math.sin(rad_yaw) * speed
        player_z -= math.cos(rad_yaw) * speed
    if keys.get(pygame.K_a, False):
        player_x -= math.cos(rad_yaw) * speed
        player_z += math.sin(rad_yaw) * speed
    if keys.get(pygame.K_d, False):
        player_x += math.cos(rad_yaw) * speed
        player_z -= math.sin(rad_yaw) * speed
    
    if keys.get(pygame.K_SPACE, False) and on_ground:
        player_velocity_y = jump_velocity
        on_ground = False

    player_y += player_velocity_y
    player_velocity_y += gravity


    if player_y <= 1:  
        player_y = 1
        player_velocity_y = 0
        on_ground = True


def handle_mouse_motion():
    global player_yaw, player_pitch
    mx, my = pygame.mouse.get_pos()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    player_yaw += (mx - center_x) * sensitivity
    player_pitch += (center_y - my) * sensitivity

    player_pitch = max(-80, min(80, player_pitch))

    pygame.mouse.set_pos([center_x, center_y]) 

MAZE_SIZE = 10
maze = [[random.choice([0, 1]) for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
maze[0][0] = 0
maze[MAZE_SIZE-1][MAZE_SIZE-1] = 0

def draw_maze():
    for x in range(MAZE_SIZE):
        for z in range(MAZE_SIZE):
            if maze[x][z] == 1:
                draw_line(x, 0, z, x+1, 0, z) 
                draw_line(x+1, 0, z, x+1, 1, z) 
                draw_line(x+1, 1, z, x, 1, z) 
                draw_line(x, 1, z, x, 0, z) 



running = True
pygame.event.set_grab(True)  
pygame.mouse.set_visible(False)  

while running:
    screen.fill((0, 0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys[event.key] = True
        elif event.type == pygame.KEYUP:
            keys[event.key] = False

    update_movement()
    handle_mouse_motion()

    draw_maze()

    pygame.display.flip()  
    pygame.time.delay(16)  

pygame.quit()