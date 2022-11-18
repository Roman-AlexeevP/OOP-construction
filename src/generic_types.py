class General(object):
    pass

class Any(General):
    pass

class Void:
    pass

# python позволяет нам делать подобные вещи без типа-параметра, необходимо только проверять наличие методов сложения
# для данных типов, если они не поддерживаются, то возвращаем Void
class Vector(Any):

    def __init__(self, items=None):
        self.items = items or []

    def __add__(self, other):
        if not isinstance(other, Vector) or len(other) != len(self):
            return Void

        try:
            new_items = [self_item + other_item for self_item, other_item in zip(self.items, other.items)]
        except TypeError:
            return Void

        return Vector(new_items)

    def __len__(self):
        return len(self.items)
