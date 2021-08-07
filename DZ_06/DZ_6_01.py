from time import sleep


class TrafficLight:
    colors = ('red', 'yellow', 'green')
    interval = (7, 2, 9)

    def __init__(self):
        self.__colors = 'green'

    def run(self):
        while True:
            for color in self.colors:
                self.__colors = color
                print(self.__colors)
                sleep(self.interval[self.colors.index(self.__colors)])


traffic_light = TrafficLight()
traffic_light.run()
