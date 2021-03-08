"""
Roku TV Controller Using Roku Remote API
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

from roku import Roku

class rokucontroller(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """        
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        '''
            Repeating set of a label and a button enclose in a box,
            this box is then added to the main box.
            Label will show the details of what the button does and 
            button performs that action on click.
            Smilar patter should be repeated for adding more buttons
            on the interface.
        '''
        # HOME
        home_label = toga.Label(
            '(It will take you back to Roku Home)',
            style=Pack(padding=(0, 5))
        )
        home_button = toga.Button(
            'HOME',
            on_press=self.gohome,
            style=Pack(padding=5)
        )
        home_box = toga.Box(style=Pack(direction=ROW, padding=5))
        home_box.add(home_button)
        home_box.add(home_label)               
        # Add HOME to main box
        main_box.add(home_box)

        # BACK
        back_label = toga.Label(
            '(Back button of the roku remote, takes you a step back)',
            style=Pack(padding=(0, 5))
        )
        back_button = toga.Button(
            'BACK',
            on_press=self.goback,
            style=Pack(padding=5)
        )
        back_box = toga.Box(style=Pack(direction=ROW, padding=5))
        back_box.add(back_button)
        back_box.add(back_label)
        # Add Back to main box
        main_box.add(back_box)
        
        # UP
        up_label = toga.Label(
            '(UP button of the roku remote)',
            style=Pack(padding=(0, 5))
        )
        up_button = toga.Button(
            'UP',
            on_press=self.goup,
            style=Pack(padding=5)
        )
        up_box = toga.Box(style=Pack(direction=ROW, padding=5))
        up_box.add(up_button)
        up_box.add(up_label)        
        # Add UP to main box
        main_box.add(up_box)
        
        # DOWN
        down_label = toga.Label(
            '(DOWN button of the roku remote)',
            style=Pack(padding=(0, 5))
        )
        down_button = toga.Button(
            'DOWN',
            on_press=self.godown,
            style=Pack(padding=5)
        )
        down_box = toga.Box(style=Pack(direction=ROW, padding=5))
        down_box.add(down_button)
        down_box.add(down_label)        
        # Add DOWN to main box
        main_box.add(down_box)
        
        # LEFT
        left_label = toga.Label(
            '(LEFT button of the roku remote)',
            style=Pack(padding=(0, 5))
        )
        left_button = toga.Button(
            'LEFT',
            on_press=self.goleft,
            style=Pack(padding=5)
        )
        left_box = toga.Box(style=Pack(direction=ROW, padding=5))
        left_box.add(left_button)
        left_box.add(left_label)        
        # Add LEFT to main box
        main_box.add(left_box)
        
        # RIGHT
        right_label = toga.Label(
            '(RIGHT button of the roku remote)',
            style=Pack(padding=(0, 5))
        )
        right_button = toga.Button(
            'RIGHT',
            on_press=self.goright,
            style=Pack(padding=5)
        )
        right_box = toga.Box(style=Pack(direction=ROW, padding=5))
        right_box.add(right_button)
        right_box.add(right_label)        
        # Add RIGHT to main box
        main_box.add(right_box)
        
        # SELECT (OK)
        select_label = toga.Label(
            '(OK button of the roku remote)',
            style=Pack(padding=(0, 5))
        )
        select_button = toga.Button(
            'OK',
            on_press=self.select_ok,
            style=Pack(padding=5)
        )
        select_box = toga.Box(style=Pack(direction=ROW, padding=5))
        select_box.add(select_button)
        select_box.add(select_label)        
        # Add SELECT to main box
        main_box.add(select_box)
        
        self.main_window = toga.MainWindow(title="Roku Controller")
        self.main_window.content = main_box
        self.main_window.show()

    
    '''
        These are all the functions that are called when respective 
        button is clicked.
    '''
    # Home
    def gohome(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.home()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )
    
    # Back
    def goback(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.back()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )

    # Up
    def goup(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.up()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )

    # Down
    def godown(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.down()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )

    # Left
    def goleft(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.left()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )

    # Right
    def goright(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.right()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )
		    
    # Select (OK)
    def select_ok(self, widget):
	    try:
			# TODO: Make it a generalized object that all funcitions
			# can use
		    roku = Roku('192.168.1.4') 
		    roku.select()
	    except Exception as exp:
		    self.main_window.info_dialog(
		    'Oops!',"There might be some error!"
		    )

def main():
    return rokucontroller()
