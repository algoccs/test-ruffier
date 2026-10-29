from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MainButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    # polimorfismo (cambiando el comportamiento del metodo)
        def on_press(self): 
            self.screen.manager.transition.direction = self.direction
            self.screen.manager.current = self.goal

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = BoxLayout(padding=10, spacing=10)
        text = Label(text='Haz click para navegar en la App!', font_size=24)

        col_buttons = BoxLayout(orientation='vertical', padding=10, spacing=10)

        col_buttons.add_widget(MainButton(self, 'left', 'first', text='Pantalla 1', font_size=24, background_color=(1,1,0,1)))
        col_buttons.add_widget(MainButton(self, 'down', 'second', text='Pantalla 2', font_size=24, background_color=(0,0,1,1)))
        col_buttons.add_widget(MainButton(self, 'up', 'third', text='Pantalla 3', font_size=24, background_color=(1,0,0,1)))
        col_buttons.add_widget(MainButton(self, 'right', 'fourth', text='Pantalla 4', font_size=24, background_color=(0,1,0,1)))

        main_layout.add_widget(text)
        main_layout.add_widget(col_buttons)

        self.add_widget(main_layout)

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MobileApp(App):
    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainWindow(name='main'))
        manager.add_widget(FirstScreen(name='first'))

        return manager

MobileApp().run()