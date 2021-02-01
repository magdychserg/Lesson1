#Светофор, проверку не делал, просто не понял как тут можно сломать очередность(
from time import sleep

class TrafficLight:
    __color = ['Red', 'Yellow', 'Green']

    def running(self):
        for i in range(0, 3):
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
TrafficLight = TrafficLight()
TrafficLight.running()
