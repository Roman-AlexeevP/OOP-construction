class WeaponRarityTypes:

    COMMON = "COMMON"
    MAGIC = "MAGIC"
    RARE = "RARE"
    LEGENDARY = "LEGENDARY"

class Weapon:
    rarity_types = (
        'COMMON',
        'MAGIC',
        'RARE'
    )

    def __init__(self, weight, base_damage, rarirty):
        self.weight = weight
        self.base_damage = base_damage
        self.rarity = rarirty
        self.ability = None
        self.damage = 0

    def calculate_own_damage(self):
        self.damage = self.weight + self.base_damage * 0.5 * self.rarity
        return self.damage

    def is_rare_weapon(self):
        return self.rarity in (WeaponRarityTypes.RARE, WeaponRarityTypes.LEGENDARY)

    def get_special_ability(self):
        return self.ability if self.is_rare_weapon() else EmptyAbility()

class Sword(Weapon):
    # вот таким образом мы не можем переопределить метод, расширив предусловие уникальности оружия
    # так как все мечи будут уникальны и выдавать пустые способности, сломав код
    MAX_DAMAGE = 999
    def is_rare_weapon(self):
        return True

    #  при этом мы можем усилить постусловие создав проверку для расчета урона легендарных мечей, чтобы они были
    # балансными и не превышали необходимое число
    def is_damage_valid(self):
        return self.damage > self.MAX_DAMAGE

    def calculate_own_damage(self):
        super().calculate_own_damage()
        if not self.is_damage_valid():
            self.damage = self.MAX_DAMAGE
