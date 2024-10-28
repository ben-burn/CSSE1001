from a2_support import *


class Card:
    """
    A super class called Card. It stores damage, block and energy cost values along with status modifiers.
    Can describe itself and display code to reproduce itself.
    """
    def __init__(self) -> None:
        """
        Initializes Card class.
        """
        return None

    def get_damage_amount(self) -> int:
        """
        Returns damage value of card.
        """
        self.damage_amount = 0
        return self.damage_amount
    
    def get_block(self) -> int:
        """
        Returns block value of card.
        """
        self.block = 0
        return self.block
    
    def get_energy_cost(self) -> int:
        """
        Returns energy value of card.
        """
        self.energy_cost = 1
        return self.energy_cost
    
    def get_status_modifiers(self) -> dict[str,int]:
        """
        Returns status modifiers of card.
        """
        self.status_modifiers = {}
        return self.status_modifiers
    
    def get_name(self) -> str:
        """
        Returns name of the card.
        """
        self.name = 'Card'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns a decription of the card.
        """
        self.description = 'A card.'
        return self.description
    
    def requires_target(self) -> bool:
        """
        Returns bool on if the card requires a target.
        """
        return True
    
    def __str__(self) -> str:
        """
        Returns the type and description of the card.
        """
        self.get_name()
        self.get_description()
        return f"{self.name}: {self.description}"
    
    def __repr__(self) -> str:
        """
        Returns the input required to reproduce the card.
        """
        self.get_name()
        return self.name + '()'
    
class Strike(Card):
    """
    Strike is a subclass of Card.
    """
    def get_damage_amount(self) -> int:
        """
        Returns damage for value the strike card.
        """
        return super().get_damage_amount() + 6
    
    def get_name(self) -> str:
        """
        Returns the name of the strike card.
        """
        self.name = 'Strike'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns the description of the strike card.
        """
        self.description = 'Deal 6 damage.'
        return self.description
    
class Defend(Card):
    """
    Defend is a subclass of Card.
    """
    def get_block(self) -> int:
        """
        Returns the block value of the defend card.
        """
        return super().get_block() + 5
    
    def get_name(self) -> str:
        """
        Returns the name of the defend card.
        """
        self.name = 'Defend'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns the description of the defend card.
        """
        self.description = 'Gain 5 block.'
        return self.description

    def requires_target(self) -> bool:
        """
        Returns false for require target for defense card.
        """
        return False
    
class Bash(Card):
    """
    Bash is a subclass of Card.
    """
    def get_damage_amount(self) -> int:
        """
        Returns the damage value of the bash card.
        """
        return super().get_damage_amount() + 7
    
    def get_block(self) -> int:
        """
        Returns the block value of the bash card.
        """
        return super().get_block() + 5
    
    def get_energy_cost(self) -> int:
        """
        Returns the energy cost of the bash card.
        """
        return super().get_energy_cost() + 1

    def get_name(self) -> str:
        """
        Returns the name of the bash card.
        """
        self.name = 'Bash'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns the description of the bash card.
        """
        self.description = 'Deal 7 damage. Gain 5 block.'
        return self.description
    
