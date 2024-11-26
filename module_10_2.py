import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            self.enemies -= self.power
            days += 1
            print(f'{self.name} сражается {days} дней, осталось {self.enemies} врагов')
            time.sleep(1)
        if self.enemies == 0:
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения