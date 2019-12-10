from panel import Panel


class Line(object):
    def __init__(self, x1, y1, x2, y2, color, screen):
        if (not isinstance(screen, Panel)):
            raise ValueError("screen must be an instance of class Panel!")
        else:
            self.color = color
            self.screen = screen
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
            self.distance = self.calculate_distance(x1, y1, x2, y2)

    # draw this Line on screen, BUT no refresh, need refresh to display later
    def draw(self):
        self.screen.draw_line(self.x1, self.y1, self.x2, self.y2, self.color)

    # draw this Line on screen, AND immediately refresh to display
    def draw_refresh(self):
        self.draw()
        self.screen.refresh()

    def change_color(self, color):
        self.color = color

    def calculate_distance(self, x1, y1, x2, y2):
        return abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2

    def get_distance(self):
        return self.distance
