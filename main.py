from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivymd.app import MDApp

Config.set('kivy', 'window_icon', '/home/student/Desktop/Wank/Stock images/shopicon.jpg')


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


name = ''
top10 = {}
tim = 1
counter = 1

top10[1] = "Nagi"
top10[2] = "Nagi"
top10[3] = "Nagi"
top10[4] = "Nagi"
top10[5] = "Nagi"
top10[6] = "Nagi"
top10[7] = "Nagi"
top10[8] = "Nagi"
top10[9] = "Nagi"
top10[10] = "Nagi"
a1 = False
a2 = False
a3 = False
a4 = False
a5 = False
a6 = False
a7 = False
a8 = False
a9 = False
a10 = False


class Math_test(MDApp):
    data = ["2", "2", "2", "2", "20", "3", "25", "2", "7", "625"]

    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file("main.kv")

    def submit_1(self, text):
        global a1
        if text == "2":
            a1 = True
        elif text != "2":
            a1 = False

    def submit_2(self, text):
        global a2
        if text == "2":
            a2 = True
        elif text != "2":
            a2 = False

    def submit_3(self, text):
        global a3
        if text == "2":
            a3 = True
        elif text != "2":
            a3 = False

    def submit_4(self, text):
        global a4
        if text == "2":
            a4 = True
        elif text != "2":
            a4 = False

    def submit_5(self, text):
        global a5
        if text == "20":
            a5 = True
        elif text != "20":
            a5 = False

    def submit_6(self, text):
        global a6
        if text == "3":
            a6 = True
        elif text != "3":
            a6 = False

    def submit_7(self, text):
        global a7
        if text == "25":
            a7 = True
        elif text != "25":
            a7 = False

    def submit_8(self, text):
        global a8
        if text == "2":
            a8 = True
        elif text != "2":
            a8 = False

    def submit_9(self, text):
        global a9
        if text == "7":
            a9 = True
        elif text != "7":
            a9 = False

    def submit_10(self, text):
        global a10
        if text == "625":
            a10 = True
        elif text != "625":
            a10 = False

    def submit_11(self):
        global counter
        global name
        global tim
        a = 0
        ans = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
        for i in ans:
            if i:
                a = a + 1
        print(f"Правильных ответов из 10: {a}")
        top10[tim] = name + str(a)
        for key, name in top10.items():
            print(key, name)
        counter += 1
        if tim >10:
            tim = 1
        else:
            tim += 1

    def uname(self, text):
        global name
        a = 0
        ans = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
        for i in ans:
            if i:
                a = a + 1
        name = text



Math_test().run()
