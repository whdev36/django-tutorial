from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests
from kivy.lang import Builder

Builder.load_file('login.kv')

API_URL = "http://127.0.0.1:8000"

class LoginScreen(BoxLayout):
    def do_login(self):
        data = {
            'username': self.ids.username.text,
            'password': self.ids.password.text
        }
        response = requests.post(f"{API_URL}/api/login/", data=data)
        if response.status_code == 200:
            token = response.json()['access']
            self.ids.status.text = "Login successful!"
            self.token = token
        else:
            self.ids.status.text = "Login failed!"

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()