class Neutralize(Card):
    """
    Neutralize is a subclass of Card.
    """
    def get_damage_amount(self) -> int:
        """
        Returns the damage value of the neutralize card.
        """
        return super().get_damage_amount() + 3
    
    def get_energy_cost(self) -> int:
        """
        Returns the energy value of the neutralize card.
        """
        return super().get_energy_cost() - 1
    
    def get_status_modifiers(self) -> dict[str, int]:
        """
        Returns the status modifiers of the neutralize card.
        """
        self.status_modifiers = super().get_status_modifiers()
        self.status_modifiers['weak'] = 1
        self.status_modifiers['vulnerable'] = 2
        return self.status_modifiers
    
    def get_name(self) -> str:
        """
        Returns the name of the neutralize card.
        """
        self.name = 'Neutralize'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns the description of the neutralize card.
        """
        self.description = 'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.'
        return self.description
    
class Survivor(Card):
    """
    Survivor is a subclass of Card.
    """
    def get_block(self) -> int:
        """
        Returns the block value of the survivor card.
        """
        return super().get_block() + 8
    
    def get_status_modifiers(self) -> dict[str, int]:
        """
        Returns the status modifiers of the survivor card.
        """
        self.status_modifiers = super().get_status_modifiers()
        self.status_modifiers['strength'] = 1
        return self.status_modifiers
    
    def get_name(self) -> str:
        """
        Returns the name of the survivor card.
        """
        self.name = 'Survivor'
        return self.name
    
    def get_description(self) -> str:
        """
        Returns the description of the survivor card.
        """
        self.description = 'Gain 8 block and 1 strength.'
        return self.description

    def requires_target(self) -> bool:
        """
        Returns false for target requirement for the survivor card.
        """
        return False
    
class Entity:
    """
    The Entity superclass stores values for Player and Monster subclasses.
    Such values are hp and block values along with the status modifiers for strength, weak and vulnerable.
    """
    def __init__(self, max_hp: int) -> None:
        """
        Initializes the Entity class.
        """
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0

    def get_hp(self) -> int:
        """
        Returns the current hp of the entity.
        """
        return self.current_hp
    
    def get_max_hp(self) -> int:
        """
        Returns the maximum hp of the entity.
        """
        return self.max_hp
    
    def get_block(self) -> int:
        """
        Returns the current block value of the entity.
        """
        return self.block
    
    def get_strength(self) -> int:
        """
        Returns the current strength value of the entity.
        """
        return self.strength
    
    def get_weak(self) -> int:
        """
        Returns the current weak value of the entity.
        """
        return self.weak
    
    def get_vulnerable(self) -> int:
        """
        Returns the current vulnerable value of the entity.
        """
        return self.vulnerable
    
    def get_name(self) -> str:
        """
        Returns the name of the entity.
        """
        self.name = f'{self.__class__.__name__}'
        return self.name
    
    def reduce_hp(self, amount: int) -> None:
        """
        Reduces the current hp of the entity.
        """
        self.block -= amount
        if self.block < 0:
            self.current_hp += self.block
            self.block = 0
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_defeated(self) -> bool:
        """
        Returns a bool on whether the current hp of the entity is equal to 0.
        """
        if self.current_hp <= 0:
            return True
        else:
            return False
    
    def add_block(self, amount: int) -> None:
        """
        Adds an amount to the current block value.
        """
        self.block += amount
    
    def add_strength(self, amount: int) -> None:
        """
        Adds an amount to the current strength value.
        """
        self.strength += amount
    
    def add_weak(self, amount: int) -> None:
        """
        Adds an amount to the current weak value.
        """
        self.weak += amount
    
    def add_vulnerable(self, amount: int) -> None:
        """
        Adds an amount to the current vulnerable value.
        """
        self.vulnerable += amount
    
    def new_turn(self) -> None:
        """
        Resets block value to 0 and reduces weak and vulnerable values by 1.
        """
        self.block = 0
        if self.weak > 0:
            self.weak -= 1
        if self.vulnerable > 0:    
            self.vulnerable -= 1
    
    def __str__(self) -> str:
        """
        Returns the name of the player and a comparison between the current hp and the max hp.
        """
        self.get_name()
        return f"{self.name}: {self.current_hp}/{self.max_hp} HP"

    def __repr__(self) -> str:
        """
        Returns the input required to replicate the entity.
        """
        self.get_name()
        return self.name + f'({self.max_hp})'
    
class Player(Entity):
    """
    Player is a subclass of Entity. Players also manage 3 lists of cards: Deck, Hand and Discard.
    """
    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """
        Initializes the player entity.
        """
        self._init_deck = cards
        self.max_hp = max_hp
        super().__init__(self.max_hp)
        self.energy = 3
        self._deck: list[Card]
        if cards is not None:
            self._deck = cards
        else:
            self._deck = []
        self._hand: list[Card] 
        self._hand = []
        self._discard: list[Card] 
        self._discard = []
    
    def get_energy(self) -> int:
        """
        Returns the current energy of the player.
        """
        return self.energy
    
    def get_hand(self) -> list[Card]:
        """
        Returns the current hand of the player.
        """
        return self._hand
    
    def get_deck(self) -> list[Card]:
        """
        Returns the current deck of the player.
        """
        return self._deck
    
    def get_discarded(self) -> list[Card]:
        """
        Returns the current discard of the player.
        """
        return self._discard
    
    def start_new_encounter(self) -> None:
        """
        Moves all current cards in the discard to the deck.
        """
        if self._hand == []:
            for i in self._discard:
                self._deck.append(i)
            self._discard = []

    def end_turn(self) -> None:
        """
        Moves all current hand cards to the discard, empties the hand.
        """
        for i in self._hand:
            self._discard.append(i)
        self._hand = []

    def new_turn(self) -> None:
        """
        Draws a new set of cards into the hand from the deck. Sets energy to 3.
        """
        super().new_turn()
        draw_cards(self._deck, self._hand, self._discard)
        self.energy = 3

    def play_card(self, card_name: str) -> Card | None:
        """
        The player plays a card of a given name if it is in the hand and has the required energy.
        """
        for i, k in enumerate(self._hand):
            if k.get_name() == card_name and k.get_energy_cost() <= self.energy:
                self.energy -= k.get_energy_cost()
                self._discard.append(k)
                self._hand.pop(i)
                return k
        return None
    
    def __repr__(self) -> str:
        """
        Returns the input required to replicate the entity.
        """
        self.get_name()
        if self._init_deck == []:
            return self.name + f'({self.max_hp})'
        return self.name + f'({self.max_hp}, {self._init_deck})'
    
class IronClad(Player):
    """
    IronClad is a subclass of Player with a unique deck.
    """
    def __init__(self) -> None:
        """
        Initializes the IronClad player class.
        """
        self.init_deck = [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Bash()]
        super().__init__(80, self.init_deck)
    
    def __repr__(self) -> None:
        """
        Returns the input required to replice the silent player.
        """
        return f'{self.__class__.__name__}' + '()'

class Silent(Player):
    """
    IronClad is a subclass of Player with a unique deck.
    """
    def __init__(self) -> None:
        """
        Initializes the Silent player class.
        """
        self.init_deck = [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Defend(), Neutralize(), Survivor()]
        super().__init__(70, self.init_deck)
    
    def __repr__(self) -> None:
        """
        Returns the input required to replice the silent player.
        """
        return f'{self.__class__.__name__}' + '()'
    
class Monster(Entity):
    """
    Monster is a subclass of Entity. Each monster has a unique id and can perform an action.
    """
    id = -1
    def __init__(self, max_hp: int) -> None:
        """
        Initializes the Monster entity.
        """
        self.max_hp = max_hp
        super().__init__(self.max_hp)
        Monster.id += 1
        self.id = Monster.id
        
    
    def get_id(self) -> int:
        """
        Returns the unique id of the monster.
        """
        return self.id
    
    def action(self) -> dict[str, int]:
        """
        Adds a requirement for an action function in the monster entity class.
        """
        raise NotImplementedError
    
class Louse(Monster):
    """
    Louse is a subclass of Monster.
    """
    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        self.louse_action_damage = random_louse_amount()
    
    def action(self) -> dict[str, int]:
        """
        Returns the action of the louse.
        """
        self.dict = {}
        self.dict['damage'] = self.louse_action_damage
        return self.dict
    
class Cultist(Monster):
    """
    Cultist is a subclass of Monster.
    """
    num_calls = 0
    def action(self) -> dict[str, int]:
        """
        Returns the actions of the cultist.
        """
        self.dict = {}
        if self.num_calls == 0:
            self.dict['damage'] = self.num_calls
            self.num_calls += 1
        else:
            self.dict['damage'] = 6 + self.num_calls
            self.num_calls += 1
        self.dict['weak'] = (self.num_calls - 1) % 2
        return self.dict

class JawWorm(Monster):
    """
    JawWorm is a subclass of Monster.
    """
    def action(self) -> dict[str, int]:
        """
        Returns the action of the jawworm. Also changes the block value.
        """
        hp_dif = self.max_hp - self.current_hp
        self.dict = {}
        if hp_dif % 2 == 0:
            damage = int(hp_dif / 2)
            self.block = damage
            self.dict['damage'] = damage
            return self.dict
        else:
            damage = int((hp_dif / 2) - 0.5)
            self.block = int((hp_dif / 2) + 0.5)
            self.dict['damage'] = damage
            return self.dict   

class Encounter:
    """
    The Encounter class consists of a Player and a list of Monsters.
    The functions within cover the actions and turns of the Player and Monsters.
    """
    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        Initializes the Encounter class.
        """
        self._monster_list: list[Monster]
        self._monster_list = []
        self._player = player
        for k in monsters:
            if k[0] == 'Louse':
                self._monster_list.append(Louse(k[1]))
            elif k[0] == 'Cultist':
                self._monster_list.append(Cultist(k[1]))
            elif k[0] == 'JawWorm':
                self._monster_list.append(JawWorm(k[1]))
        self._player.start_new_encounter() 
        self.start_new_turn()

    def start_new_turn(self) -> None:
        """
        Makes the player entity start a new turn.
        """
        self._player.new_turn()
    
    def end_player_turn(self) -> None:
        """
        Ends the turn of the player entity.
        """
        self._player.end_turn()
        for i in self._monster_list:
            i.new_turn()
    
    def get_player(self) -> Player:
        """
        Returns the player entity in the current encounter.
        """
        return self._player
    
    def get_monsters(self) -> list[Monster]:
        """
        Returns the list of monsters in the current encounter.
        """
        return self._monster_list
    
    def is_active(self) -> bool:
        """
        Returns a bool on if the monster list is empty or not.
        """
        if self._monster_list != []:
            return True
        else:
            return False
   
    def player_apply_card(self, card_name: str, target_id: int | None = None) -> bool:
        """
        Applies all the effects of a card being played by the player.
        """
        # Set up target_id_list
        caf = '\nCard application failed.\n'
        target_id_list = []
        for i in self._monster_list:
            target_id_list.append(i.get_id())
        if self._player.get_hand() == []:
            print(caf)
            return False
        
        # Store current energy and hand of player
        player_energy_check = self._player.get_energy()
        self._re_hand = self._player._hand.copy()

        # Create Card and Card attributes
        self._card = self._player.play_card(card_name)
        if self._card == None:
            print(caf)
            return False
        self.card_damage = self._card.get_damage_amount()
        self.card_block = self._card.get_block()
        self.card_energy = self._card.get_energy_cost()
        self.status_modifiers = self._card.get_status_modifiers()
        self.card_target = self._card.requires_target()

        # Check target logic
        if self.card_target == True and target_id == None:
            self._player.energy += self.card_energy
            self._player._hand = self._re_hand
            print(caf)
            return False
        elif target_id not in target_id_list and self.card_target == True:
            self._player.energy += self.card_energy
            self._player._hand = self._re_hand
            print(caf)
            return False
        
        # Determine target monster id
        if target_id != None:
            for i in self._monster_list:
                if i.get_id() == target_id:
                    self._target_monster = i
        
        # Check energy
        if self.card_energy > player_energy_check:
            self._player.energy += self.card_energy 
            self._player._hand = self._re_hand
            print(caf)
            return False
        
        # Add Status modifiers
        self._player.add_block(self.card_block)
        if 'strength' in self.status_modifiers:
            self._player.add_strength(self.status_modifiers['strength'])
        if 'vulnerable' in self.status_modifiers:
            self._target_monster.add_vulnerable(self.status_modifiers['vulnerable'])
        if 'weak' in self.status_modifiers:
            self._target_monster.add_weak(self.status_modifiers['weak'])
        self.damage = self._card.get_damage_amount()
        if self.damage == 0:
            return True
        else:
            # Apply damage
            self.player_damage = self.card_damage + self._player.get_strength()
            if self._player.get_weak() > 0:
                self.player_damage = int(self.player_damage*0.75)
                self._target_monster.reduce_hp(self.player_damage)
            elif self._target_monster.get_vulnerable() > 0:
                self.player_damage = int(self.player_damage*1.5)
                self._target_monster.reduce_hp(self.player_damage)
            elif self._player.get_weak() > 0 and self._target_monster.get_vulnerable() > 0:
                self.player_damage = (self.player_damage*0.75)
                self.player_damage = int(self.player_damage*1.5)
                self._target_monster.reduce_hp(self.player_damage)
            else:
                self._target_monster.reduce_hp(self.player_damage)
            if self._target_monster.is_defeated() == True:
                for i, k in enumerate(self._monster_list):
                    if k.get_id() == self._target_monster.get_id():
                        self._monster_list.pop(i)
        return True

    def enemy_turn(self) -> None:
        """
        All the monsters in the current monster list perform their action.
        """
        if self._player.get_hand() != []:
            return None
        for monster in self._monster_list:
            actions = monster.action()
            if 'strength' in actions:
                actions['damage'] += actions['strength']
            if 'weak' in actions:
                self._player.add_weak(actions['weak'])
            if 'vulnerable' in actions:
                self._player.add_vulnerable(actions['vulnerable'])
            if self._player.get_vulnerable() > 0:
                if 'damage' in actions:
                    self._player.reduce_hp(int(1.5 * actions['damage']))
            elif monster.get_weak() > 0:
                if 'damage' in actions:
                    self._player.reduce_hp(int(0.5 * actions['damage']))
            elif self._player.get_vulnerable() > 0 and monster.get_weak() > 0:
                if 'damage' in actions:
                    self._player.reduce_hp(int((1.5 * actions['damage']) * 0.5))
            elif 'damage' in actions:
                self._player.reduce_hp(int(actions['damage']))
        self._player.new_turn()


