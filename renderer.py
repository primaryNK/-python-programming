import pygame
import math
import random


WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom 3D Renderer with Player Controls")

class Player:
    def __init__(self, x, y, z, yaw, pitch):
        self.x = x
        self.y = y
        self.z = z
        self.yaw = yaw
        self.pitch = pitch
        self.velocity_y = 0
        self.on_ground = True
        self.gravity = -0.02
        self.jump_velocity = 0.5
        self.speed = 0.1
        self.sensitivity = 0.2
    
    def player_coordiates(x,y,z,yaw,pitch):
        x = x
        y = y
        z = z
        yaw = yaw
        pitch = pitch
    

def project(x, y, z):
    dx = x - Player.x
    dy = y - Player.y
    dz = z - Player.z

    rad_yaw = math.radians(Player.player_yaw)
    transformed_x = dx * math.cos(rad_yaw) - dz * math.sin(rad_yaw)
    transformed_z = dx * math.sin(rad_yaw) + dz * math.cos(rad_yaw)

    rad_pitch = math.radians(Player.player_pitch)
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

def draw_visible_box_edges(x, y, z, width, height, depth, color=(255, 255, 255)):
    # 상자의 8개 꼭짓점 좌표 계산
    vertices = [
        (x, y, z),  # front-bottom-left
        (x + width, y, z),  # front-bottom-right
        (x, y + height, z),  # front-top-left
        (x + width, y + height, z),  # front-top-right
        (x, y, z + depth),  # back-bottom-left
        (x + width, y, z + depth),  # back-bottom-right
        (x, y + height, z + depth),  # back-top-left
        (x + width, y + height, z + depth),  # back-top-right
    ]

    # 각 면의 꼭짓점 인덱스 (시계 방향)
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0),  # front edges
        (4, 5), (5, 7), (7, 6), (6, 4),  # back edges
        (0, 4), (1, 5), (2, 6), (3, 7),  # connecting edges
    ]

    # 보이는 모서리만 그리기
    for edge in edges:
        draw_line(
            vertices[edge[0]][0], vertices[edge[0]][1], vertices[edge[0]][2],
            vertices[edge[1]][0], vertices[edge[1]][1], vertices[edge[1]][2],
            color
        )



# MAZE_SIZE = 10
# maze = [[random.choice([0, 1]) for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
# maze[0][0] = 0
# maze[MAZE_SIZE-1][MAZE_SIZE-1] = 0

# def draw_maze_with_depth():
#     # 박스를 Z값(깊이) 기준으로 정렬
#     boxes = []
#     for x in range(MAZE_SIZE):
#         for z in range(MAZE_SIZE):
#             if maze[x][z] == 1:
#                 # 중심점의 Z값 계산
#                 center_z = z + 0.5
#                 boxes.append((center_z, x, z))

#     # Z값 기준으로 정렬 (가까운 Z값이 먼저 그려지도록 내림차순 정렬)
#     boxes.sort(reverse=True, key=lambda box: box[0])

#     # 정렬된 순서대로 박스 그리기
#     for _, x, z in boxes:
#         draw_visible_box_edges(x, 0, z, 1, 2, 1, color=(255, 255, 255))

boxes = []

def add_box(x, y, z, width, height, depth):
    """
    상자의 정보를 추가하는 함수.
    :param x: 상자의 X 좌표
    :param y: 상자의 Y 좌표
    :param z: 상자의 Z 좌표
    :param width: 상자의 너비
    :param height: 상자의 높이
    :param depth: 상자의 깊이
    """
    boxes.append((x, y, z, width, height, depth))

def draw_boxes_with_depth():
    """
    Z값(깊이)을 기준으로 상자를 정렬한 뒤, 보이는 모서리만 렌더링하는 함수.
    """
    # Z값 기준으로 정렬 (가까운 Z값이 먼저 그려지도록 내림차순 정렬)
    sorted_boxes = sorted(boxes, key=lambda box: box[2], reverse=True)

    # 정렬된 순서대로 상자 그리기
    for x, y, z, width, height, depth in sorted_boxes:
        draw_visible_box_edges(x, y, z, width, height, depth, color=(255, 255, 255))


# 예제: 상자 추가
add_box(0, 0, 5, 1, 2, 1)  # (x, y, z, width, height, depth)
add_box(2, 0, 7, 1, 2, 1)
add_box(-1, 0, 10, 1, 2, 1)

running = True
pygame.event.set_grab(True)  
pygame.mouse.set_visible(False)
running = True
pygame.event.set_grab(True)  
pygame.mouse.set_visible(False)  
