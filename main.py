from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import json
import os

class AloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text='[ Alo - Control Offline ]', font_size=24, size_hint_y=None, height=50))
        
        self.input_cliente = TextInput(hint_text='Nombre del Cliente', size_hint_y=None, height=40)
        layout.add_widget(self.input_cliente)
        
        self.input_doc = TextInput(hint_text='Documento', size_hint_y=None, height=40)
        layout.add_widget(self.input_doc)
        
        btn_registrar = Button(text='Registrar Venta', size_hint_y=None, height=50)
        btn_registrar.bind(on_press=self.registrar_venta)
        layout.add_widget(btn_registrar)
        
        self.lbl_estado = Label(text='', font_size=18)
        layout.add_widget(self.lbl_estado)
        
        return layout

    def registrar_venta(self, instance):
        cliente = self.input_cliente.text
        doc = self.input_doc.text
        if cliente and doc:
            data_path = os.path.join(self.user_data_dir, "ventas_alo.json")
            
            ventas = []
            if os.path.exists(data_path):
                with open(data_path, "r") as f:
                    try:
                        ventas = json.load(f)
                    except:
                        ventas = []
            
            ventas.append({"cliente": cliente, "documento": doc})
            
            with open(data_path, "w") as f:
                json.dump(ventas, f)
                
            self.lbl_estado.text = "VENTA REGISTRADA CON ÉXITO"
            self.input_cliente.text = ""
            self.input_doc.text = ""
        else:
            self.lbl_estado.text = "Por favor completa los campos"

if __name__ == '__main__':
    AloApp().run()
  
