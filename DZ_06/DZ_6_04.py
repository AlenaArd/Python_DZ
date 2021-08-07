class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_polise = is_police

    def go(self):
        print(f'{self.name} Go')

    def stop(self):
        print(f'{self.name} Stop')

    def turn(self, direction):
        print(f'{self.name} Car go to {direction}')

    def show_speed(self):
        print(f'{self.name} Current speed is {self.speed}')


class TounCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'{self.name} Speed limit violated!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'{self.name} Speed limit violated!')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, True)


t = TounCar('Mazda', 'red', 70,)
s = SportCar('Jaguar', 'black', 150)
w = WorkCar('Belaz', 'orange', 50)
p = PoliceCar('police', 'blue', 120)


t.turn('left')
t.show_speed()
t.speed = 55
t.show_speed()
s.show_speed()
w.show_speed()
w.turn('rigth')
p.go()
