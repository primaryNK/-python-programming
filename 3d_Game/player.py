class Player:
    x= 0
    y= 0
    z= 0
    yaw= 0
    pitch= 0
    velocity_y= 0
    on_ground= True
    gravity= -0.02
    jump_velocity= 0.5
    speed= 0.1
    sensitivity= 0.2
    

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