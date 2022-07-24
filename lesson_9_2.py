

class Road:
    _length: int = 0
    _width: int = 0
    _thickness: int = 0

    def weight_Road(self, _length: int, _width: int, _thickness: int):
        weight = 25 
        self._length = _length
        self._width = _width
        self._thickness = _thickness
        result = (self._length*self._width*weight*self._thickness) / 1000
        return f'{self._length} m*{self._width} m*{weight} кг*{self._thickness} см = {int(result)} т'


road = Road()
print(road.weight_Road(20, 5000, 5))