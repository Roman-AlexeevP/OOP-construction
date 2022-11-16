# на уровне соглашения в python действует положение о приватных и защищенных методах/атрибутах, ключевым моментом
# является то, что это соглашение, а не обязательство и его можно обойти

# Соответствующие пункты:
# 1. метод публичен в родительском классе А и публичен в его потомке B;
# Классический пример, по умолчанию реализован в python

class ReportForExport:

    def export(self):
        pass

    def prepare_data(self):
        pass


class ReportForExcel(ReportForExport):
    pass

# По умолчанию доступны методы export() и prepare_data() на таком же уровне, что и в родителе

# пример 4. метод скрыт в родительском классе А и скрыт в его потомке B.

class ReportForExport:

    def export(self):
        pass

    def __prepare_data(self):
        pass


class ReportForExcel(ReportForExport):
    pass

# здесь при вывозве __prepare_data() что в родителе, что в потомке будет вызвана ошибка
