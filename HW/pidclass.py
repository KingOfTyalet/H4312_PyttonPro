import random


class SimpleEncoder:
    def __init__(self):
        self.__num = 0

    def __calculate(self, x):
        ops = ['+', '-', '*', '//']
        op = random.choice(ops)

        if op == '+': return self.__num + x
        if op == '-': return self.__num - x
        if op == '*': return self.__num * x
        if op == '//': return self.__num // x if x != 0 else self.__num

    def add_input(self):
        try:
            x = float(input("Введіть число: "))
            self.__num = self.__calculate(x)
            print(f"Виконано операцію з числом {x}")
        except ValueError:
            print("Помилка! Введіть число.")

    def __str__(self):
        return f"Поточний результат: {self.__num}"


# Використання
encoder = SimpleEncoder()

print("Простий шифратор - вводьте числа:")
for i in range(3):
    encoder.add_input()
    print(encoder)