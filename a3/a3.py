import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional

# C:\code\sem_1_2023\csse1001\a3\a3_support.py
# from a3.a3_support import *
# from a3.model import *
# from a3.constants import *
from a3_support import *
from model import *
from constants import *

class InfoBar(AbstractGrid):
    """
    Represents the InfoBar for the farm game.
    """
    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """
        Constructor for the InfoBar.

        Sets up this InfoBar to be an AbstractGrid with the appropriate
        number of rows and columns, and the appropriate width and height.

        Parameters:
            master (tk.TK | tk.Frame): The master Tk root.
        """
        super().__init__(master, (2, 3), (700, INFO_BAR_HEIGHT))
        self.configure(bg = 'light grey')
        self._day = 1
        self._money = 0
        self._energy = 100
        self.redraw(self._day, self._money, self._energy)

    def redraw(self, day: int, money: int, energy: int) -> None:
        """ Clears the InfoBar and redraws it to display the
            provided day, money, and energy.

        Parameters:
            day (int): The current day in farm game.
            money (int): The money of the player.
            energy (int): The energy of the player.
        """
        self.delete(tk.ALL)
        # print(day, money, energy)
        self.annotate_position((0,0), 'Day:', HEADING_FONT)
        self.annotate_position((0,1), 'Money:', HEADING_FONT)
        self.annotate_position((0,2), 'Energy:', HEADING_FONT)
        self.annotate_position((1,0), str(day))
        self.annotate_position((1,1), f'${money}')
        self.annotate_position((1,2), str(energy))


class FarmView(AbstractGrid):
    """
    Represents the FarmView for the farm game.
    """
    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                size: tuple[int, int], **kwargs) -> None:
        """
        Constructor for the FarmView.

        Sets up the FarmView to be an AbstractGrid with the appropriate dimensions
        and size, and creates an instance attribute of an empty dictionary to be used
        as an image cache.

        Parameters:
            master (tk.TK | tk.Frame): The master Tk root.
            dimensions (tuple[int, int]): The dimensions of the farm map in rows and columns.
            size (tuple[int, int]): The size of the FarmView in pixels (x,y)
        """
        super().__init__(master, dimensions, size)
        self._kwarg_list = []
        for key in kwargs:
            self._kwarg_list.append(kwargs[key])
        self._cell_size = self.get_cell_size()
        self._grass_image = get_image('images/grass.png', self._cell_size)
        self._soil_image = get_image('images/soil.png', self._cell_size)
        self._untilled_soil_image = get_image('images/untilled_soil.png', self._cell_size)
        self._image_cache = {}
        self.redraw(self._kwarg_list[0], self._kwarg_list[1], self._kwarg_list[2], self._kwarg_list[3])
        
    def redraw(self, ground: list[str], plants: dict[tuple[int, int], 'Plant'],
                player_position: tuple[int, int], player_direction: str) -> None:
        """ Clears the farm view, then creates (on the FarmView instance) the images for the ground,
            then the plants, then the player.

        Parameters:
            ground (list[str]): The ground tiles in FarmView, stored as a list of strings.
                    'G' for grass, 'U' for untilled soild, 'S' for soil.
            plants (dict[tuple[int, int], 'Plant']): A dictionary storing the coordiantes as cells as 
                                                     the key and a 'Plant' as the value.
            player_position (tuple[int, int]): The position of the player.
            player_direction (str): The direction the player is facing
        """
        self.delete(tk.ALL)  
        # For each block of strings in 'ground', create an image for each character in said string
        for i, row in enumerate(ground):
            for j, tile in enumerate(row):
                if tile == 'G':
                    self.create_image(self.get_midpoint((i, j)), image = self._grass_image)
                if tile == 'S':
                    self.create_image(self.get_midpoint((i, j)), image = self._soil_image)
                if tile == 'U':
                    self.create_image(self.get_midpoint((i, j)), image = self._untilled_soil_image)
        # For each plant in the dictionary, 'plants', create an image at the given location.
        for i in plants:
            self._plant_loc = i
            self._plant = plants[i]
            if self._plant._NAME == 'potato':
                self._plant_stage = self._plant.get_stage()
                self._plant_image = get_image(f'images/plants/potato/stage_{self._plant_stage}.png', self._cell_size, self._image_cache)
                self.create_image(self.get_midpoint(self._plant_loc), image = self._plant_image)
            if self._plant._NAME == 'kale':
                self._plant_stage = self._plant.get_stage()
                self._plant_image = get_image(f'images/plants/kale/stage_{self._plant_stage}.png', self._cell_size, self._image_cache)
                self.create_image(self.get_midpoint(self._plant_loc), image = self._plant_image)
            if self._plant._NAME == 'berry':
                self._plant_stage = self._plant.get_stage()
                self._plant_image = get_image(f'images/plants/berry/stage_{self._plant_stage}.png', self._cell_size, self._image_cache)
                self.create_image(self.get_midpoint(self._plant_loc), image = self._plant_image)
        self._player = get_image(f'images/player_{player_direction}.png', self._cell_size)
        self.create_image(self.get_midpoint(player_position), image = self._player)


