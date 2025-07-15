class Flowers:
    stem = True
    root = True
    leaves = True

    def __init__(self, title):
        self.title = title


class Rose(Flowers):
    thorns = True
    time_of_life = 5
    price = 20

    def __init__(self, title, color, length_of_stem):
        super().__init__(title)
        self.color = color
        self.length_of_stem = length_of_stem

    def __str__(self):
        result = (f"Цветок: {self.title}, цвет: {self.color}, длина стебля: {self.length_of_stem},"
                  f" время жизни: {self.time_of_life}дней, цена: {self.price}")
        return result


class Chamomile(Flowers):
    time_of_life = 2
    price = 10

    def __init__(self, title, color, length_of_stem):
        super().__init__(title)
        self.color = color
        self.length_of_stem = length_of_stem

    def __str__(self):
        result = (f"Цветок: {self.title}, цвет: {self.color}, длина стебля: {self.length_of_stem},"
                  f" время жизни: {self.time_of_life}дня, цена: {self.price}")
        return result


class Cornflower(Flowers):
    time_of_life = 3
    price = 5

    def __init__(self, title, color, length_of_stem):
        super().__init__(title)
        self.color = color
        self.length_of_stem = length_of_stem

    def __str__(self):
        result = (f"Цветок: {self.title}, цвет: {self.color}, длина стебля: {self.length_of_stem},"
                  f" время жизни: {self.time_of_life}дня, цена: {self.price}")
        return result


class Bunch:
    def __init__(self):
        self.flowers = []

    def __add__(self, flower):
        self.flowers.append(flower)
        return self

    def __str__(self):
        result = '; '.join(str(flower) for flower in self.flowers)
        return result

    def average_lifetime(self):
        total_days = sum(flower.time_of_life for flower in self.flowers)
        return round(total_days / len(self.flowers), 1)

    def bunch_price(self):
        total_price = sum(flower.price for flower in self.flowers)
        return total_price

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def find_by_lifetime(self):
        average = self.average_lifetime()
        result = [flower for flower in self.flowers if flower.time_of_life <= average]
        print("Цветы с временем жизни меньше или равным среднему:")
        for flower in result:
            print(flower)
        return result


flower_1 = Rose('Rose', 'red', 10)
print(flower_1)

flower_2 = Chamomile('Chamomile', 'white', 5)
print(flower_2)

flower_3 = Cornflower('Cornflower', 'blue', 3)
print(flower_3)

bunch_1 = Bunch() + flower_1 + flower_2 + flower_3
bunch_2 = Bunch() + flower_1 + flower_2
print("Букет номер 1:", bunch_1)
print(f"Время увядания букета номер 1: {bunch_1.average_lifetime()} дней")
print(f"Общая стоимость букета номер 1: {bunch_1.bunch_price()}")

print("Букет номер 2:", bunch_2)
print(f"Время увядания букета номер 2: {bunch_2.average_lifetime()} дней")
print(f"Общая стоимость букета номер 2: {bunch_2.bunch_price()}")


bunch_1.sort_by_color()
print("Букет 1 после сортировки по цвету:", bunch_1)
bunch_2.sort_by_color()
print("Букет 2 после сортировки по цвету:", bunch_2)

bunch_1.sort_by_price()
print("Букет 1 после сортировки по цене:", bunch_1)

bunch_2.sort_by_price()
print("Букет 2 после сортировки по цене:", bunch_2)

flowers_found = bunch_1.find_by_lifetime()
