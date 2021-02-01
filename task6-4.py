class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' you {self.name} go'

    def stop(self):
        return f'you {self.name} stop'

    def turn(self, turning):
        if turning == 'left':
            return f'{self.name} you car turn on left'
        elif turning == 'right':
            return f'{self.name} you car turn on right'

    def show_speed(self):
        return f'{self.name} you speed {self.speed} km/h'

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} your speed is high'
        else:
            return f'{self.name} you speed {self.speed} km/h'

class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} your speed is high'
        else:
            return f'{self.name} you speed {self.speed} km/h'

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



bmw = SportCar(250, 'red', 'bmw', False)
nissan = TownCar(75, 'green', 'nissan', True)
gaz = WorkCar(38, 'blue', 'gaz', False)
lada = PoliceCar(120, 'white', 'lada', True)
print(bmw.go())
print(f"{gaz.turn('left')} {gaz.show_speed()}")
print(f'{nissan.name} color you car is {nissan.color}')
print(lada.turn('right'))
print(f'{bmw.show_speed()}. {nissan.show_speed()}')

