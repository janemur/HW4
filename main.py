import json


class AdvertBase(object):
    """ Класс позволяет обращаться к полям через точку"""
    def __init__(self, data):

        for key, val in data.items():

            # Обрабатываем значения меньше нуля
            if key == 'price' and val < 0:
                print('ValueError: must be >= 0')
                quit()
            # создаем словарь со значениями json
            setattr(self, key, self.compute_attr_value(val))

    def compute_attr_value(self, value):
        """ Для каждого ключа обозначение его значение"""
        if type(value) is list:
            return [self.compute_attr_value(x) for x in value]
        elif type(value) is dict:
            return AdvertBase(value)
        else:
            return value

    def __repr__(self):
        return f'{AdvertBase(j).title} | {AdvertBase(j).price} ₽'


class ColorizeMixin:
    """ Класс Миксин окрашивает в заданный цвет вывод"""

    @staticmethod
    def add_some_colors(s, repr_color_code=33):
        return f'\033[{repr_color_code}m{s}\033[0m'


class Advert(AdvertBase, ColorizeMixin):
    """ Класс объединяет значения основного класса AdvertBase и класса миксина ColorizeMixin"""
    pass


if __name__ == '__main__':
    phone = """
    {
    "title": "iPhone X",
    "price": 45,
    "location": {
    "address": "город Самара, улица Мориса Тореза, 50",
    "metro_stations": ["Спортивная", "Гагаринская"]
    }
    }"""

    corgi = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    without_price = """{"title": "python"}"""

    j = json.loads(phone)
    iphone_ad = Advert(j)

    # вывод в консоль значений
    k = AdvertBase(j).__repr__()
    print(iphone_ad.add_some_colors(k))

    # обращаемся к атрибуту location.address, вывод адреса
    print(iphone_ad.location.address)
