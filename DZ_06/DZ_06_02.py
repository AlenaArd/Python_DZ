class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_of(self, norm, height):
        return self.__length * self.__width * norm * height / 1000


road_r = Road(5000, 20)
print(road_r.mass_of(25, 5))
