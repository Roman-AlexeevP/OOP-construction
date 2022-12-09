Класс локация содержит класс внутренней активности, который представлен базовым класс Подземелье
с потомками пещера, катакомбы.
При этом она обладает классом тип поверхности: лава, болото, например, что позволяет избегать длинных цепочек как
ЛокацияВоднаяСКатакомбами и гибко генерировать итоговый класс локации через собственные сеттеры.

```python
class Dungeon:
    pass

class Catacomb(Dungeon):
    pass

class Cave(Dungeon):
    pass

class Surface:
    pass

class Lava(Surface):
    pass

class Location:

    encounter: Dungeon
    terrain_type: Surface

lava_location_with_catacomb = Location()
lava_location_with_catacomb.set_surface(Lava())
lava_location_with_catacomb.set_encounter(Catacomb())
```