def main():
    """
    The main function allows a user to choose and Player-Type and a game file.
    Runs all necessary functions based of the input of the user.
    """
    # Initiate Player
    while True:
        command_player = input("Enter a player type: ")
        if command_player == 'ironclad':
            player = IronClad()
            break
        elif command_player == 'silent':
            player = Silent()
            break
    
    # Initiate game file
    command_game_file = input("Enter a game file: ")
    game_file = read_game_file(command_game_file)
    player_death = 0
    monster_list_empty = 0
    for k in game_file:
        if player_death == 1:
            print('\nYou have lost the game!\n')
            return None
        encounter = Encounter(player, k)
        print('New encounter!\n')
        display_encounter(encounter)
        while True:
            if encounter._monster_list == []:
                monster_list_empty += 1
                print('\nYou have won the encounter!\n')
                break

            # Categorize player move
            player_move = input("Enter a move: ")
            if len(player_move.split(' ')) == 2:
                player_move_action = player_move.split(' ')[0]
                player_move_action_command = player_move.split(' ')[1]
            elif len(player_move.split(' ')) == 3:
                player_move_action = player_move.split(' ')[0]
                player_move_action_command = player_move.split(' ')[1]
                player_move_action_target = int(player_move.split(' ')[2])
            else:  
                player_move_action = player_move
            
            # Execute logic based off player move
            if player_move == 'end turn':
                encounter.end_player_turn()
                encounter.enemy_turn()
                if player.is_defeated() == True:
                    player_death += 1
                    break
                display_encounter(encounter)
            elif player_move_action == 'inspect':
                if player_move_action_command == 'deck':
                    print(f'\n{player.get_deck()}\n')
                elif player_move_action_command == 'discard':
                    print(f'\n{player.get_discarded()}\n')
            elif player_move_action == 'describe':
                if player_move_action_command == 'Strike':
                    dummy_card = Strike()
                    print(f'\n{dummy_card.get_description()}\n')
                if player_move_action_command == 'Defend':
                    dummy_card = Defend()
                    print(f'\n{dummy_card.get_description()}\n')
                if player_move_action_command == 'Bash':
                    dummy_card = Bash()
                    print(f'\n{dummy_card.get_description()}\n')
                if player_move_action_command == 'Neutralize':
                    dummy_card = Neutralize()
                    print(f'\n{dummy_card.get_description()}\n')
                if player_move_action_command == 'Survivor':
                    dummy_card = Survivor()
                    print(f'\n{dummy_card.get_description()}\n')
            elif player_move_action == 'play':
                if len(player_move.split(' ')) == 2:
                    if encounter.player_apply_card(player_move_action_command) ==  False:
                        pass
                    else:
                        display_encounter(encounter)
                elif len(player_move.split(' ')) == 3:
                    if encounter.player_apply_card(player_move_action_command, player_move_action_target) == False:
                        pass
                    else:
                        display_encounter(encounter)
    if monster_list_empty == len(game_file) and player.is_defeated() == False:
        print('\nYou have won the game!\n')
    else:
        print('\nYou have lost the game!\n')
    return None

if __name__ == '__main__':
    main()