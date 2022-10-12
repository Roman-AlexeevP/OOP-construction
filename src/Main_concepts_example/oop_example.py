# Наследование

# Определим общий класс валидатора некого абстрактного значения
from typing import List


class Validator:

    # конструктор: принимается любое абстрактное значение для проверки
    def __init__(self, raw_data):
        self.raw_data = raw_data

    # внутренняя функция для реализации в наследниках собственно логики проверким
    def _validate(self) -> bool:
        raise NotImplementedError

    # функция для определения сообщения об ошибке
    def get_error_message(self):
        raise NotImplementedError

    # верификация результата с возвращением проверенных данных или же выбрасывания исключения
    def __call__(self, *args, **kwargs) -> bool:
        return self._validate()


# Реализуем конкретного наследника - валидатор целых положительных чисел,
# он по сути является валидатором и реализует его логику исходя из собственной спецификации
class PositiveIntegerValidator(Validator):

    def _validate(self) -> bool:
        return self.raw_data >= 0 and isinstance(self.raw_data, int)

    def get_error_message(self):
        return "Данные представлены не в виде целого числа или меньше 0"

# Композиция
# В данном случае имеется абстрактный класс поля данных, у которого в силу своих ограничений
# могут быть собственные валидаторы, которые содержатся в этом классе как список
class Field:

    def __init__(self, value, name, validators: List[Validator]):
        self.value = value
        self.name = name
        self.validators = [validator(value) for validator in validators]
        self.errors = []

    # в данном случае и используется полиморфизм так как нам все равно какой конкретно валидатор предоставлен
    # а также какая у него логика, главное, чтобы он был потомком Validator и реализовывал метод _validate()
    def is_valid(self) -> bool:
        for validator in self.validators:
            if not validator():
                self.errors += validator.get_error_message()
        return len(self.errors) < 1

