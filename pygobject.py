from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()

# Создаем окно с заголовками "Hello World"
# и отоброжаем его методом show()

window.connect("destroy", Gtk.main_quit)
Gtk.main()
