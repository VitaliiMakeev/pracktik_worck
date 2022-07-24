import time


# class TrafficLight:
#     __color: list = ['красный', 'желтый', 'зеленый']
#     def runing(self):
#         while True:
#             try:
#                 print(f'{self.__color[0]}')
#                 time.sleep(7)
#                 print(f'{self.__color[1]}')
#                 time.sleep(2)
#                 print(f'{self.__color[2]}')
#                 time.sleep(2)
#             except KeyboardInterrupt:
#                 print('Пользователь остановил программу')
#                 break

class TrafficLight:
    __color: list = ['красный', 'желтый', 'зеленый']

    def runing(self, count: int):
        self.count = count
        i = 0
        while i < self.count:
            try:
                print(f'{self.__color[0]}')
                time.sleep(7)
                print(f'{self.__color[1]}')
                time.sleep(2)
                print(f'{self.__color[2]}')
                time.sleep(2)
                i += 1
            except KeyboardInterrupt:
                print('Пользователь остановил программу')
                break






trfli = TrafficLight()
trfli.runing(2)