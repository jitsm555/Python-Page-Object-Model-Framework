import math


class ImageElement:

    def __init__(self, driver, x, y, width, height):
        self.driver = driver
        self.center_x = math.floor(x + width / 2)
        self.center_y = math.floor(y + height / 2)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def click(self):
        """
        Clicks in the middle of an image bounds
        """
        return self.driver.tap([(self.center_x, self.center_y)])

    @property
    def size(self):
        return {'width': self.width, 'height': self.height}

    @property
    def location(self):
        return {'x': self.x, 'y': self.y}

    @property
    def rect(self):
        return {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def is_displayed(self):
        return True
