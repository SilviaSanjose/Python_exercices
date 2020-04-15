import sys
from PyQt5.Qt import QApplication, QMainWindow
from ventanas_clases.registro_cancion import Registrar_cancion
from ventanas_clases.listado_canciones import Listado_canciones
from ventanas_clases.tabla_canciones import Tabla_Canciones
from ventanas_clases.bienvenidos import VentanaMusical
from ventanas.ventana_cambio import Ui_editor_window
from ventanas_clases.registro_usuario import Registro_usuario



app = QApplication(sys.argv)
my_win = QMainWindow()

my_win.setStyleSheet("QMainWindow{background-image: url(ventanas/music.jpg)}")



#creo las interfaces de las ventanas secundarias
win_registro_cancion = Registrar_cancion()
win_listado_cancion = Listado_canciones()
win_editar_cancion = Ui_editor_window()
win_tabla_canciones = Tabla_Canciones(my_win, win_editar_cancion)
win_registro_usuarios = Registro_usuario()


win_bienvenidos = VentanaMusical(my_win, win_registro_cancion, win_listado_cancion, win_tabla_canciones, win_registro_usuarios)
win_bienvenidos.setupUi(my_win)

my_win.show()


sys.exit(app.exec_())
