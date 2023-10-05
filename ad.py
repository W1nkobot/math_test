from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton

class MyApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Создание кнопки с айди button1 и привязка функции on_button_press к событию on_release
        button1 = MDRectangleFlatButton(text="Button 1", id="button1")
        button1.bind(on_release=self.on_button_press)
        layout.add_widget(button1)

        # Создание кнопки с айди button2 и привязка функции on_button_press к событию on_release
        button2 = MDRectangleFlatButton(text="Button 2", id="button2")
        button2.bind(on_release=self.on_button_press)
        layout.add_widget(button2)

        return layout

    def on_button_press(self, instance):
        # Получение айди кнопки
        button_id = instance.id
        print(f"Button with id '{button_id}' was pressed.")

MyApp().run()
