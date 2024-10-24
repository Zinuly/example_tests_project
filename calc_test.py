# Определяем функцию test_sum
def test_sum():
    # Выполняем сложение чисел 2 и 2, результат присваиваем переменной sum
    sum = 2 + 2
    # Используем оператор assert для проверки правильности результата сложения
    # Если sum равно 4, тест проходит, иначе возникает AssertionError
    assert sum == 4


def test_integer_division():
    a = 5 // 2
    assert a == 2
test_integer_division()

