"""
An application built with Beeware's Toga to test basic math
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random

class Mathgame(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.
        """
        main_box = toga.Box(style=Pack(direction=ROW))
        
        def open_sequence(widget):
            print('sequence')
            pass

        def open_addition(widget):
            print('addition')
            pass

        btn_open_sequence = toga.Button(
            'Sequence',
            on_press=open_sequence,
            style=Pack(
                padding=5, 
                font_size=16
            )
        )
        btn_open_addition = toga.Button(
            'Addition',
            on_press=open_addition,
            style=Pack(
                padding=5, 
                font_size=16
            )
        )

        main_box.add(btn_open_sequence)
        main_box.add(btn_open_addition)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Mathgame()
