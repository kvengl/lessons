class Rectangle:
    def __init__(self, width, height, L, battalion):
        self.width = width
        self.height = height
        self.L = L
        self.battalion = battalion
        self.squares = Squares(width, height)
        self.is_captured = False
        self.count_captured = 0

    def capture(self):
        new_L = 0
        new_battalion = []
        for i in range(0, self.L * 2, 2):
            x = self.battalion[i]
            y = self.battalion[i + 1]
            if self.squares.is_need_to_capture(x, y):
                self.squares.squares[x][y].capture()
                self.count_captured += 1
                if self.squares.is_need_to_capture(x + 1, y):
                    new_L += 1
                    new_battalion.append(x + 1)
                    new_battalion.append(y)
                if self.squares.is_need_to_capture(x - 1, y):
                    new_L += 1
                    new_battalion.append(x - 1)
                    new_battalion.append(y)
                if self.squares.is_need_to_capture(x, y + 1):
                    new_L += 1
                    new_battalion.append(x)
                    new_battalion.append(y + 1)
                if self.squares.is_need_to_capture(x, y - 1):
                    new_L += 1
                    new_battalion.append(x)
                    new_battalion.append(y - 1)
        self.L = new_L
        self.battalion = new_battalion
        self.update_is_captured()

    def update_is_captured(self):
        if self.count_captured == self.width * self.height:
            self.is_captured = True


class Squares:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.squares = []
        for i in range(width):
            self.squares.append([])
            for j in range(height):
                square = Square(i, j)
                self.squares[i].append(square)

    def is_need_to_capture(self, x, y):
        if self.is_valid_coord(x, y) and not self.squares[x][y].is_captured:
            return True
        return False

    def is_valid_coord(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        return False


class Square:
    def __init__(self, x, y, is_captured=False):
        self.x = x
        self.y = y
        self.is_captured = is_captured

    def capture(self):
        self.is_captured = True


def ConquestCampaign(N, M, L, battalion):
    battalion = normalize_battalion(battalion)
    rectangle = Rectangle(N, M, L, battalion)
    days = 0
    while not rectangle.is_captured:
        rectangle.capture()
        days += 1
    return days


def normalize_battalion(battalion):
    new_battalion = []
    for el in battalion:
        new_battalion.append(el - 1)
    return new_battalion
