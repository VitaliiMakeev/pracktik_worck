

class Car:
    speed: int = 0
    color: str = 'черная'
    name: str = 'Chevrolet'
    is_police: bool = False

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула {direction}'

    def show_speed(self, avto):
        self.avto = avto
        return f'Текущая скорость автобобиля: {avto}'


class TownCar(Car):
    speed = 60
    color = 'Белая'
    name = 'Lada'
    is_police = False

    def show_speed(self, avto: speed):
        self.speed = avto
        if TownCar.speed > 60:
            return f'Превышение скорости на {avto - 60}'
        else:
            return f'Текущая скорость автомобиля {avto}'


class SportCar(Car):
    speed = 120
    color = 'Красная'
    name = 'Ferrari'
    is_police = False


class WorkCar(Car):
    speed = 40
    color = 'Желтая'
    name = 'Gazel'
    is_police = False

    def show_speed(self, avto: speed):
        self.speed = avto
        if WorkCar.speed > 40:
            return f'Превышение скорости на {avto - 40}'
        else:
            return f'Текущая скорость автомобиля {avto}'


class PoliceCar(Car):
    speed = 80
    color = 'Синяя'
    name = 'Lada Vesta'
    is_police = True


car_1 = Car()
car_2 = TownCar()
print(car_1.show_speed(PoliceCar.speed))
TownCar.speed = 110
print(PoliceCar().color)
print(SportCar().name)
print(car_2.show_speed(TownCar.speed))
print(SportCar().name, Car().turn('направо'))