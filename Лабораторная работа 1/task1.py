# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Recipe:
    def __init__(self, name: str, number_of_servings: int, product_list: dict):
        """
        Создание и подготовка к работе объекта "Рецепт"
        
        :param name: Название блюда
        :param number_of_servings : Количество порций
        :param product_list: Список продуктов 
                             В качестве ключей задано название продукта, а в качестве значения - необходимое количество
                             этого продукта
        
        Примеры:
        >>> salat = Recipe("Овощной салат", 2, {"Помидор": 1, "Огурец": 1})
        """
        if not isinstance(name, str):
            raise TypeError("Необходимо ввести строку")
        self.name = name

        if not isinstance(number_of_servings, int):
            raise TypeError("Количество порций должно быть целым числом")
        if number_of_servings <= 0:
            raise ValueError("Количество блюд должно быть положительным числом")
        self.number_of_servings = number_of_servings

        for product_name, product_count in product_list.items():
            if not isinstance(product_name, str):
                raise TypeError("Название продуктов необходимо указать строкой")
            if not isinstance(product_count, (int, float)):
                raise TypeError("Количество продуктов необходимо указать целым или дробным числом")
            if product_count <= 0:
                raise ValueError("Количество продуктов должно быть положительным")
        self.product_list = product_list

    def increase_product_amount(self, amount) -> None:
        """
        Функция, подсчитывающая необходимое количество продуктов при увеличении числа порций блюда

        :param amount: Число дополнительных порций блюда

        Примеры:
        >>> salat = Recipe("Овощной салат", 2, {"Помидор": 1, "Огурец": 1})
        >>> salat.increase_product_amount(2)
        """
        if not isinstance(amount, int):
            raise TypeError("Число дополнительных порций необходимо указать целым числом")
        if amount <= 0:
            raise ValueError("Число дополнительных порций должно быть положительным")
        ...

    def export_list(self, file_name: str) -> None:
        """
        Функция, экспортирующая список продуктов в отдельный текстовый файл

        :param file_name: Название файла

        Примеры:
        >>> salat = Recipe("Овощной салат", 2, {"Помидор": 1, "Огурец": 1})
        >>> salat.export_list("spisok productov.txt")
        """
        if not isinstance(file_name, str):
            raise TypeError("Имя файла необходимо указать строкой")
        ...


class Window:
    def __init__(self, width: int, height: int, mark: str):
        """
        Создание и подготовка к работе объекта "Окно"

        :param width: Ширина окна в мм
        :param height : Высота окна в мм
        :param mark: Марка окна

        :raise ValueError: С целью унификации размеров строительных элементов размеры окна кратны 10 мм

        Примеры:
        >>> window_1 = Window(1470, 1320, "ОК1")
        """
        if not isinstance(width, int):
            raise TypeError("Ширина окна должна быть целым числом")
        if not (width % 10 == 0):
            raise ValueError("Ширина окна должна быть кратна 10 мм")
        if width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("Высота окна должна быть целым числом")
        if not height % 10 == 0:
            raise ValueError("Высота окна должна быть кратна 10 мм")
        if height <= 0:
            raise ValueError("Высота окна должна быть положительным числом")
        self.height = height

        if not isinstance(mark, str):
            raise TypeError("Необходимо ввести строку")
        self.mark = mark

    def square(self) -> float:
        """
        Функция, подсчитывающая площадь окна в кв.м.

        :return: Площадь окна в кв.м.

        Примеры:
        >>> window_1 = Window(1470, 1320, "ОК1")
        >>> window_1.square()
        """
        ...

    def m2(self) -> float:
        """
        Функция, переводящая высоту и ширину окна из мм в кв.м

        :return: Высота и ширина окна в кв.м.

        Примеры:
        >>> window_1 = Window(1470, 1320, "ОК1")
        >>> window_1.m2()
        """
        ...


class GameCharacter:
    def __init__(self, strength: int, dexterity: int, intelligence: int):
        """
        Создание и подготовка к работе объекта "Игровой персонаж"

        :param strength : Значение параметра силы
        :param dexterity : Значение параметра ловкости
        :param intelligence: Значение параметра интеллекта

        :raise ValueError: В каждый параметр можно вложить одно, два или три очка, либо не вкладывать вовсе
        :raise ValueError: Всего необходимо распределить три очка

        Примеры:
        >>> Steve = GameCharacter(2, 1, 0)
        """
        if strength not in [0, 1, 2, 3]:
            raise ValueError("Параметр силы задается целым числом от 0 до 3")
        if dexterity not in [0, 1, 2, 3]:
            raise ValueError("Параметр ловкости задается целым числом от 0 до 3")
        if intelligence not in [0, 1, 2, 3]:
            raise ValueError("Параметр интеллекта задается целым числом от 0 до 3")
        if strength + dexterity + intelligence != 3:
            raise ValueError("Суммарное число очков должно быть равно 3")
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

    def fight(self) -> str:
        """
        Функция, позволяющая сыграть простейший бой с противником.
        С помощью модуля random генерируется случайное значение из диапазона от 0 до 3 для одного из параметров.
        Если значение данного параметра у персонажа больше, то он побеждает.

        :return: В случае победы строка "Победа!"
                 В случае поражения строка "Поражение..."

        Примеры:
        >>> Steve = GameCharacter(2, 1, 0)
        >>> Steve.fight()
        """
        ...

    def increase_parameter(self, parameter: str) -> None:
        """
        Функция, увеличивающая значение выбранного параметра персонажа на 1 очко

        :param: parameter: выбираемый параметр (сила, ловкость или скорость)

        Примеры:
        >>> Steve = GameCharacter(2, 1, 0)
        >>> Steve.increase_parameter("strength")
        """

        if parameter not in ["strength", "dexterity", "intelligence"]:
            raise NameError("Название параметра введено неверно")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
