import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import rfidElechouse
import threading

class visualInterface(Gtk.Window):
    def __init__(self):
        # creem la finestra
        Gtk.Window.__init__(self, title="Atenea lite")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)

        # Creem la caixa i la afegim a la finestra
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(self.box)

        # Fem una caixa eventual que canvia de color
        self.evbox = Gtk.EventBox()
        self.evbox.override_background_color(0, Gdk.RGBA(0, 0, 8, 1))

        # Etiqueta
        self.label = Gtk.Label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.label.set_use_markup(True)
        self.label.set_name("Bluelabel")
        self.label.set_size_request(500, 100)

        #afegim l'etiqueta dins de la caixa eventual
        self.evbox.add(self.label)

        # Botó
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked)

        # Afegim tot a la caixa inicial
        self.box.pack_start(self.evbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)

        # Crea thread y las condiciones para pararlo
        thread = threading.Thread(target=self.scan_uid)
        thread.setDaemon(True)
        thread.start()

        self.show_all()
        Gtk.main()

    
    # Funció cridada quan es clica el botó de clear
    def clicked(self, widget):

        # Resetejem l'etiqueta
        self.label.set_label('<span foreground="white" size="x-large">Please, login with your university card</span>')
        self.evbox.override_background_color(0, Gdk.RGBA(0, 0, 8, 1))
        
        #Com el thread inicial ha finalitzat el seu "target" desapareix i hem d'iniciar un altre.
        thread = threading.Thread(target = self.scan_uid)
        thread.start()

    # Escanejem targeta
    def scan_uid(self):
    # Llegim el uid
        reader = rfidElechouse.rfidElechouse()
        uid = reader.lector()  

    # Canviem l'etiqueta per que ensenyi el uid i canvii de color
        label_text = f'UID: {uid}'
        self.label.set_label(f'<span foreground="white" size="x-large">{label_text}</span>')
        self.evbox.override_background_color(0, Gdk.RGBA(8, 0, 0, 1))

run = visualInterface()