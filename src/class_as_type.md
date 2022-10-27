Пример использования динамического связывания в Python

```python

# класс, определяющий интерфейс для класс-обработчика файлов, который может преобразовать содержимое в словарь(на самом деле можно и без него)
class Reader:

    def read(file):
        raise NotImplementedError
    def output_to_dict():
        raise NotImplentedError

# класс реализующий поведение для pdf файлов    
class PDFReader():

    def read(file):
        some_calculations()

    def output_to_dict():
        return some_dict()
# класс реализующий поведение для csv файлов        
class CSVReader():

    def read(file):
        some_calculations()

    def output_to_dict():
        return some_dict()
# фабрика для создания класса-обработчика на основании имени файла
def reader_factory(file):
    return some_reader_instance
# Вводим список файлов различных расширений, под которые у нас есть классы и с помощью динамического связывания пишем универсальный код преобразования в словарь файлов из списка
files = ["foo.pdf", "bar.csv"]
output_dicts = []
for file in files:
    reader = reader_factory(file)
    reader.read(file)
    output_dicts.append(reader.output_to_dict())
```
