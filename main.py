# "Битва героев"

class Hero():
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        print(f'{self.name} атакует')
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game():
    def __init__(self, player: Hero, computer: Hero):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            print(f'У {self.computer.name} осталось {self.computer.health} очков здоровья.')

            if not self.computer.is_alive():
                print(f' {self.computer.name} убит. {self.player.name} победил. Игра окончена.')
                break

            self.computer.attack(self.player)
            print(f'У {self.player.name} осталось {self.player.health} очков здоровья.')

            if not self.player.is_alive():
                print(f' {self.player.name} убит. {self.computer.name} победил. Игра окончена.')


player1 = Hero("Вупсень")
computer1 = Hero("Компьютер")

game = Game(player1, computer1)
game.start()
