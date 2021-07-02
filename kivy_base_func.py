from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Builder.load_file('mynew.kv')
flag = 0


class MyWidget(Widget):
    """in the function '__init__' we can  create changeable
    characteristics of GUI design.
    (that can be changed before file.kv creation),
    [but kv.file vise versa contain only constant elements of a GUI design] """

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.widgets_config()

    def widgets_config(self):
        """function with widgets changeable parameters"""
        self.button1.text = 'send'
        self.button2.text = 'clear'
        self.label.text = 'text output'
        self.image.source = 'luffy.png'

    def key_pressed(self, keyboard, keycode, text, modifiers):
        """function of assigning other functions to keys"""
        if keycode[1] == 'enter':
            self.sending()
        elif keycode[1] == 'backspace':
            self.clear()

    def sending(self):
        info = self.info.text
        self.label.text = info
        self.info.text = ''
        self.image_changing()

    def clear(self):
        self.label.text = ''

    def image_changing(self):
        global flag
        if flag == 0:
            self.image.source = 'law.jpg'
            flag = 1
        else:
            self.image.source = 'luffy.png'
            flag = 0


class MyNew (App):

    def build(self):
        """build - Initializes the application; it will be called only once.
                If this method returns a widget (tree), it will be used as the root
                widget and added to the window. """
        application = MyWidget()
        self.win_config()
        MyKeyboard = Window.request_keyboard(None, application)
        MyKeyboard.bind(on_key_down=application.key_pressed)
        return application

    def win_config(self):
        """function for configuring parameters of the main window"""
        Window.size = (1000, 700)
        self.icon = 'luffy.png'
        self.title = 'tester'

    def build_config(self, config):
        """build_config - function for automatically generating config-file (.ini)
                with starting parameters (mean1, mean2...)
                [this parameters cannot be changed in this function before file configuring]"""

        config.setdefaults('section1', {
            'key1': 'mean1',
            'key2': 'mean2'
        })

    def on_start(self):
        """on_start - in that function should be initialized all action which
                    would be activated with app starting """

        print('All_OK')

    def on_stop(self):
        """on_stop - in that function should be initialized all action which
                    would be activated with app finishing """

        print('GOODBYE')


if __name__ == '__main__':
    MyNew().run()
