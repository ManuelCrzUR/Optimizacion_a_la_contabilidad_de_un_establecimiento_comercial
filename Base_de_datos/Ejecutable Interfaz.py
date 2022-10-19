from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from Usuarios import *
from Base_de_datosUsr import *
import sqlite3

#Tama;o de ventana:
Window.size = (300, 520)


class LoginApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Indigo'

        return Builder.load_file(filename = "login.kv")

    def login(self):
        user_identificacion = self.root.ids.user.text
        verificador_base = Filtrar("usuario", f"{user_identificacion}")
        user_password = self.root.ids.password.text
        
        if len(verificador_base) == 1:
            verificador_base = verificador_base[0]
            if verificador_base [5] == user_password:
             self.dialog = MDDialog (
                title = 'Login',
                text = f'Bienvenido, {verificador_base[1]}!',
                buttons = [
                    MDFlatButton(
                        text = "OK", text_color = self.theme_cls.accent_color,
                        on_release = self.close
                    ),
                ],
            )
            self.dialog.open()   
        else:
            self.dialog = MDDialog(
                title = 'Login',
                text = f'Usuario o contraseña inexistentes.',
                buttons = [
                    MDFlatButton( 
                        text = "OK", text_color = self.theme_cls.accent_color,
                            on_release = self.close
                        ),
                    ],
            )
            self.dialog.open()


    def close(self):
        self.dialog.dismiss()

LoginApp().run()