class Void:
    pass

class Any(General):

    @classmethod
    def assignment_attempt(cls, target, source):
        if isinstance(target, cls) and isinstance(source, cls):
            target.value = source.value
            return target
        return Void