class ItemView(tk.Frame):
    """
    Represents a single instance of an ItenView frame.
    Has a label and either 1 or 2 buttons.
    The label displays the name of the item and the buy and sell price.
    If the item is not a seed then there is only a sell button.
    """
    def __init__(self, master: tk.Frame, item_name: str, amount: int, select_command:
                 Optional[Callable[[str], None]] = None, sell_command: Optional[Callable[[str],
                 None]] = None, buy_command: Optional[Callable[[str], None]] = None) -> None:
        super().__init__(master, height = 500/6, width = INVENTORY_WIDTH)
        """
        Constructor for the ItemView.

        Sets up ItemView to operate as a tk.Frame, and creates all internal widgets. Sets the commands for the buy and sell buttons to the buy command and sell command each called with
        the appropriate item name respectively. Binds the select command to be called with the
        appropriate item name when either the ItemView frame or label is left clicked.

        Parameters:
            master (tk.TK | tk.Frame): The master Tk root.
            item_name (str): The name of the item.
            amount (int): The amount of the item.
        """
        self._amount = amount
        self._item_name = f'{item_name}: '
        self._sell_price = ''
        self._buy_price = ''
        self._label = tk.Label(
            self,
            text = f'{self._item_name}{self._amount}\n{self._sell_price}\n{self._buy_price}'
        )
        self._label.bind('<Button-1>', lambda x: select_command(item_name))
        self.bind('<Button-1>', lambda x: select_command(item_name))

        # This disgusting hard-coded monstrosity creates the correct label and number of buttons (buy or sell) for the item view widget.
        # Apologies I ran out of time
        if self._item_name == "Potato Seed: ":
            self._sell_price = 'Sell price: $5'
            self._buy_price = 'Buy price: $10'  
            self._buy_button = tk.Button(
                self,
                text = 'Buy',
                command = (lambda : buy_command(item_name))
            )
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        if self._item_name == "Kale Seed: ":
            self._sell_price = 'Sell price: $35'
            self._buy_price = 'Buy price: $70' 
            self._buy_button = tk.Button(
                self,
                text = 'Buy',
                command = (lambda : buy_command(item_name))
            )
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        if self._item_name == "Berry Seed: ":
            self._sell_price = 'Sell price: $40'
            self._buy_price = 'Buy price: $80' 
            self._buy_button = tk.Button(
                self,
                text = 'Buy',
                command = (lambda : buy_command(item_name))
            )
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        if self._item_name == "Potato: ":
            self._sell_price = 'Sell price: $25'
            self._buy_price = 'Buy price: $N/A' 
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        if self._item_name == "Kale: ":
            self._sell_price = 'Sell price: $110'
            self._buy_price = 'Buy price: $N/A' 
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        if self._item_name == "Berry: ":
            self._sell_price = 'Sell price: $50'
            self._buy_price = 'Buy price: $N/A' 
            self._sell_button = tk.Button(
                self,
                text = 'Sell',
                command = (lambda : sell_command(item_name))
            )
        self._label.pack(
            expand = tk.TRUE,
            fill = tk.BOTH,
            side = 'left')
        if self._buy_price != 'Buy price: $N/A':
            self._buy_button.pack(side = 'left')
        
        self._sell_button.pack(
            side = 'left',
            expand = tk.TRUE)
        self.update(0)

    def update(self, amount: int, selected: bool = False) -> None:
        """ Updates the text on the label, and the colour of this ItemView appropriately.        
        
        Parameters:
            amount (int): The amount that the item needs to be iterated by.
            selected (bool): Whether the frame of ItemView/Label of, has been selected with mouse button 1.
        """
        self._amount += amount
        if self._amount < 0:
            self._amount = 0
        # Sets the colour of the Inventory
        if self._amount >= 1:
            self._label.config(
                text = f'{self._item_name}{self._amount}\n{self._sell_price}\n{self._buy_price}',
                bg = INVENTORY_COLOUR)
            self.config(bg = INVENTORY_COLOUR)
        if selected == True:
            self._label.config(bg = INVENTORY_SELECTED_COLOUR)
            self.config(bg = INVENTORY_SELECTED_COLOUR)
        if self._amount == 0:
            self._label.config(
                text = f'{self._item_name}{self._amount}\n{self._sell_price}\n{self._buy_price}',
                bg = INVENTORY_EMPTY_COLOUR)
            self.config(bg = INVENTORY_EMPTY_COLOUR)
    

