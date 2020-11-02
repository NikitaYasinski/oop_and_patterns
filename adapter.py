class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee
        self.lights = []
        self.obstacles = []

    def lighten(self, grid):
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    self.lights.append((y, x))

                if grid[x][y] == -1:
                    self.obstacles.append((y, x))

        self.adaptee.set_dim((len(grid[0]), len(grid)))
        self.adaptee.set_lights(self.lights)
        self.adaptee.set_obstacles(self.obstacles)
        return self.adaptee.generate_lights()

