import copy


class General(object):

    def __repr__(self):
        class_name = type(self)
        attrs = dir(self)
        print(f"Class {class_name}\nAttributes: {attrs}")

    def __cmp__(self, other):
        for original, another in zip(dir(self), dir(other)):
            if original != another:
                return False
        return True

    def __copy__(self):
        return copy.copy(self)

    def __deepcopy__(self, memodict={}):
        return copy.deepcopy(self)

    def __str__(self):
        return ', '.join(dir(self))

    def __instancecheck__(self, instance):
        return type(self) == type(instance)


class Any(General):
    pass
