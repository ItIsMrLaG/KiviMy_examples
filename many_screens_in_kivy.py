from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_string("""
<Screen1>
    size: root.width, root.height
    BoxLayout:
        horizontal: 'vertical'
        Button:
            text: 'Screen1'
            on_press: root.press_func1()
<Screen2>
    size: root.width, root.height
    BoxLayout:
        horizontal: 'vertical'
        Button:
            text: 'Screen2'
            on_press: root.press_func2()
        Button:
            text: 'щииищ'""")


class Screen1(Screen, Widget):
    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)

    def press_func1(self, *args):
        self.manager.current = 'second'
        print(1)


class Screen2(Screen, Widget):
    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)

    def press_func2(self, *args):
        self.manager.current = 'first'
        print(2)


class TestApp(App):
    def build(self):
        win = ScreenManager(transition=NoTransition())
        win.add_widget(Screen1(name='first'))
        win.add_widget(Screen2(name='second'))
        return win


if __name__ == '__main__':
    TestApp().run()