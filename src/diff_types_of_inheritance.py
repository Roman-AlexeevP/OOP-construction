# Определяем общий класс стека - первый вошел, первый вышел
class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        raise NotImplementedError

    def pop(self, index):
        raise NotImplementedError

# Определяем класс-уточнение для стека - стек с ограниченным размером
class SizedStack(Stack):

    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def push(self, value):
        if len(self.data) == self.max_size:
            return BAD_STATUS
        super().push(value)

# Определяем класс расширение - двустороняя очередь, теперь можно доставать и последнее значение и добавлять в начало
class Deque(Stack):

    def push_front(self):
        raise NotImplementedError

    def pop_tail(self):
        raise NotImplementedError