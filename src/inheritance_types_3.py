#  как АТД
class Stack:
    pass

# как наследование с детализацией
class SizedStack(Stack):
    pass

class Validator:
    pass
# абстрактные методы проверки
    def validate(self):
        pass

# как наследование с детализацией
class IntegerValidator(Validator):

    def validate(self, input):
        return isinstance(int, input)

