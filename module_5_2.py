class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название здания
        self.number_of_floors = number_of_floors  # Количество этажей

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Пример использования класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Выводим строковое представление объектов h1 и h2
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 20

# Получаем количество этажей с помощью len()
print(len(h1))  # Ожидаемый вывод: 10
print(len(h2))  # Ожидаемый вывод: 20