import RPi.GPIO as GPIO
import time

# Class define the LED panel


class Panel(object):
    # time variable
    delay = 0.000001
    frame_duration = 1.0
    # Define size of Screen
    width = 16
    length = 32
    # Define Pins
    # RGB Pin
    red1_pin = 27
    green1_pin = 15
    blue1_pin = 22
    red2_pin = 23
    green2_pin = 24
    blue2_pin = 25
    # Address Pin
    a_pin = 7
    b_pin = 8
    c_pin = 9
    # Other Pin
    clock_pin = 3
    latch_pin = 4
    oe_pin = 2

    def __init__(self):
        # init screen matrix
        self.screen = [[0 for x in range(self.length)]
                       for x in range(self.width)]
        # GPIO setups
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.red1_pin, GPIO.OUT)
        GPIO.setup(self.green1_pin, GPIO.OUT)
        GPIO.setup(self.blue1_pin, GPIO.OUT)
        GPIO.setup(self.red2_pin, GPIO.OUT)
        GPIO.setup(self.green2_pin, GPIO.OUT)
        GPIO.setup(self.blue2_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.a_pin, GPIO.OUT)
        GPIO.setup(self.b_pin, GPIO.OUT)
        GPIO.setup(self.c_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.oe_pin, GPIO.OUT)

    def clean_gpio(self):
        GPIO.cleanup()

    def clock(self):
        GPIO.output(self.clock_pin, 1)
        GPIO.output(self.clock_pin, 0)

    def latch(self):
        GPIO.output(self.latch_pin, 1)
        GPIO.output(self.latch_pin, 0)

    def bits_from_int(self, x):
        a_bit = x & 1
        b_bit = x & 2
        c_bit = x & 4
        return (a_bit, b_bit, c_bit)

    def set_row(self, row):
        # time.sleep(self.delay)
        a_bit, b_bit, c_bit = self.bits_from_int(row)
        GPIO.output(self.a_pin, a_bit)
        GPIO.output(self.b_pin, b_bit)
        GPIO.output(self.c_pin, c_bit)
        # time.sleep(self.delay)

    def set_color_top(self, color):
        # time.sleep(self.delay)
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red1_pin, red)
        GPIO.output(self.green1_pin, green)
        GPIO.output(self.blue1_pin, blue)
        # time.sleep(self.delay)

    def set_color_bottom(self, color):
        # time.sleep(self.delay)
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red2_pin, red)
        GPIO.output(self.green2_pin, green)
        GPIO.output(self.blue2_pin, blue)
        # time.sleep(self.delay)

    # refresh whole LED panel
    def refresh(self):
        for row in range(8):
            GPIO.setmode(GPIO.BCM)
            GPIO.output(self.oe_pin, 1)
            self.set_color_top(0)
            self.set_row(row)
            # time.sleep(self.delay)
            for col in range(32):
                self.set_color_top(self.screen[row][col])
                self.set_color_bottom(self.screen[row+8][col])
                self.clock()
            #GPIO.output(self.oe_pin, 0)
            self.latch()
            GPIO.output(self.oe_pin, 0)
            time.sleep(self.delay)

    # keep refresh() for frame_duration
    # call this method every time a new screen should be displayed on the panel
    def frame(self):
        start_time = time.time()
        run = True
        while run:
            self.refresh()
            now_time = time.time()
            if (now_time - start_time > self.frame_duration):
                run = False

    def fill_rectangle(self, x1, y1, x2, y2, color):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                self.screen[y][x] = color

    # set one LED at (x, y) to color
    def set(self, x, y, color):
        # 0 <= x <= 31
        # 0 <= y <= 15
        # colors:
        # Black = 0
        # Red = 1
        # Green = 2
        # Yellow = 3
        # Blue = 4
        # Magenta = 5
        # Cyan = 6
        # White = 7
        if (x >= 0 and x < self.length and y >= 0 and y < self.width):
            self.screen[y][x] = color

    # generate a Node in tree or graph at (x, y) with color
    def draw_node(self, x, y, color):
        # delta of a cross shape
        delta = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        for i, j in delta:
            self.set(x + i, y + j, color)

    # generate a Line from (x1, y1) to (x2, y2) with color
    # Only can generate a horizontal or vertical or diagonal line
    def draw_line(self, x1, y1, x2, y2, color):
        if not (x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1)):
            raise ValueError(
                "Bad x1 = {}, y1 = {}, x2 = {}, y2 = {}! \n Only can generate a horizontal or vertical or diagonal line".format(x1, x2, y1, y2))

        delta = [(1, 0), (1, 1), (0, 1), (-1, 1),
                 (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)]
        i = 0
        if (x2 > x1):
            if (y2 == y1):
                i = 0
            elif (y2 > y1):
                i = 1
            else:
                i = 7
        elif (x2 == x1):
            if (y2 == y1):
                i = 8
            elif (y2 > y1):
                i = 2
            else:
                i = 6
        else:
            if (y2 == y1):
                i = 4
            elif (y2 > y1):
                i = 3
            else:
                i = 5

        dx, dy = delta[i]

        for i in range(0, abs(x2 - x1) + 1):
            self.set(x1 + i * dx, y1 + i * dy, color)

    # connect two nodes at (x1, y1) and (x2, y2) using line with color
    # Only can generate a horizontal or vertical or diagonal line
    def connect_nodes(self, x1, y1, x2, y2, color):
        if (x1 == x2):
            if y2 < y1:
                self.draw_line(x1, y1 - 2, x2, y2 + 2, color)
            else:
                self.draw_line(x1, y1 + 2, x2, y2 - 2, color)
        elif (y1 == y2):
            if x2 < x1:
                self.draw_line(x1 - 2, y1, x2 + 2, y2, color)
            else:
                self.draw_line(x1 + 2, y1, x2 - 2, y2, color)
        elif (abs(x2 - x1) == abs(y2 - y1)):
            if x2 > x1:
                if y2 > y1:
                    self.draw_line(x1 + 1, y1 + 1, x2 - 1, y2 - 1, color)
                elif y2 < y1:
                    self.draw_line(x1 + 1, y1 - 1, x2 - 1, y2 + 1, color)
            elif x2 < x1:
                if y2 > y1:
                    self.draw_line(x1 - 1, y1 + 1, x2 + 1, y2 - 1, color)
                elif y2 < y1:
                    self.draw_line(x1 - 1, y1 - 1, x2 + 1, y2 + 1, color)
        else:
            raise ValueError(
                "Bad x1 = {}, y1 = {}, x2 = {}, y2 = {}! \n Only can generate a horizontal or vertical or diagonal line".format(x1, x2, y1, y2))
