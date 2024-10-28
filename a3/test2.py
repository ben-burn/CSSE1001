import tkinter as tk
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional

# C:\code\sem_1_2023\csse1001\a3\a3_support.py
from a3.a3_support import *
from a3.model import *
from a3.constants import *


class InfoBar(AbstractGrid):
    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        super.__init__(master, (2, 3), (700, INFO_BAR_HEIGHT))
        # self.annotate_position((1,1), 'Day:')
        # self.annotate_position((1,2), 'Money:')
        # self.annotate_position((1,3), 'Energy:')
        # self._init_day = 1
        # self._init_money = 0
        # self._init_energy = 100
        # self.redraw(self._init_day, self._init_money, self._init_energy)
    def redraw(self, day: int, money: int, energy: int) -> None:
        # self.annotate_position((2,1), str(day))
        # self.annotate_position((2,2), f'${money}')
        # self.annotate_position((2,3), str(energy))
        pass

def main() -> None:
    root = tk.Tk()
    root.title('farm game')
    geo_width = FARM_WIDTH + INVENTORY_WIDTH
    geo_height = INFO_BAR_HEIGHT + BANNER_HEIGHT + 500
    root.geometry(f'{geo_width}x{geo_height}') 
    info_bar = InfoBar(root)
    info_bar.pack(side = tk.BOTTOM)
    info_bar.annotate_position((5,5), 'Day:')
    root.mainloop()
    

if __name__ == '__main__':
    main()



kwargs = {'ground': ['gggggg','uuuuuuu'],
          'plants': {'berry': 1, 'potatoe': 2},
          'player_position': (1,1),
          'player_direction': 'left'}
        #   'ground_images': self._ground_images}
for key in kwargs:
    print(type(kwargs[key]), kwargs[key])  
     
x = [5,5]

for i in range(6-len(x)):
    x.append(0)


potato = 0
kale = 0
berry = 0

#buy
#       potato += 1

#redraw
#   if potatoe == 1
        # update
        # potatoe -= 1



['GGGGGGGG', 'GGGHGGGG']