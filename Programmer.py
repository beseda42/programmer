def check_name(name):
    """
    Проверяет правильность введенного имени (насколько это возможно)

    :param name: строка-кандидат на имя
    :type name: str
    :return: name
    :rtype: str
    :raises TypeError: Не является строкой
    :raises ValueError: Некорректное имя
    """

    if not isinstance(name, str):
        raise TypeError("Не является строкой")
    if not (name != ''):
        raise ValueError("Некорректное имя")

    return name

def check_position(position):
    """
    Проверяет правильность введенной должности

    :param position: строка-кандидат на должность
    :type position: str
    :return: position
    :rtype: str
    :raises TypeError: Не является строкой
    :raises ValueError: Несуществующая должность
    """
    if not isinstance(position, str):
        raise TypeError("Не является строкой")

    positions = ['Junior', 'Middle', 'Senior']
    for elem in positions:
        if position.casefold() == elem.casefold():
            return elem

    raise ValueError("Несуществующая должность")

def set_pay_per_hour(position):
    """
    Определяет зарплату для должности

    :param position: должность
    :type position: str
    :return: размер зарплаты у должности
    :rtype: int
    :raises TypeError: Не является строкой
    :raises ValueError: Несуществующая должность
    """
    if not isinstance(position, str):
        raise TypeError("Не является строкой")

    positions_pay = {'Junior' : 10, 'Middle' : 15, 'Senior' : 20}
    for elem in positions_pay.keys():
        if position.casefold() == elem.casefold():
            return positions_pay.get(elem)

    raise ValueError("Несуществующая должность")

class Programmer:
    """
    Класс программиста в компании

    Атрибуты:
    name (str): имя
    position(str): должность (Junior, Middle, Senior)
    hours(int): количество отработанных часов
    wage(int): накопленная зарплата
    pay_per_hour(int): плата за час работы
    statistics(list of str): статистика с момента приема на работу

    """
    def __init__(self, name = '', position = ''):
        """
        Конструктор класса

        :param name: имя
        :type name: str
        :param position: должность (Junior, Middle, Senior)
        :type position: str
        """

        self.__name = check_name(name)
        self.__position = check_position(position)
        self.__hours = 0
        self.__wage = 0
        self.__pay_per_hour = set_pay_per_hour(position)
        self.__statistics = [f"{self.__name} {self.__position} устроился на работу"]


    def work(self, time):
        """
        Отмечает новую отработку в количестве часов
        и начисляет зарплату

        :param time: время работы
        :type time: int
        :return: None
        :rtype: None
        :raises TypeError: Не является int
        :raises ValueError: Отрицательное число
        """

        if not isinstance(time, int):
            raise TypeError("Не является int")
        if time < 0:
            raise ValueError("Отрицательное число")

        self.__statistics.append(f"{self.__name} {self.__position} отрабатывает {time} часов")
        self.__hours += time
        self.__wage += time * self.__pay_per_hour

    def bonus(self, amount):
        """
        Выдает бонус к зарплате

        :param amount: размер бонуса
        :type amount: int
        :return: None
        :rtype: None
        :raises TypeError: Не является int
        :raises ValueError: Отрицательное число
        """

        if not isinstance(amount, int):
            raise TypeError("Не является int")
        if amount < 0:
            raise ValueError("Отрицательное число")

        self.__statistics.append(f"{self.__name} {self.__position} получает бонус в размере {amount}")
        self.__wage += amount


    def rise(self):
        """
        Повышает должность программиста
        (и его заработную плату, соответственно)

        :return:None
        :rtype: None
        """

        self.__statistics.append(f"{self.__name} {self.__position} получает повышение")
        positions = ['Junior', 'Middle', 'Senior']
        for i in range (len(positions) - 1):
            if self.__position == positions[i]:
                self.__position = positions[i + 1]
                self.__pay_per_hour = set_pay_per_hour(self.__position)
                return
        self.__pay_per_hour += 1

    def info(self):
        """
        :return: строка в формате: <Имя> <Количество отработанных часов>ч. <Накопленная зарплата> тгр.
        :rtype: str
        """

        return f"{self.__name} {self.__hours} ч. {self.__wage} тгр."

    def salary(self):
        """
        Выдача зарплаты
        Возвращает сколько надо выдать зарплаты и обнуляет накопленную зарплату

        :return: сумма зарплаты
        :rtype: int
        """

        self.__statistics.append(f"{self.__name} {self.__position} получает зарплату в размере {self.__wage}")
        wage = self.__wage
        self.__wage = 0
        return wage

    def stat(self):
        """
        Выводит статистику и все шаги с момента приема на работу в формате <Имя> <Должность> <Событие с описанием>
        :return: None
        :rtype: None
        """

        print('\n'.join(map(str, self.__statistics)))