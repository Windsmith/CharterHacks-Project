from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition           #remember to import and use a transition!
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from functools import partial

__version__ = "0.0.1"

#adding fonts
LabelBase.register(name="Futurist", fn_regular=r".\GUI\Resources\Futurist fixed-width.TTF")
LabelBase.register(name="Open Sans", fn_regular=r"GUI\Resources\OpenSans-SemiBold.ttf")
LabelBase.register(name="Montserrat", fn_regular=r"GUI\Resources\Montserrat-Thin.ttf")

question_screen_counter1 = (i for i in range(1,8))
question_screen_counter2 = (j for j in range(1,8))

global screens, current, next_
screens = [[],[],[]]

#building questions screen



Builder.load_string(f"""
#:import partial functools.partial
<StartupWindow>:
    FloatLayout:
        Image:
            source: "GUI/Resources/pink bg.jpg"
            size_hint: root.size
            allow_stretch: False
            keep_ratio: True
            pos_hint: {{'center_x':.5, 'center_y':.5}}
        Button: 
            text: f"Covihelp"
            font_size: 35
            font_name: "Futurist"
            background_color : 0, 0, 0, 0
            pos_hint: {{'center_x':.5, 'center_y':.52}}
            on_press:
                root.manager.transition.duration : 0.5
                root.manager.current = 'test_1'
        Label:
            text: f"Tap to start"
            pos: 0, -20
            background_color: 0, 0, 0, 1
<QuestionScreenTemplate>:
    name: f"test_{next(question_screen_counter1)}"
    question_label: question_label
    buttons_box: buttons_box
    submit: submit
    FloatLayout:
        Image:
            source: "GUI/Resources/pink bg.jpg"
            size_hint: root.size
            allow_stretch: False
            keep_ratio: True
            pos_hint: {{'center_x':.5, 'center_y':.5}}
        GridLayout:
            cols: 1
            rows: 3
            Label:
                id: question_label
                font_size: 32
                font_name: "Montserrat"
            BoxLayout:
                id: buttons_box
                orientation: 'horizontal'
            BoxLayout:
                id: submit
                orientation: 'horizontal'
                Button:
                    id: submit
                    text: "Submit"
                    font_name: "Open Sans"
                    font_size: 32
                    pos_hint: {{'center_x':0.5,'center_y':0.5}}

""")

class MainApp(App):            #app instance, returns screen manager
    def build(self):
        self.sm = ScreenManager(transition=FadeTransition()) 
        self.sm.add_widget(StartupWindow(name="startup")) 

        SAMPLE = {"This is a question. Are you retarded?":[{"multi":True}, ["Yes", "Yes", "Yes"]],
                "This is another question. Am I retarded?":[{"multi":False}, ["Yes", "Absolutely"]]}

        for k in SAMPLE:
            screen = QuestionScreenTemplate(name=f"test_{next(question_screen_counter2)}")
            screen.set_question(k)
            screen.create_input_layout(SAMPLE[k][0]["multi"], SAMPLE[k][1])
            self.sm.add_widget(screen)
        return self.sm


class StartupWindow(Screen):     
    pass

class CustomToggleButton(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_down = 1, 0.753, 0.796, 1
        self.background_normal = 1, 0.753, 0.796, 0
        
class QuestionScreenTemplate(Screen):
    answers = []
    question_label = ObjectProperty(None)
    buttons_box = ObjectProperty(None)
    submit = ObjectProperty(None)

    def create_input_layout(self, multi:bool, values:list):
        if multi:
            self.get_multi_option_buttons(values)
        else:
            self.get_option_buttons(values)

    def get_multi_option_buttons(self, options:list):
        self.submit.bind(on_press=partial(self.multi_input_button_pressed))
        self.multi_buttons = []
        for i in options:
            multi_button = ToggleButton(text=i)
            self.multi_buttons.append(multi_button)
            self.buttons_box.add_widget(multi_button)

    def multi_input_button_pressed(self, instance):
        multi_answer_entry = [i.text for i in self.multi_buttons if i.state == 'down']
        print(multi_answer_entry)
        QuestionScreenTemplate.answers.append(multi_answer_entry)
        self.manager.transition.duration = 0.5
        #next_screen = screens
        self.manager.current = "startup"

    def get_option_buttons(self, options:list):
        self.buttons = []        #can be used later to iter through to get answers
        for i in options:
            button = Button(text=i, background_color=(0, 0, 0, 0), font_name="Open Sans", font_size=32, border=(255,192,203,1))
            button.bind(on_press=partial(self.single_input_button_pressed))
            self.buttons.append(button)
            self.buttons_box.add_widget(button)
            
    def single_input_button_pressed(self, instance):
        QuestionScreenTemplate.answers.append(instance.text)
        self.manager.transition.duration = 0.5
        self.manager.current = "startup"

    def set_question(self, question:str):
        self.question_label.text = question


if __name__ == "__main__":
    MainApp().run()
    
