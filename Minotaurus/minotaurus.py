## IMPORTAR MODULOS ##
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import socket

class MinotaurusApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.ip_input = TextInput(hint_text="Inserta la dirección IP de destino aquí")
        self.port_input = TextInput(hint_text="Elige el puerto al que vas a enviar los paquetes (Presiona Enter para usar el puerto predeterminado 12345)")
        self.num_packets_input = TextInput(hint_text="Cuantos paquetes quieres enviar? (Presiona Enter para usar 100)")
        self.packet_size_input = TextInput(hint_text="Tamaño del paquete en bytes (Presiona Enter para usar el tamaño predeterminado 64)")

        self.packet_type_spinner = Spinner(text='UDP', values=['UDP', 'En Mantenimiento', 'En Mantenimiento'])

        self.send_button = Button(text="ENVIAR", background_color=(1, 0, 0, 1))
        self.send_button.bind(on_press=self.send_packets)

        self.loop_button = Button(text="Bucle Totalus", background_color=(0, 0, 1, 1))
        self.loop_button.bind(on_press=self.start_loop)

        self.layout.add_widget(Label(text="Minotaurus"))
        self.layout.add_widget(self.ip_input)
        self.layout.add_widget(self.port_input)
        self.layout.add_widget(self.num_packets_input)
        self.layout.add_widget(self.packet_size_input)
        self.layout.add_widget(self.packet_type_spinner)
        self.layout.add_widget(self.send_button)
        self.layout.add_widget(self.loop_button)

        self.sent_label = Label(text="", font_name="Roboto", font_size=15)
        self.lost_label = Label(text="", font_name="Roboto", font_size=15)
        self.layout.add_widget(self.sent_label)
        self.layout.add_widget(self.lost_label)

        self.sent_packets = 0
        self.loop_active = False
        self.loop_clock = None

        return self.layout

    def send_packets(self, instance):
        ip_address = self.ip_input.text
        port_input = self.port_input.text
        num_packets_input = self.num_packets_input.text
        packet_size_input = self.packet_size_input.text

        if port_input.strip():
            port = int(port_input)
        else:
            port = 12345

        if num_packets_input.strip():
            num_packets = int(num_packets_input)
        else:
            num_packets = 100

        if packet_size_input.strip():
            packet_size = int(packet_size_input)
        else:
            packet_size = 64

        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = b"X" * packet_size
        lost_packets = 0

        try:
            for _ in range(num_packets):
                udp_socket.sendto(message, (ip_address, port))
                self.sent_packets += 1
        except Exception as e:
            lost_packets += 1
        
        self.sent_label.text = f"Paquetes enviados: {self.sent_packets}"
        self.lost_label.text = f"Paquetes perdidos: {lost_packets}"

    def start_loop(self, instance):
        if not self.loop_active:
            self.loop_active = True
            self.loop_clock = Clock.schedule_interval(self.send_packets_continuously, 0.1)
            self.loop_button.text = "Detener Bucle"
        else:
            self.stop_loop()

    def send_packets_continuously(self, dt):
        self.send_packets(None)

    def stop_loop(self):
        if self.loop_active:
            self.loop_active = False
            if self.loop_clock:
                self.loop_clock.cancel()
                self.loop_clock = None
            self.loop_button.text = "Bucle Totalus"

    def on_stop(self):
        self.stop_loop()

if __name__ == '__main__':
    MinotaurusApp().run()