class FarmGame():
    """
    The FarmGame class is the controller of farm game. The controller is responsible for creating and maintaining
    instances of the model and view classes, event handling, and facilitating communication between the model and view classes.
    """
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        """
        Constructor for FarmGame.
        
        - Set the title of the window.
        - Create the title banner.
        - Create the FarmModel instance.
        - Create 6 instances of ItemView.
            - Potato Seed
            - Kale Seed
            - Berry Seed
            - Potato
            - Kale
            - Berry
        - Create a button to enable users to increment the day. When this button is pressed, the
          model should advance to the next day, and then the view classes should be redrawn to
          reflect the changes in the model.
        - Bind the handle keypress method to the <KeyPress> event.
        - Call the redraw method to ensure the view draws according to the current model state.
        """
        self._root = master
        # Window Title
        self.window_title = 'Farm Game'
        self._root.title(f'{self.window_title}')
        # Header
        self._header_frame = tk.Frame(
            self._root
        )
        self._header_img = get_image('images/header.png',
                                     (700,130))
        self._header_label = tk.Label(
            self._header_frame,
            image = self._header_img
        )
        # FarmView and ItemView Frame
        self._FV_IV_frame = tk.Frame(
            self._root
        )
        # Creates an instance of the FarmModel
        self._farm_model = FarmModel(map_file)
        self._dimensions = self._farm_model.get_dimensions()
        self._player = self._farm_model.get_player()
        self._selected_item = ''
        # Creates and instance of the InfoBar
        self._info_bar = InfoBar(self._root)
        # Next Day Button
        self._next_day_btn = tk.Button(
            self._root,
            text = 'Next day',
            command = self.new_day_button
        )
        # Creates the correct inputs for FarmView and creates an instance of it.
        self._ground = self._farm_model.get_map()
        self._plants = self._farm_model.get_plants()
        self._player_position = self._farm_model.get_player_position()
        self._player_direction = self._farm_model.get_player_direction()
        self._farm_view_inputs = {'ground': self._ground,
                                  'plants': self._plants,
                                  'player_position': self._player_position,
                                  'player_direction': self._player_direction}

        self._farm_view = FarmView(self._FV_IV_frame, self._farm_model.get_dimensions(), (FARM_WIDTH, 500), **self._farm_view_inputs)
        # Packing order
        self._header_frame.pack(
            fill = tk.X,
            side = tk.TOP
            )
        self._header_label.pack(
            )
        self._FV_IV_frame.pack(
            expand = tk.TRUE,
            fill = tk.BOTH,
            side = 'top'
            )
        self._farm_view.pack(
            side = 'left')
        # Creates the ItemView instances
        self._init_amounts = []
        self._player_inventory = self._player.get_inventory()
        # Creates the correct initial values of the items.
        for i in self._player_inventory:
            self._init_amounts.append(self._player_inventory[i])
        if len(self._init_amounts) < 6:
            for i in range(6-len(self._init_amounts)):
                self._init_amounts.append(0)
        self.item_views: dict[str: ItemView]
        self.item_views = {}
        # Generates the instances of ItemView and stores them in a dictionary self._item_views
        for i, k in enumerate(ITEMS):
            item_name = k
            item_view = ItemView(self._FV_IV_frame, item_name, self._init_amounts[i],
                                            select_command = self.select_item,
                                            sell_command = self.sell_item,
                                            buy_command = self.buy_item
            )
            self.item_views[item_name] = item_view
            item_view.pack(
            expand = tk.TRUE,
            fill = tk.BOTH
            )
  
        # Binds the keypress' to self._root
        self._root.bind('<KeyPress>', self.handle_keypress)

        # Packs the InfoBar and the Next Day Button 
        self._info_bar.pack()
        self._next_day_btn.pack()
    
    def new_day_button(self) -> None:
        """ Increments the day by 1.        
        """
        self._farm_model.new_day()
        self._info_bar._day += 1
        self._info_bar.redraw(self._info_bar._day, self._info_bar._money, self._info_bar._energy)
        self.redraw()
    
    def redraw(self) -> None:
        """ Redraws the entire game based on the current model state.        
        """
        self._farm_view_kwargs = self.get_farm_args()
        self._day = self._farm_model.get_days_elapsed()
        self._player_money = self._player.get_money()
        self._player_energy = self._player.get_energy()
        self._farm_view.redraw(self._farm_view_kwargs['ground'],
                               self._farm_view_kwargs['plants'],
                               self._farm_view_kwargs['player_position'],
                               self._farm_view_kwargs['player_direction'])
        self._info_bar.redraw(self._day, self._player_money, self._player_energy)
            
    def handle_keypress(self, event: tk.Event) -> None:
        """ An event handler to be called when a keypress event occurs. If a key is pressed that does not correspond to
            an event, it should be ignored. 
        
        Parameters:
            event (tk.Event): The event of a keypress, eg 'w'.
        """
        # Checks what key was pressed and performs relevant logic.
        # Event for pressing 'w': Move the player up 1 space.
        if event.char == 'w':
            if self._farm_model.get_player_position()[0] != 0:
                self._farm_model.move_player('w')
                self.redraw()
            else:
                self._player.set_direction('w')
                self.redraw()
        # Event for pressing 'a': Move the player left 1 space.
        if event.char == 'a':
            if self._farm_model.get_player_position()[1] != 0:
                self._farm_model.move_player('a')
                self.redraw()
            else:
                self._player.set_direction('a')
                self.redraw()
        # Event for pressing 's': Move the player down 1 space.
        if event.char == 's':
            if self._farm_model.get_player_position()[0] != self._dimensions[0] - 1:
                self._farm_model.move_player('s')
                self.redraw()
            else:
                self._player.set_direction('s')
                self.redraw()
        # Event for pressing 'd': Move the player right 1 space.
        if event.char == 'd':
            if self._farm_model.get_player_position()[1] != self._dimensions[1] - 1:
                self._farm_model.move_player('d')
                self.redraw()
            else:
                self._player.set_direction('d')
                self.redraw()
        # Event for pressing 'p': If possible, plant the selected plant at the current player location.
        if event.char == 'p':
            if self._selected_item in self._player.get_inventory():
                self._current_map = self._farm_model.get_map()
                self._current_tile = self._current_map[self._player.get_position()[0]][self._player.get_position()[1]]
                if self._player.get_position() not in self._farm_model.get_plants():
                    if self._current_tile == 'S':
                        if self._selected_item[0] == 'P':
                            self._selected_plant = PotatoPlant()
                            self._player.remove_item(('Potato Seed', 1))
                            self.item_views['Potato Seed'].update(-1, True)
                        if self._selected_item[0] == 'K':
                            self._selected_plant = KalePlant()
                            self._player.remove_item(('Kale Seed', 1))
                            self.item_views['Kale Seed'].update(-1, True)
                        if self._selected_item[0] == 'B':
                            self._selected_plant = BerryPlant()
                            self._player.remove_item(('Berry Seed', 1))
                            self.item_views['Berry Seed'].update(-1, True)
                        self._farm_model.add_plant(self._player.get_position(), self._selected_plant)
                        self.redraw()
        # Event for pressing 'h': If possible, harvest the selected plant at the current player location.
        if event.char == 'h':
            self.iterable_plants = (self._farm_model.get_plants()).copy()
            for i in self.iterable_plants:
                if self._player.get_position() == i:
                    self._harvest = self._farm_model.harvest_plant(self._player.get_position())
                    if self._harvest != None:
                        self._player.add_item(self._harvest)
                        self.item_views[self._harvest[0]].update(self._harvest[1])
                        self.redraw()
            self.redraw()
        # Event for pressing 'r': If possible, remove the selected plant at the current player location.
        # Will return the plant back to the inventory as a seed no matter the stage of the plant.
        if event.char == 'r':
            if self._player.get_position() in self._farm_model.get_plants():
                self._removed_plant = self._farm_model.get_plants()[self._player.get_position()]
                self._farm_model.remove_plant(self._player.get_position())
                print(self._removed_plant.get_name()[0])
                if self._removed_plant.get_name()[0] == 'p':
                    print(self._player.get_inventory())
                    self._player.add_item(('Potato Seed', 1))
                    self.item_views['Potato Seed'].update(1, 0)
                if self._removed_plant.get_name()[0] == 'k':
                    print(self._player.get_inventory())
                    self._player.add_item(('Kale Seed', 1))
                    self.item_views['Kale Seed'].update(1, 0)
                if self._removed_plant.get_name()[0] == 'b':
                    print(self._player.get_inventory())
                    self._player.add_item(('Berry Seed', 1))
                    self.item_views['Berry Seed'].update(1, 0)
                self.redraw()
        # Event for pressing 't': If possible, till the soil at the current player location.
        if event.char == 't':
            self._farm_model.till_soil(self._player.get_position())
            self.redraw()
        # Event for pressing 'u': If possible, untill the soil at the current player location.
        if event.char == 'u':
            self._farm_model.untill_soil(self._player.get_position())
            self.redraw()
        # Event for pressing 'm': Cheat code to give the player $10000 for testing purposes.
        # if event.char == 'm':
        #     self._player._money = 10000
        #     self.redraw()

    def select_item(self,  item_name: str) -> None:
        """ The callback to be given to each ItemView
            for item selection. This method should set the selected item to be item name and then redraw the view.
        
        Parameters:
            item_name (str): The name of the item from ItemView that is being selected.
        """
        for i in self.item_views:
            if self.item_views[i]._amount > 0:
                if i == item_name:
                    self._selected_item = item_name
                    self._player.select_item(item_name)
                    self.item_views[i].update(0, True)
                else:
                    self.item_views[i].update(0, False)
        self.redraw()

    def buy_item(self, item_name: str) -> None:
        """ The callback to be given to each ItemView for buying items. 
            This method should cause the player to attempt to buy the item with the
            given item name, at the price specified in BUY PRICES, and then redraw the view
                    
        Parameters:
            item_name (str): The name of the item from ItemView that is being selected.
        """
        if self._player.get_money() >= BUY_PRICES[item_name]:
            self.item_views[item_name].update(1)
            self._player.buy(item_name, BUY_PRICES[item_name])
            self.redraw()
    
    def sell_item(self, item_name: str) -> None:
        """ The callback to be given to each ItemView for selling items. 
            This method should cause the player to attempt to sell the item with the
            given item name, at the price specified in SELL PRICES, and then redraw the view.

        Parameters:
            item_name (str): The name of the item from ItemView that is being selected.
        """
        self.item_views[item_name].update(-1)
        self._player.sell(item_name, SELL_PRICES[item_name])
        self.redraw()
        
    def get_farm_args(self) -> dict:
        """ A function to generate the values that get used to create an instance of FarmView.
        """
        self._ground = self._farm_model.get_map()
        self._plants = self._farm_model.get_plants()
        self._player_position = self._player.get_position()
        self._player_direction = self._player.get_direction()
        self._farm_view_kwargs = {'ground': self._ground,
                                  'plants': self._plants,
                                  'player_position': self._player_position,
                                  'player_direction': self._player_direction}
        return self._farm_view_kwargs
    

def play_game(root: tk.Tk, map_file: str) -> None:
    """ Creates an instance of the controller and runs root.mainloop().
    """
    farm_game = FarmGame(root, map_file)
    root.mainloop()

  
def main() -> None:
    """ The main function. Creates the root tk.TK instance and runs the play_game function.
    """
    game = tk.Tk()
    play_game(game, 'maps/map1.txt')


if __name__ == '__main__':
    main()
