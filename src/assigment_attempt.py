class Void:
    pass

class General(object):
    def assigment_attempt(self, target):
        if issubclass(target, self):
            return target
        return Void()

class Any(General):
    pass