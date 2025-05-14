import objects
class PhysicalEngine:
    physical_objects = []

    def __init__(self):
        self.physical_objects = []

    def add_physical_object(self, x, y, z, box):
        self.physical_objects.append({x, y, z, box})

    def update(self):
        for obj in self.physical_objects:
            obj.update()
            obj.check_collisions(self.physical_objects)
            obj.apply_gravity()
            obj.update_position()
            obj.update_velocity()
            obj.update_rotation()
            obj.update_scale()
            obj.update_transform()
            obj.update_renderable()
            obj.update_physics()
            obj.update_physics_renderable()
            obj.update_physics_transform()
            obj.update_physics_velocity()
            obj.update_physics_rotation()
            obj.update_physics_scale()

def update_physics(obj):
    # Update the physics properties of the object
    pass


def main():
    engine = PhysicalEngine()
    # Add physical objects to the engine
    # For example: engine.add_physical_object(PhysicalObject(...))
    # Run the update loop
    while True:
        engine.update()
    
