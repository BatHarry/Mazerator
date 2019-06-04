class Cell:

    def __init__(self, x, y, color=(255, 255, 255)):
        self.a = (x, y)
        self.b = (x+50, y)
        self.c = (x+50, y+50)
        self.d = (x, y+50)
        self.walls = [1, 1, 1, 1]
        self.visited = False
        self.color = color
