from pprint import pprint

class Animals():
    type_animals = "Живое существо"
    name = "Без имени"
    fill = 0
    state = "Отдыхает"
    sound = "......."

    def __init__(self, name):
        self.name = name

    def feed(self, value=10):
        print(f"Вы даёте {self.type_animals} {self.name} еды в размере {value}%")
        fully_charged = self.fill + value
        if fully_charged > 100:
            print(f"{self.type_animals} {self.name} не может столько съесть")
        else:
            self.fill += value
            print(f"{self.type_animals} {self.name} сыто на {self.fill}%")

    def voice(self):
        print(self.sound)

    def action_start(self):
        state = "Контакт"

    def action_stop(self):
        state = "Отдыхает"

class Goose(Animals):
    type_animals = "Гусь"
    sound = "Га-га-га"
    def action_start(self):
        state = "Начинаем собирать яйца"
    def action_stop(self):
        state = "Собрали сколько смогли яиц"

class Cow(Animals):
    type_animals = "Корова"
    sound = "Му-у-у-у"
    def action_start(self):
        state = "Начинаем доить"
    def action_stop(self):
        state = "Закончили доить"

class Sheep(Animals):
    type_animals = "Овца"
    sound = "Бе-е-е-е"
    def action_start(self):
        state = "Начинаем стричь"
    def action_stop(self):
        state = "Закончили стричь"

class Hen(Animals):
    type_animals = "Курица"
    sound = "Ко-ко-ко"
    def action_start(self):
        state = "Начинаем собирать яйца"
    def action_stop(self):
        state = "Собрали сколько смогли яиц"

class Goat(Animals):
    type_animals = "Коза"
    sound = "Ме-е-е-е"
    def action_start(self):
        state = "Начинаем доить"
    def action_stop(self):
        state = "Закончили доить"

class Duck(Animals):
    type_animals = "Утка"
    sound = "Кря-кря"
    def action_start(self):
        state = "Начинаем собирать яйца"
    def action_stop(self):
        state = "Собрали сколько смогли яиц"

def choose_animal():
    print('\nВы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных: \
    \nгусей "Серый" (g1) и "Белый" (g2) \
    \nкорову "Маньку" (c1)\
    \nовец "Барашек" (s1) и "Кудрявый" (s2)\
    \nкур "Ко-Ко" (h1) и "Кукареку" (h2)\
    \nкоз "Рога" (g1) и "Копыта" (g2)\
    \nи утку "Кряква" (d1)')
    user_command = input("\nВыберите животного: ")
    if user_command == "g1":
        return goose1
    elif user_command == "g2":
        return goose2
    elif user_command == "c1":
        return cow1
    elif user_command == "s1":
        return sheep1
    elif user_command == "s2":
        return sheep2
    elif user_command == "h1":
        return hen1
    elif user_command == "h2":
        return hen2
    elif user_command == "g1":
        return hen1
    elif user_command == "g2":
        return hen2
    elif user_command == "d1":
        return duck1
    else:
        print("Извините, других животных тут нет")

def what_animals_are_yours(choose):
    for animal in farm:
        if animal == choose:
            print(f"Вы выбрали - {animal.type_animals} {animal.name}")
            return animal

def what_should_u_do(animal):
    print('Со всеми животными вы можете как-то взаимодействовать: \
    \nкормить (f)\
    \nкорову и коз доить (start/stop)\
    \nовец стричь (start/stop)\
    \nсобирать яйца у кур, утки и гусей (start/stop)\
    \nразличать по голосам (коровы мычат, утки крякают и т.д.) (v)')
    user_command = input("Выберите действие: ")
    if user_command == "f":
        pass
    elif user_command == "start":
        pass
    elif user_command == "stop":
        pass
    elif user_command == "v":
        pass
    else:
        print("Этого сделать нельзя")

def main():
    my_animal = what_animals_are_yours(choose_animal())
    what_should_u_do(my_animal)

goose1 = Goose("Белый")
goose2 = Goose("Серый")
cow1 = Cow("Манька")
sheep1 = Sheep("Барашек")
sheep2 = Sheep("Кудрявый")
hen1 = Hen("Ко-ко")
hen2 = Hen("Кукареку")
goat1 = Goat("Рога")
goat2 = Goat("Копыта")
duck1 = Duck("Кряква")

farm = (goose1, goose2, cow1, sheep1, sheep2, hen1, hen2, goat1, goat2, duck1)

main()
