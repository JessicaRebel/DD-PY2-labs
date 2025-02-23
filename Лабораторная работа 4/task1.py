import math
import doctest
if __name__ == "__main__":
    class Slab:
        """
        Класс "Плита перекрытия"
        attr: material: Материал плиты
        """
        material = "reinforced concrete"

        def __init__(self, length: int, width: int, height: int):
            """
            Создание и подготовка к работе объекта "Плита"
            :param length: Длина плиты в мм
            :param width: Ширина плиты в мм
            :param height: Высота плиты в мм

            Примеры:
            >>> slab = Slab(1500, 2400, 200)
            """
            self.length = length
            self.width = width
            self.height = height

        @property
        def length(self) -> int:
            return self._length

        @length.setter
        def length(self, length: int) -> None:
            if not isinstance(length, int):
                raise TypeError("Длина плиты должна быть задана целым числом")
            if length <= 0:
                raise ValueError("Длина плиты должна быть задана положительным числом")
            if length % 100 != 0:
                raise ValueError("Длина плиты должна быть кратна 100")
            self._length = length

        @property
        def height(self) -> int:
            return self._height

        @height.setter
        def height(self, height: int) -> None:
            if not isinstance(height, int):
                raise TypeError("Высота плиты должна быть задана целым числом")
            if height <= 0:
                raise ValueError("Высота плиты должна быть задана положительным числом")
            if height % 10 != 0:
                raise ValueError("Высота плиты должна быть кратна 10")
            self._height = height

        @property
        def width(self) -> int:
            return self._width

        @width.setter
        def width(self, width: int) -> None:
            if not isinstance(width, int):
                raise TypeError("Ширина плиты должна быть задана целым числом")
            if width <= 0:
                raise ValueError("Ширина плиты должна быть задана положительным числом")
            if width % 100 != 0:
                raise ValueError("Ширина плиты должна быть кратна 100")
            self._width = width

        def volume(self) -> float:
            """
            Определение объема материала плиты

            :return: Объем плиты в куб.м. с точностью до тысячных

            Примеры:
            >>> s = Slab(1500, 2400, 200)
            >>> s.volume()
            0.72
            """
            volume = self.length * self.width * self.height / 10 ** 9
            return round(volume, 3)

        def cut_opening(self, a: int, b: int, x: int, y: int) -> float:
            """
            Вырезает прямоугольное отверстие в плите(например, под вентиляционный канал)

            :param a: Длина отверстия
            :param b: Ширина отверстия
            :param x: Расстояние по горизонтали от левой границы плиты до левой границы отверстия
            :param y: Расстояние по вертикали от нижней границы плиты до нижней границы отверстия

            :return: Объем материала плиты в куб. м с точностью до тысячных после вырезания отверстия

            Примеры:
            >>> s = Slab(1500, 2400, 200)
            >>> s.cut_opening(200, 100, 1000, 500)
            0.716
            """
            if not isinstance(a, int):
                raise TypeError("Длина отверстия должна быть задана целым числом")
            if not isinstance(b, int):
                raise TypeError("Ширина отверстия должна быть задана целым числом")
            if not isinstance(x, int):
                raise TypeError("Расстояние x должно быть задано целым числом")
            if not isinstance(y, int):
                raise TypeError("Расстояние y должно быть задано целым числом")
            if (a <= 0) or (b <= 0):
                raise ValueError("Размеры отверстия должны быть заданы положительным числом")
            if (x < 0) or (y < 0):
                raise ValueError("Расстояния не должны быть отрицательными")
            if (x >= self.length) or (y >= self.width):
                raise ValueError("Отверстие полностью находится за границами плиты")
            if ((x == 0) and (a >= self.length)) or ((y == 0) and (b >= self.width)):
                raise ValueError("Исходный объект разделен на несколько частей")
            z_x = self.length - (x + a)
            z_y = self.width - (y + b)
            if z_x > 0:
                z_x = 0  # Если отверстие не выходит за границу плиты обнуляем "свешивающуюся" часть
            if z_y > 0:
                z_y = 0
            new_volume = self.volume() - (self.height * (a + z_x) * (b + z_y)) / 10 ** 9
            return round(new_volume, 3)

        def __str__(self) -> str:
            return f"Плита перекрытия железобетонная сплошная {self.length}x{self.width}x{self.height} мм"

        def __repr__(self) -> str:
            return f"Slab(length={self.length}, width={self.width}, height={self.height})"


    class HollowCoreSlab(Slab):
        """
        Класс "Многопустотная плита перекрытия"
        (Пример, как она выглядит https://st26.stpulscen.ru/images/product/231/987/570_original.jpg)
        Наследуется от класса "Плита перекрытия"
        """
        def __init__(self, length: int, width: int, height: int, diameter: int):
            """
            Создание и подготовка к работе объекта "Многопустотная плита"

            :param length: Длина плиты в мм
            :param width: Ширина плиты в мм
            :param height: Высота плиты в мм
            :param diameter: Диаметр пустот в плите в мм

            Примеры:
            >>> s1 = HollowCoreSlab(1500, 2400, 200, 100)
            """
            super().__init__(length, width, height)
            self._diameter = diameter

        @property
        def diameter(self) -> int:
            return self._diameter

        @diameter.setter
        def diameter(self, diameter) -> None:
            if not isinstance(diameter, int):
                raise TypeError("Диаметр пустот должен быть задан целым числом")
            if diameter <= 0:
                raise ValueError("Диаметр пустот должен быть задан положительным числом")
            if diameter % 10 != 0:
                raise ValueError("Диаметр пустот должен быть кратен 10")
            if diameter > self.height - 50:
                raise ValueError("Слишком большой диаметр")
            self._diameter = diameter

        def number(self) -> int:
            """
            Определяет максимальное число пустот в плите исходя из условий:
            - минимальное расстояние между краями пустот - 25 мм
            - все расстояния одинаковы и кратны 5

            :return: Число пустот в плите

            Примеры:
            >>> s1 = HollowCoreSlab(1500, 2400, 200, 100)
            >>> s1.number()
            19
            """
            a = 25  # Задаем минимальное расстояние между краями пустот
            while True:
                w = self.width
                n = 0
                while w > a:
                    w = w - (a + self.diameter)
                    n += 1
                if w == a:
                    break
                a += 5  # Расстояния между краями пустот кратны 5
            return n

        def volume(self, n=None):
            """
            Определяет объем материала плиты в куб. м с точностью до сотых

            :param n: При желании, пользователь может сам задать необходимое число пустот
                      Если не задано, значение n определяется методом number

            :return: Объем материала плиты в куб. м с точностью до тысячных
            Примеры:
            >>> s1 = HollowCoreSlab(1500, 2400, 200, 100)
            >>> s1.volume(10)
            0.602
            """
            if n is None:
                n = self.number()
            if not isinstance(n, int):
                raise TypeError("Количество пустот должно быть задано целым числом")
            if n <= 0:
                raise ValueError("Количество пустот должно быть задано положительным числом")
            if n * self.diameter >= self.width:
                raise ValueError("Количество пустот лишком большое")
            volume = super().volume() - (n * self.diameter ** 2 / 4 * math.pi * self.length) / 10 ** 9
            return round(volume, 3)

        def __str__(self) -> str:
            return (f"Плита перекрытия железобетонная многопустотная "
                    f"{self.length}x{self.width}x{self.height} мм, d={self.diameter} мм")

        def __repr__(self) -> str:
            return (f"HollowCoreSlab"
                    f"(length={self.length}, width={self.width}, height={self.height}, diameter={self.diameter})")

    doctest.testmod()  # тестирование примеров, которые находятся в документации

