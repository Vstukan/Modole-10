# Создание класса

from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name=str, power=int):
        super().__init__()
        self.name = name
        self.power = power
        self.count_an = 100
        self.count_day = 0
    def run(self):
        print(f'{self.name}, На нас напали!')

        while self.count_an > 0:
                self.count_an -= self.power
                self.count_day += 1
                print(f'{self.name} сражается {self.count_day}..., осталось {self.power} воинов.')
                sleep(1)
        print(f'{self.name} одержал победу спустя {self.count_day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)


# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print(f'Все битвы закончились!')



