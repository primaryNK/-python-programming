import objects.box
import physical_engine
import graphics_engine
import renderer
import pygame
import math
import player
import objects

WIDTH, HEIGHT = 800, 600
    
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
pygame.key.set_repeat(1, 1)

Player = player.Player

def update_movement(keys):
    rad_yaw = math.radians(Player.yaw)
    if keys.get(pygame.K_w, False):
        Player.x += math.sin(rad_yaw) * Player.speed
        Player.z += math.cos(rad_yaw) * Player.speed
    if keys.get(pygame.K_s, False):
        Player.x -= math.sin(rad_yaw) * Player.speed
        Player.z -= math.cos(rad_yaw) * Player.speed
    if keys.get(pygame.K_a, False):
        Player.x -= math.cos(rad_yaw) * Player.speed
        Player.z += math.sin(rad_yaw) * Player.speed
    if keys.get(pygame.K_d, False):
        Player.x += math.cos(rad_yaw) * Player.speed
        Player.z -= math.sin(rad_yaw) * Player.speed
    
    if keys.get(pygame.K_SPACE, False) and Player.on_ground:
        Player.velocity_y = Player.jump_velocity
        Player.on_ground = False

    Player.y += Player.velocity_y
    Player.velocity_y += Player.gravity

    if Player.y <= 1:  
        Player.y = 1
        Player.velocity_y = 0
        Player.on_ground = True

    for obj in physical_engine.PhysicalEngine.physical_objects:
        if Player.x >= obj[0] and Player.x <= obj[0] + obj[3].height and Player.z >= obj[2] and Player.z <= obj[2] + obj[3].depth:
            if Player.y >= obj[1] and Player[1] <= obj[1] + obj[3].height:
                Player.y = obj[1] + obj[4].height
                Player.velocity_y = 0
                Player.on_ground = True
                break

def handle_mouse_motion():
    mx, my = pygame.mouse.get_pos()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    Player.yaw += (mx - center_x) * Player.sensitivity
    Player.pitch += (center_y - my) * Player.sensitivity

    Player.pitch = max(-80, min(80, Player.pitch))

    pygame.mouse.set_pos([center_x, center_y]) 

keys = {}
running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Renderer")
clock = pygame.time.Clock()


renderer.add_box(0, 0, 5, 1, 2, 1)  # (x, y, z, width, height, depth)
physical_engine.PhysicalEngine.add_physical_object(physical_engine.PhysicalEngine, 0,0,5,objects.box.Box(1, 2, 1))
renderer.add_box(2, 0, 7, 1, 2, 1)
physical_engine.PhysicalEngine.add_physical_object(physical_engine.PhysicalEngine, 2, 0, 7, objects.box.Box(1, 2, 1))
renderer.add_box(-1, 0, 10, 1, 2, 1)
physical_engine.PhysicalEngine.add_physical_object(physical_engine.PhysicalEngine, -1, 0, 10, objects.box.Box(1, 2, 1))

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys[event.key] = True
        elif event.type == pygame.KEYUP:
            keys[event.key] = False

    update_movement(keys)
    handle_mouse_motion()

    renderer.draw_boxes_with_depth()
    renderer.flip()
    screen.fill((0, 0, 0))

    pygame.time.delay(16)  


pygame.quit()