from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition           #remember to import and use a transition!
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.theming import ThemeManager
#Barebones structure
Builder.load_string("""
<StartupWindow>:
    FloatLayout: 
        Button: 
            text: f"Covihelp"
            background_color : 0, 0, 1, 1 
            on_press: 
                root.manager.transition.duration : 1 
                root.manager.current = 'chat_screen' 
        Label:
            text: f"Tap to start"
            pos: 0, -20
            background_color: 0, 0, 1, 1

<MainChatWindow>:
    BoxLayout:
        Button:
            text: "Ok"
            background_color: 1, 0, 0, 1
            on_press:
                root.manager.transition.duration : 2
                root.manager.current = "start_screen"
""")

sm = ScreenManager(transition=FadeTransition())            #used to switch between screens with a smooth transition

class MainApp(App):            #app instance, returns screen manager
    theme_cls = ThemeManager()
    def build(self):
        return sm

class StartupWindow(Screen):      #screen classes, being designed in the kv file
    pass

class MainChatWindow(Screen):
    pass


sm.add_widget(StartupWindow(name="start_screen"))
sm.add_widget(MainChatWindow(name="chat_screen"))

if __name__ == "__main__":
    MainApp().run()