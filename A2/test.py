# class Foo:
#     def bar(self) -> str:
#         self.name = f'{self.__name__}'
#         return self.name

# class SubFoo(Foo):
#     pass

# s  = SubFoo()
# s.__class__.__name__
from a2 import * 

class test:
    def __init__(self, hp: int) -> None:
        self.hp = hp
        self.block = 0
    
    def get_block(self):
        return self.block

    def action(self, num: int) -> dict[str, int]:
            self.d = {}
            hp_dif = num
            if hp_dif % 2 == 0:
                damage = int(hp_dif / 2)
                self.block = damage
                self.d['damage'] = damage
                return self.d
            else:
                damage = int((hp_dif / 2) - 0.5)
                self.block = int((hp_dif / 2) + 0.5)
                self.d['damage'] = damage
                return self.d
           
ic = IronClad()
e1 = Encounter(ic, [('Louse',10),('Louse',10),('Louse',10)])
ic.get_hand()
e1.start_new_turn()
ic.get_hand()
ic.get_deck()
e1.player_apply_card('Strike') # should return false
e1.is_active()

d = {}
d['block'] = 5
d['strength']

card = Card()
str(card) == 'Card: A card.'
str(card)

# Check that the number did not change for same instance
louse = Louse(10)
louse.get_id()
louse.action()
al = Louse(10)
al.get_id()
al.action()

random.seed(10012023)
louse = Louse(10)
louse2 = Louse(10)
louse3 = Louse(10)
louse4 = Louse(10)
louse5 = Louse(10)
louse.action()
louse2.action()
louse3.action()
louse4.action()
louse5.action()

random.seed("louse")
louse = Louse(10)
louse2 = Louse(10)
louse3 = Louse(10)
louse4 = Louse(10)
louse5 = Louse(10)
louse.action()
louse2.action()
louse3.action()
louse4.action()
louse5.action()

random.seed(10012023)
random_louse_amount()

random.seed("louse")
random_louse_amount()

ic = IronClad()
repr(ic)

cards = [Bash(), Strike(), Defend()]
p = Player(10, cards, [1,2,3,4])
repr(p)

player = Silent()
monsters = [('Louse', 10), ('Cultist', 10)]
encounter = Encounter(player, monsters)
encounter.player_apply_card('Neutralize', 0)


player = Silent()
monsters = [('Louse', 10)]
encounter = Encounter(player, monsters)
# Specify a seed for testing
random.seed("player_apply_card")
# Ensure cards are reset
encounter.end_player_turn()
encounter.start_new_turn()
# Check card not in hand
encounter.player_apply_card('Neutralize') == False

'C:\Users\benbu\OneDrive\Documents\sem 1 2023\csse1001\assignment_2\A2\games\game1.txt'