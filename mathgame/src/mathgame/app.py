"""
An application built with Beeware's Toga to test basic math
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import random

score = 0
attempt = 0

# class SequenceNumbers(toga.window):
class Mathgame(toga.App):
    

    def chooseoptions(self):
        initialNum = random.randint(0,20)

        options = [0,0,0]
        options[0]=initialNum+1
        options[1]=initialNum+random.randint(2,4)
        options[2]=initialNum-random.randint(0,3)
        
        #initialNum, choices = chooseoptions()
        choice1 = random.randint(0,2)
        if choice1 == 0:
            choice2 = 1
        elif choice1 == 1:
            choice2 = 2
        else:
            choice2 = 0

        if choice1 == 0:
            choice3 = 2
        elif choice1 == 1:
            choice3 = 0
        else:
            choice3 = 1
            
        button1label = options[choice1]
        button2label = options[choice2]
        button3label = options[choice3]
        return(initialNum,button1label,button2label,button3label)   

    def check_answer(self,widget):
        global score 
        global attempt
        if int(widget.label) == int(self.number_display.value) + 1:
            score = score + 1
            attempt = attempt + 1
            print(score,attempt)
   
            self.update_labels(widget)
        else:
            attempt = attempt + 1
            print(score,attempt)
            self.score_display.value = f'{score} / {attempt}'

    def startSequence(self):
        self.btn_open_sequence.enabled=False
        self.btn_open_addition.enabled=True
        
        # sequence_box = toga.Box(style=Pack(direction=COLUMN))    
        def create_labels():
            button_labels = self.chooseoptions()    
            print(button_labels)
            question_label = toga.Label(
                'What is the next number?',
                style=Pack(
                    padding=(0, 5),
                    font_size=16,
                )
            )
            self.number_display = toga.TextInput(
                style=Pack(
                    flex=1,
                    font_size=16,
                ), 
                initial=button_labels[0],
                readonly=True
            )
            
            question_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
            question_box.add(question_label)
            question_box.add(self.number_display)

            self.button1 = toga.Button(
                f'{button_labels[1]}',
                id = f'{button_labels[1]}',
                on_press=self.check_answer,
                style=Pack(
                    padding=5, 
                    background_color='Orange',
                    font_size=16,
                )
            )
            self.button2 = toga.Button(
                f'{button_labels[2]}',
                id = f'{button_labels[2]}',
                on_press=self.check_answer,
                style=Pack(
                    padding=5, 
                    background_color='Blue',
                    font_size=16,
                )
            )
            self.button3 = toga.Button(
                f'{button_labels[3]}',
                id = f'{button_labels[3]}',
                on_press=self.check_answer,
                style=Pack(
                    padding=5, 
                    background_color='Green',
                    font_size=16,
                )
            )

            self.score_display = toga.TextInput(
                style=Pack(
                    flex=1,
                    font_size=10,
                ), 
                initial=f'{score} / {attempt}',
                readonly=True
            )

            self.sequence_box.add(question_box)
            self.sequence_box.add(self.button1)
            self.sequence_box.add(self.button2)
            self.sequence_box.add(self.button3)
            self.sequence_box.add(self.score_display)
            
        create_labels()

        # return(sequence_box)

    def update_labels(self,widget):
        button_labels = self.chooseoptions()
        print(button_labels)
        self.number_display.value = button_labels[0]
        self.button1.label = button_labels[1]
        self.button2.label = button_labels[2]
        self.button3.label = button_labels[3]
        self.score_display.value = f'{score} / {attempt}'  
        

    def startup(self):
        """
        Construct and show the Toga application.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_button_box = toga.Box(style=Pack(direction=ROW))
        def open_sequence(widget):
            print('sequence')
            # main_box.remove(main_button_box)
            # main_box.add(self.startSequence())
            sequence_window = toga.Window(title="Sequence")
            self.windows.add(sequence_window)
            self.sequence_box = toga.Box(style=Pack(direction=COLUMN)) 
            sequence_window.content = self.sequence_box
            self.startSequence()
            sequence_window.show() #why doen't this work?

        def open_addition(widget):
            print('addition')
            print(main_box.children)
            # main_box.remove(main_box.children)
            pass

        self.btn_open_sequence = toga.Button(
            'Sequence',
            on_press=open_sequence,
            style=Pack(
                padding=5, 
                font_size=16,
            ),
            enabled=True
        )
        self.btn_open_addition = toga.Button(
            'Addition',
            on_press=open_addition,
            style=Pack(
                padding=5, 
                font_size=16,
            ),
            enabled=False
        )
        self.num_input1 =toga.NumberInput(
            min_value=0,
            max_value=20,
            style=Pack(
                padding=5, 
                font_size=16,
            ),
        )
        main_button_box.add(self.btn_open_sequence)
        main_button_box.add(self.btn_open_addition)
        main_button_box.add(self.num_input1)

        main_box.add(main_button_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return Mathgame()
