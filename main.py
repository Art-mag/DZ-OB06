# Определение класса Hero, который будет использоваться для создания героев в игре
class Hero:
    # Конструктор класса, который инициализирует нового героя с именем, здоровьем и силой удара
    def __init__(self, name, health=100, attack_power=20):
        self.name = name  # Имя героя
        self.health = health  # Здоровье героя, по умолчанию 100
        self.attack_power = attack_power  # Сила удара героя, по умолчанию 20

    # Метод для атаки другого героя, который уменьшает здоровье противника на величину силы удара
    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    # Метод для проверки, жив ли герой (здоровье больше 0)
    def is_alive(self):
        return self.health > 0

# Определение класса Game, который управляет игровым процессом
class Game:
    # Конструктор класса, который инициализирует игру с двумя героями: игроком и компьютером
    def __init__(self, player, computer):
        self.player = player  # Герой-игрок
        self.computer = computer  # Герой-компьютер

    # Метод для начала игры, который чередует ходы игрока и компьютера до тех пор, пока один из героев не умрет
    def start(self):
        turn = 0  # Счетчик ходов
        # Цикл продолжается, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            # Если номер хода четный, атакует игрок, иначе - компьютер
            if turn % 2 == 0:
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)
            turn += 1  # Увеличение счетчика ходов
            # Вывод текущего состояния здоровья игрока и компьютера
            print(f"Здоровье игрока: {self.player.health}, Здоровье компьютера: {self.computer.health}")

        # Определение победителя игры
        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена. Победитель: {winner.name}")

# Создание экземпляров героев
player_hero = Hero("Игрок")  # Герой-игрок
computer_hero = Hero("Компьютер")  # Герой-компьютер

# Создание экземпляра игры и начало игрового процесса
game = Game(player_hero, computer_hero)
game.start()  # Запуск игры
