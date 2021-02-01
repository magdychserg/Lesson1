#Если правильно понял задание. 2 атрибута класса и 2 переменных в методе расчета
class Road:
    def __init__(self, _length, _width):
        self._width = _width
        self._length = _length

    def weight(self, mass, thickness):
        self.mass = mass
        self.thickness =thickness
        return int(self._width * self._length * self.mass * self.thickness * 0.001)

weigh = Road(20, 5000)
print(f'weight of asphalt - {weigh.weight(25,5)} tonn')

