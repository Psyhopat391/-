from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pyttsx3
from  kivy.uix.textinput import TextInput
engine = pyttsx3.init()

ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

engine.setProperty('voice',ru_voice_id)


class FirstScr(Screen):
	def __init__(self, name):
		super().__init__(name=name)
		vl = BoxLayout(orientation="vertical")
		self.txtInput = TextInput(text='Озвучь меня!')
		self.btnVoice = Button(text="Озвучить")
		self.btnVoice.on_press = self.Say
		self.btnStreet = Button(text="Улица")
		self.btnStreet.on_press = self.toStreet
		vl.add_widget(self.txtInput)
		vl.add_widget(self.btnVoice)
		vl.add_widget(self.btnStreet)
		self.add_widget(vl)
	def Say(self):
		engine.say(self.txtInput.text)
		engine.runAndWait()
	def toStreet(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'street'
class Street(Screen):
	def __init__(self, name):
		super().__init__(name=name)
		vl = BoxLayout(orientation="vertical")
		self.btn1 = Button(text="Переведите через дорогу")
		self.btn1.on_press = lambda : self.Say("Переведите через дорогу")
		vl.add_widget(self.btn1)
		self.btn2 = Button(text="Позовите охрану")
		self.btn2.on_press = lambda : self.Say("Позовите охрану")
		vl.add_widget(self.btn2)
		self.btn3 = Button(text="Помогите выдвинуть пандус")
		self.btn3.on_press = lambda : self.Say("Помогите выдвинуть пандус")
		vl.add_widget(self.btn3)
		self.btn4 = Button(text="Помогите")
		self.btn4.on_press = lambda : self.Say("Помогите")
		vl.add_widget(self.btn4)
		self.btn5 = Button(text="ОТкройте, пожалуйста, дверь")
		self.btn5.on_press = lambda : self.Say("ОТкройте, пожалуйста, дверь")
		vl.add_widget(self.btn5)
		self.btnhome = Button(text="Главное меню")
		self.btnhome = self.toHome
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

		return sm


app = MyApp()
app.run()
