# Primero se importan las librerias necesarias del programa, como lo son KivyApp que contiene los metodos builder necesarios para comenzar con la app
# KivyUIX Label es para poder escribir texto y modificarlo en la pantalla del usuario
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# class KivySaludo(App):

#     # La clase build solo usa el parametro self para poder generar la pantalla y retornar Label es el texto que aparece en pantalla
#     def build(self): 

#         return Label(text = "Hola cara de rana")

# class miButton(App):
#     def disable(self, instance, *args):
#         instance.disabled= True

#     def update(self, instance, *args):
#         instance.text = "Estoy desjabilitado"

#     def build(self):
#         mybtn  = Button(text = "Haga clic para desactivar el boton", pos = (300,300), size_hint = (.25 , .18) )

#         mybtn.bind(on_press = partial(self.disable, mybtn))

#         mybtn.bind(on_press = partial(self.update, mybtn))

#         return mybtn

Builder.load_string("""

<KivyButton>:
    Button:
        text: 'Hola desde mi clase Builder'
      f  size_hint: .12 , .12 

        Image:
            source: 'URosario Logo color.png'
            center_x: self.parent.center_x
            center_x: self.parent.center_y
""")
# miButton().run()

class KivyButton(App, BoxLayout):
    def build(self):

        return self

KivyButton().run()
