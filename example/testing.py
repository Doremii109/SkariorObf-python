# да, этот код я сгенерировал при помощи ИИ, мне лень было писать самому
# yes, I generated this code using AI, I was too lazy to write it myself.

# Определяем несколько функций для тестирования
class Test:
    def add(a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(a, b):
        """Возвращает разность двух чисел."""
        return a - b

    def multiply(a, b):
        """Возвращает произведение двух чисел."""
        return a * b

    def divide(a, b):
        """Возвращает частное двух чисел."""
        if b == 0:
            raise ValueError("Нельзя делить на ноль!")
        return a / b

    def is_even(n):
        """Проверяет, является ли число четным."""
        return n % 2 == 0

    # Тестируем функции с помощью assert

    def test_functions():
        # Тестируем функцию add
        assert Test.add(2, 3) == 5, "Ошибка в функции add"
        assert Test.add(-1, 1) == 0, "Ошибка в функции add"
        assert Test.add(0, 0) == 0, "Ошибка в функции add"

        # Тестируем функцию subtract
        assert Test.subtract(5, 3) == 2, "Ошибка в функции subtract"
        assert Test.subtract(10, 10) == 0, "Ошибка в функции subtract"
        assert Test.subtract(0, 0) == 0, "Ошибка в функции subtract"

        # Тестируем функцию multiply
        assert Test.multiply(3, 4) == 12, "Ошибка в функции multiply"
        assert Test.multiply(0, 5) == 0, "Ошибка в функции multiply"
        assert Test.multiply(-2, 3) == -6, "Ошибка в функции multiply"

        # Тестируем функцию divide
        assert Test.divide(10, 2) == 5, "Ошибка в функции divide"
        assert Test.divide(9, 3) == 3, "Ошибка в функции divide"
        try:
            Test.divide(1, 0)
            assert False, "Ошибка в функции divide: не было вызвано исключение при делении на ноль"
        except ValueError:
            pass

        # Тестируем функцию is_even
        assert Test.is_even(4) == True, "Ошибка в функции is_even"
        assert Test.is_even(5) == False, "Ошибка в функции is_even"
        assert Test.is_even(0) == True, "Ошибка в функции is_even"

        print('Все тесты пройдены успешно!')

author = "Doremi109 or @pyexec"
# Запускаем тестирование
Test.test_functions()

print(author)
