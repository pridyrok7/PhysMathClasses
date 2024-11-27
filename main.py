# 1.Создайте класс «Дробь». 10 минут
# 2. Необходимо хранить в полях класса: числитель и знаменатель. 15 минут
# 3.1 Реализовать метод класса для ввода данных. 7 минут
# 3.2 Реализовать метод класса для вывода данных. 7 минут
# 3.3 Реализовать доступ к отдельным полям через методы класса. 7 минут
# 4. Создайть метод класса для выполнения арифметических операций  15-20 минут
# 5. Создать  класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот.  15 минут
# 6. У класса должно быть два статических метода:
# 6. 1  Перевод из Цельсия в Фаренгейт 12 минут
# 6. 2 Перевод из Фаренгейта в Цельсий.  12 минут
# 7. Создать класс для перевода из метрической системы в английскую и наоборот: километры и мили, галоны и литры.   20  минут

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # числитель
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def set_numerator(self, value):
        self.numerator = value

    def set_denominator(self, value):
        self.denominator = value

    def display(self):
        print(f'{self.numerator} / {self.denominator}')

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        num2 = self.denominator * other.denominator
        return Fraction(num, num2)

    def __sub__(self, other):
        gen = self.numerator * other.denominator - other.numerator * self.denominator
        gen2 = self.denominator * other.denominator
        return Fraction(gen, gen2)

    def __mul__(self, other):
        pool = self.numerator * other.numerator
        pool2 = other.denominator * self.denominator
        return Fraction(pool, pool2)

    def __truediv__(self, other):
        cool = self.numerator * other.denominator
        cool2 = self.denominator * other.numerator
        return Fraction(cool, cool2)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (1.8 * celsius) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return 5 / 9 * (fahrenheit - 32)


class MetricToImperialConverter:
    @staticmethod
    def kilometer_to_miles(kilometer):
        return 0.621371 * kilometer

    @staticmethod
    def miles_to_kilometer(miles):
        return miles * 1.60934

    @staticmethod
    def gallons_to_liters(gallons):
        return gallons * 3.78541

    @staticmethod
    def litters_to_gallons(litters):
        return litters / 3.78541


if __name__ == '__main__':
    fr1 = Fraction(4, 8)
    fr2 = Fraction(1, 2)
    print(fr1 + fr2)
    print(fr1 - fr2)
    print(fr1 * fr2)
    print(fr1 / fr2)

    #Тестовые данные для перевода из Цельсия в Фаренгейт
    print(TemperatureConverter.celsius_to_fahrenheit(0))
    print(TemperatureConverter.celsius_to_fahrenheit(100))
    print(TemperatureConverter.celsius_to_fahrenheit(-40))

    print(TemperatureConverter.fahrenheit_to_celsius(32))
    print(TemperatureConverter.fahrenheit_to_celsius(212))
    print(TemperatureConverter.fahrenheit_to_celsius(-40))

    #Тестовые данный расстояние
    print(MetricToImperialConverter.kilometer_to_miles(0))
    print(MetricToImperialConverter.kilometer_to_miles(100))
    print(MetricToImperialConverter.kilometer_to_miles(42.195))

    print(MetricToImperialConverter.miles_to_kilometer(0))
    print(MetricToImperialConverter.miles_to_kilometer(50))
    print(MetricToImperialConverter.miles_to_kilometer(26.2195))

    #Тестовые данные Галлоны:
    print(MetricToImperialConverter.gallons_to_liters(0))
    print(MetricToImperialConverter.gallons_to_liters(10))
    print(MetricToImperialConverter.gallons_to_liters(5.5))

    print(MetricToImperialConverter.litters_to_gallons(0))
    print(MetricToImperialConverter.litters_to_gallons(50))
    print(MetricToImperialConverter.litters_to_gallons(20.8194))

