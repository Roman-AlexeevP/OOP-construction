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


class UpdateView:
    model_name = ""
    
    def update(self, fields):
        get_model(self.model_name).update(fields)
        
 # класс с льготным наследованием, где уточняется модель для обновления
 class UpdateUser(UpdateView):
    model_name = "user"
