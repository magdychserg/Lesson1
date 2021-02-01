class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'start draw'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'pen start draw'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'pencil start draw'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'handle start draw'

pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle("handle")

print(pen.draw())
print(pencil.draw())
print(handle.draw())

