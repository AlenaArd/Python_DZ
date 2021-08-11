class Stationery:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'Start drawing with a {self.name}!')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


pen = Pen('pen')
pencil = Pencil('pencil')
marker = Handle('marker')


pen.draw()
pencil.draw()
marker.draw()
