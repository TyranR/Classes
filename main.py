from pprint import pprint

class Animals():
    type_animals = "Живое существо"
    name = "Без имени"
    weight = 0
    fill = 0
    state = "Отдыхает"
    sound = "......."

    def __init__(self, name, weight):
        """
        Определяем имя и вес
        """
        self.name = name
        self.weight = weight


    def feed(self, value=10):
        """
        Кормим животное
        """
        print(f"Вы даёте {self.type_animals} {self.name} еды в размере {value}%")
        fully_charged = self.fill + value
        if fully_charged > 100:
            print(f"{self.type_animals} {self.name} не может столько съесть")
        else:
            self.fill += value
            print(f"{self.type_animals} {self.name} сыто на {self.fill}%")

    def voice(self):
        """
        Животное издает звук
        """
        print(self.sound)

    def action_start(self):
        """
        Действие по умолчанию
        """
        state = "Контакт"

    def action_stop(self):
        """
        Действие по умолчанию
        """
        state = "Отдыхает"

class Goose(Animals):
    type_animals = "Гусь"
    sound = "Га-га-га"
    def action_start(self):
        self.state = "В процессе сбора яиц"
        print("Начинаем собирать яйца")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Собрали сколько смогли яиц")

class Cow(Animals):
    type_animals = "Корова"
    sound = "Му-у-у-у"
    def action_start(self):
        self.state = "В процессе дойки"
        print("Начинаем доить")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Закончили доить")

class Sheep(Animals):
    type_animals = "Овца"
    sound = "Бе-е-е-е"
    def action_start(self):
        self.state = "В процессе стрижки"
        print("Начинаем стричь")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Закончили стричь")

class Hen(Animals):
    type_animals = "Курица"
    sound = "Ко-ко-ко"
    def action_start(self):
        self.state = "В процессе сбора яиц"
        print("Начинаем собирать яйца")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Собрали сколько смогли яиц")

class Goat(Animals):
    type_animals = "Коза"
    sound = "Ме-е-е-е"
    def action_start(self):
        self.state = "В процессе дойки"
        print("Начинаем доить")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Закончили доить")

class Duck(Animals):
    type_animals = "Утка"
    sound = "Кря-кря"
    def action_start(self):
        self.state = "В процессе сбора яиц"
        print("Начинаем собирать яйца")
    def action_stop(self):
        self.state = "Отдыхает"
        print("Собрали сколько смогли яиц")

def choose_animal():
    """
    Выбор животное пользователем
    """
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

def which_animal_is_yours(choose):
    """
    Поиск животное в базе фермы
    """
    for animal in farm:
        if animal == choose:
            print(f"Вы выбрали - {animal.type_animals} {animal.name}")
            return animal

def which_animal_is_heaviest():
    """
    Подсчет самого тяжелого животного
    """
    name = ""
    weight = 0
    marker = 1
    for animal in farm:
        if animal.weight > weight:
            name = animal.name
            weight = animal.weight
        elif animal.weight == weight:
            marker = 0
        else:
            pass
    if marker:
        print(f"Самое тяжелое животное на ферме: {name}")
    else:
        print("Самое тяжелое животное нельзя определить, потому что их несколько")

def total_weight():
    """
    Подсчет общего веса всех животных
    """
    weight = 0
    for animal in farm:
        weight += animal.weight
    print(f"Общий вес всех животных на ферме: {weight}")

def what_should_u_do(animal):
    """
    Взаимодейтсвие с животными
    """
    print('Со всеми животными вы можете как-то взаимодействовать: \
    \nкормить (f)\
    \nкорову и коз доить (start/stop)\
    \nовец стричь (start/stop)\
    \nсобирать яйца у кур, утки и гусей (start/stop)\
    \nразличать по голосам (коровы мычат, утки крякают и т.д.) (v)')
    user_command = input("Выберите действие: ")
    if user_command == "f":
        animal.feed()
    elif user_command == "start":
        animal.action_start()
    elif user_command == "stop":
        animal.action_stop()
        print(animal.state)
    elif user_command == "v":
        animal.voice()
        print(f"{animal.type_animals} {animal.name} издает звук {animal.sound}")
    else:
        print("Этого сделать нельзя")

def main():
    """
    Основная функция программы
    """
    my_animal = which_animal_is_yours(choose_animal())
    what_should_u_do(my_animal)
    total_weight()
    which_animal_is_heaviest()

goose1 = Goose("Белый", 10)
goose2 = Goose("Серый", 15)
cow1 = Cow("Манька", 120)
sheep1 = Sheep("Барашек", 120)
sheep2 = Sheep("Кудрявый", 100)
hen1 = Hen("Ко-ко", 20)
hen2 = Hen("Кукареку", 20)
goat1 = Goat("Рога", 90)
goat2 = Goat("Копыта", 130)
duck1 = Duck("Кряква", 30)

farm = (goose1, goose2, cow1, sheep1, sheep2, hen1, hen2, goat1, goat2, duck1)

main()
