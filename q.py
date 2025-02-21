import pyttsx3
from voice.py import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
##################

engine = pyttsx3.init() #связь с библиотекой звуков
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', ru_voice_id)
#####################
class FirstScr(Screen):
    def __init__(self, name):
        super().__init__(name=name) 
        vl = BoxLayout(orientation="vertical")
        self.txtInput = TextInput(text='Озвучь меня!')
        self.btnVoice = Button(text='Озвучить')
        self.btnVoice.on_press = self.Say
        self.btnStreet = Button(text="Улица")
        self.btnStreet.on_press = self.toStreet
        self.btnHouse = Button(text="Дом")
        self.btnHouse.on_press = self.toHouse
        self.btnShop = Button(text="Магазин")
        self.btnShop.on_press = self.toShop
        self.btnTransport = Button(text="Транспорт")
        self.btnTransport.on_press = self.toTransport
        vl.add_widget(self.txtInput)
        vl.add_widget(self.btnVoice)
        vl.add_widget(self.btnStreet)
        vl.add_widget(self.btnHouse)
        vl.add_widget(self.btnShop)
        vl.add_widget(self.btnTransport)
        self.add_widget(vl)
    def Say(self):
            engine.say(self.txtInput.text)
            engine.runAndWait()
    def toStreet(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'street'
    def toHouse(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'house'
    def toShop(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'shop'
    def toTransport(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'transport'
class Street(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        vl = BoxLayout(orientation="vertical")
        self.btn1 = Button(text="Переведите, пожалуйста, меня через дорогуПереведите, пожалуйста, меня через дорогу")
        self.btn1.on_press = lambda : self.Say("Переведите, пожалуйста, меня через дорогу")
        vl.add_widget(self.btn1)
        self.btn2 = Button(text = "Позовите охрану")
        self.btn2.on_press = lambda : self.Say("Позовите охрану")
        vl.add_widget(self.btn2)
        self.btn3 = Button(text = "Помогите выдвинуть пандус")
        self.btn3.on_press = lambda : self.Say("Помогите выдвинуть пандус")
        vl.add_widget(self.btn3)
        self.btn4 = Button(text = "Помогите!")
        self.btn4.on_press = lambda : self.Say("Помогите!")
        vl.add_widget(self.btn4)
        self.btn5 =Button(text = "Откройте, пожалуйста, дверьОткройте, пожалуйста, дверь")
        self.btn5.on_press = lambda : self.Say("Откройте, пожалуйста, дверь")
        vl.add_widget(self.btn5)
        self.btnhome = Button(text = "Главное менюГлавное меню")
        self.btnhome.on_press = self.toHome
        vl.add_widget(self.btnhome)
        self.add_widget(vl)
    def Say(self,word):
        engine.say(word)
        engine.runAndWait()
    def toHome(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
class House(Screen):    
    def __init__(self, name):
        super().__init__(name=name)
        vl = BoxLayout(orientation="vertical")
        self.btn6 = Button(text = "Помогите убраться")
        self.btn6.on_press = lambda : self.Say("Помогите убраться")
        vl.add_widget(self.btn6)
        self.btn7 = Button(text = "Помогите приготовить еду")
        self.btn7.on_press = lambda : self.Say("Помогите приготовить еду")
        vl.add_widget(self.btn7)
        self.btn8 = Button(text = "Откройте,пожалуйста,дверь")
        self.btn8.on_press = lambda : self.Say("Откройте,пожалуйста,дверь")
        vl.add_widget(self.btn8)
        self.btn9 = Button(text = "Включите, пожалуйста,телевизор")
        self.btn9.on_press = lambda : self.Say("Включите, пожалуйста,телевизор")
        vl.add_widget(self.btn9)
        self.btnhome = Button(text = "Главное меню")
        self.btnhome.on_press = self.toHome
        vl.add_widget(self.btnhome)
        self.add_widget(vl)
    def Say(self,word):
        engine.say(word)
        engine.runAndWait()
    def toHome(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
class Shop(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        vl = BoxLayout(orientation="vertical")
        self.btn10 = Button(text = "Извините")
        self.btn10.on_press = lambda : self.Say("Извините")
        vl.add_widget(self.btn10)
        self.btn11 = Button(text = "Помогите,пожалуйста,с выбором")
        self.btn11.on_press = lambda : self.Say("Помогите,пожалуйста,с выбором")
        vl.add_widget(self.btn11)
        self.btn12 = Button(text = "Достаньте,пожалуйста,этот продукт")
        self.btn12.on_press = lambda : self.Say("Достаньте,пожалуйста,этот продукт")
        vl.add_widget(self.btn12)
        self.btnhome = Button(text = "Главное меню")
        self.btnhome.on_press = self.toHome
        vl.add_widget(self.btnhome)
        self.add_widget(vl)
    def Say(self,word):
        engine.say(word)
        engine.runAndWait()
    def toHome(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
class Transport(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        vl = BoxLayout(orientation="vertical")
        self.btn13 = Button(text = "Возьмите,пожалуйста, за проезд")
        self.btn13.on_press = lambda : self.Say("Возьмите,пожалуйста, за проезд")
        vl.add_widget(self.btn13)
        self.btn14 = Button(text = "Извините")
        self.btn14.on_press = lambda : self.Say("Извините")
        vl.add_widget(self.btn14)
        self.btn15 = Button(text = "Садитесь")
        self.btn15.on_press = lambda : self.Say("Садитесь")
        vl.add_widget(self.btn15)
        self.btn16 =Button(text = "Уступите, пожалуйста,место")
        self.btn16.on_press = lambda : self.Say("Уступите, пожалуйста,место")
        vl.add_widget(self.btn16)
        self.btnhome = Button(text = "Главное меню")
        self.btnhome.on_press = self.toHome
        vl.add_widget(self.btnhome)
        self.add_widget(vl)
    def Say(self,word):
        engine.say(word)
        engine.runAndWait()
    def toHome(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'first'
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(Street(name='street'))
        sm.add_widget(House(name='house'))
        sm.add_widget(Shop(name='shop'))
        sm.add_widget(Transport(name='transport'))
        return sm


app = MyApp()
app.run()
