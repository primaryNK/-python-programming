import physical_engine
import graphics_engine
import renderer
import pygame
import math

WIDTH, HEIGHT = 800, 600

class GameEngine:
    def __init__(self, window_size=(800, 600), fps=60):
        self.window_size = window_size
        self.fps = fps
        self.physical_engine = physical_engine.PhysicalEngine()
        self.graphics_engine = graphics_engine.GraphicsEngine()

    def run(self):
        self.graphics_engine.initialize()
        while True:
            self.physical_engine.update_physics()
            # self.graphics_engine.render()
            # self.graphics_engine.handle_events()
            # self.graphics_engine.update_display()
            # self.graphics_engine.limit_fps(self.fps)
            if self.graphics_engine.should_exit():
                break
        self.graphics_engine.cleanup()
        self.physical_engine.cleanup()

if __name__ == "__main__":
    game_engine = GameEngine()
    # game_engine.run()

def update_movement(keys):
    rad_yaw = math.radians(player_yaw)
    if keys.get(pygame.K_w, False):
        renderer.Player.x += math.sin(rad_yaw) * renderer.Player.speed
        renderer.Player.z += math.cos(rad_yaw) * renderer.Player.speed
    if keys.get(pygame.K_s, False):
        renderer.Player.x -= math.sin(rad_yaw) * renderer.Player.speed
        renderer.Player.z -= math.cos(rad_yaw) * renderer.Player.speed
    if keys.get(pygame.K_a, False):
        renderer.Player.x -= math.cos(rad_yaw) * renderer.Player.speed
        renderer.Player.z += math.sin(rad_yaw) * renderer.Player.speed
    if keys.get(pygame.K_d, False):
        renderer.Player.x += math.cos(rad_yaw) * renderer.Player.speed
        renderer.Player.z -= math.sin(rad_yaw) * renderer.Player.speed
    
    if keys.get(pygame.K_SPACE, False) and on_ground:
        player_velocity_y = renderer.Player.jump_velocity
        on_ground = False

    player_y += player_velocity_y
    player_velocity_y += renderer.Player.gravity


    if player_y <= 1:  
        player_y = 1
        player_velocity_y = 0
        on_ground = True

def handle_mouse_motion():
    global player_yaw, player_pitch
    mx, my = pygame.mouse.get_pos()
    center_x, center_y = WIDTH // 2, HEIGHT // 2

    player_yaw += (mx - center_x) * renderer.Player.sensitivity
    player_pitch += (center_y - my) * renderer.Player.sensitivity

    player_pitch = max(-80, min(80, player_pitch))

    pygame.mouse.set_pos([center_x, center_y]) 

keys = {}
running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Renderer")
clock = pygame.time.Clock()

while running:
    renderer.screen.fill((0, 0, 0)) 
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

    renderer.update_movement(keys)
    renderer.handle_mouse_motion()

    renderer.draw_boxes_with_depth()

    pygame.display.flip()  
    pygame.time.delay(16)  


pygame.quit()