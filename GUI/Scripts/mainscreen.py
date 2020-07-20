from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition   
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from functools import partial

from SeverityDeterminer import Process
import PrescriptionAppointmentRemedy as appointment

__version__ = "0.0.1"

#adding fonts
LabelBase.register(name="Futurist", fn_regular=r".\GUI\Resources\Futurist fixed-width.TTF")
LabelBase.register(name="Open Sans", fn_regular=r"GUI\Resources\OpenSans-SemiBold.ttf")
LabelBase.register(name="Montserrat", fn_regular=r"GUI\Resources\Montserrat-Regular.ttf")

question_screen_counter1 = (i for i in range(1,7))
question_screen_counter2 = (j for j in range(1,7))
name_counter = (k for k in range(2,7))

screens= []
process = Process()

def build_question_screens():
    global process, screens,question_screen_counter1
    set_1 = process.get_set_1()
    set_2 = process.get_set_2()
    set_3 = process.get_set_3()

    for question in set_1:
        screen = QuestionScreenTemplate(name=f"test_{next(question_screen_counter1)}")
        screen.set_question(question)
        screen.create_input_layout(set_1[question][0]["multi"], set_1[question][1])
        screens.append(screen)

    for question in set_2:
        screen = QuestionScreenTemplate(name=f"test_{next(question_screen_counter1)}")
        screen.set_question(question)
        screen.create_input_layout(set_2[question][0]["multi"], set_2[question][1])
        screens.append(screen)

    for question in set_3:
        screen = QuestionScreenTemplate(name=f"test_{next(question_screen_counter1)}")
        screen.set_question(question)
        screen.create_input_layout(set_3[question][0]["multi"], set_3[question][1])
        screens.append(screen)

def create_final_screen(severity, patientdata):
    print(f"inside creating final\nseverity {severity}")  
    output_text = appointment.prepare_and_send_result_mail(severity, patientdata)
    screen = QuestionScreenTemplate(name="final_result")
    screen.set_question(output_text)
    screens.append(screen)
    return screen

def get_output_from_process():
    return process.get_severity()


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
    question_label: question_label
    buttons_box: buttons_box
    screen_grid: screen_grid

    FloatLayout:
        Image:
            source: "GUI/Resources/pink bg.jpg"
            size_hint: root.size
            allow_stretch: False
            keep_ratio: True
            pos_hint: {{'center_x':.5, 'center_y':.5}}
        GridLayout:
            id: screen_grid
            cols: 1
            rows: 3
            Label:
                id: question_label
                font_size: 25
                font_name: "Montserrat"
            GridLayout:
                id: buttons_box
                cols: 3
                rows: 4

""")

class MainApp(App):            #app instance, returns screen manager
    def build(self):
        self.sm = ScreenManager(transition=FadeTransition()) 
        self.sm.add_widget(StartupWindow(name="startup")) 
        for i in screens:
            self.sm.add_widget(i)
        
        return self.sm


class StartupWindow(Screen):     
    pass


class QuestionScreenTemplate(Screen):
    answers = []
    severity = 0
    all_answers = []
    final_screen = None
    question_label = ObjectProperty(None)
    buttons_box = ObjectProperty(None)
    screen_grid = ObjectProperty(None)


    def create_input_layout(self, multi, values:list):    #creates the screen based on whether question is multi answer or not
        if multi:
            self.get_multi_option_buttons(values)
        elif multi is None:
            self.slider_specific_option()
        elif not multi:
            self.get_option_buttons(values)

    def get_multi_option_buttons(self, options:list):     #makes the options buttons (toggle)
        self.box = BoxLayout(orientation='horizontal')
        self.submit = Button(text="Submit", font_name="Open Sans", font_size=25, pos_hint={'center_x':0.5,'center_y':0.5}, size_hint=(0.5,0.5), background_color=(0, 0, 0, 0))
        self.submit.bind(on_press=partial(self.multi_input_button_pressed))
        self.box.add_widget(self.submit)
        self.multi_buttons = []
        for i in options:
            multi_button = ToggleButton(text=i)
            multi_button.background_color = 1, 0.45, 0.60, 0.25
            self.multi_buttons.append(multi_button)
            self.buttons_box.add_widget(multi_button)
        self.screen_grid.add_widget(self.box)

    def multi_input_button_pressed(self, instance):     #submit button for multi inputs
        multi_answer_entry = [i.text for i in self.multi_buttons if i.state == 'down']
        QuestionScreenTemplate.answers.append(multi_answer_entry)
        self.manager.transition.duration = 0.5
        self.manager.current = f"test_{next(name_counter)}"
        self.send_answers()

    def get_option_buttons(self, options:list):       #for single inputs
        self.buttons = []        #can be used later to iter through to get answers
        for i in options:
            button = Button(text=i, background_color=(0, 0, 0, 0), font_name="Open Sans", font_size=32, border=(255,192,203,1))
            button.bind(on_press=partial(self.single_input_button_pressed))
            self.buttons.append(button)
            self.buttons_box.add_widget(button)
            
    def single_input_button_pressed(self, instance):    #bound function to single input options
        QuestionScreenTemplate.answers.append(instance.text)
        self.manager.transition.duration = 0.5
        self.manager.current = f"test_{next(name_counter)}"
        self.send_answers()

    def slider_specific_option(self):
        self.box = BoxLayout(orientation='vertical')
        self.slider = Slider(min=10, max=100, step=1)
        self.val = Label(text=str(self.slider.value), font_size=34, color=(0,0,0,1))
        self.slider.bind(value=self.slider_value_change)
        self.submit = Button(text="Submit", font_name="Open Sans", font_size=25, pos_hint={'center_x':0.5,'center_y':0.5}, size_hint=(0.5,0.5), background_color=(0, 0, 0, 0))
        self.submit.bind(on_press=self.slider_submit_pressed)
        self.box.add_widget(self.slider)
        self.box.add_widget(self.val)
        self.box.add_widget(self.submit)
        self.buttons_box.add_widget(self.box)
    
    def slider_submit_pressed(self, instance):
        QuestionScreenTemplate.answers.append(self.slider.value)
        self.manager.transition.duration = 0.5
        try:
            self.manager.current = f"test_{next(name_counter)}"
            self.send_answers()
        except StopIteration:
            print("inside exception")
            self.send_answers()
            self.manager.current = f"final_result"
        
    def set_question(self, question:str):       #set label to question
        self.question_label.text = question

    def send_answers(self):
        print("inside send_answers")
        if self.name == 'test_2':
            process.result_1(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.all_answers.extend(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.answers = []
        elif self.name == 'test_4':
            process.result_2(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.all_answers.extend(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.answers = []
        elif self.name == 'test_6':
            print("inside send check")
            process.result_3(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.all_answers.extend(QuestionScreenTemplate.answers)
            QuestionScreenTemplate.answers = []
            QuestionScreenTemplate.severity = get_output_from_process()
            QuestionScreenTemplate.final_screen = create_final_screen(QuestionScreenTemplate.severity, QuestionScreenTemplate.all_answers)
            self.manager.add_widget(QuestionScreenTemplate.final_screen)

    def slider_value_change(self, instance, value):        #bind label to slider to display its value
        self.val.text = str(value)

    

build_question_screens()
MainApp().run()


