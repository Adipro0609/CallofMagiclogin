class Spell:
    def __init__(self, name, cost, effect, cooldown, spell_type):
        self.name = name
        self.cost = cost      # Mana cost
        self.effect = effect  # Function or power value
        self.cooldown = cooldown
        self.type = spell_type
        self.timer = 0        # For cooldown tracking

class Player:
    def __init__(self, name, color, x, y, controls):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.x, self.y = x, y
        self.color = color
        self.spells = [...]   # List of Spell objects
        self.active_spell = 0
        self.controls = controls  # Dict of keys for movement and action
