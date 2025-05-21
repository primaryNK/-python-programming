class benz:
    speed = 0
    color = "red"

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    def show(self):
        print(f"(class_Benz) speed: {self.speed}, color: {self.color}")

class oudi:
    speed = 0
    color = "blue"

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0

    def show(self):
        print(f"(class_Oudi) speed: {self.speed}, color: {self.color}")