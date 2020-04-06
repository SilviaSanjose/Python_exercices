import sys
from PyQt5.Qt import QApplication, QMainWindow
from ventanas_clases.registro_cancion import Registrar_cancion
from ventanas_clases.listado_canciones import Listado_canciones
from ventanas_clases.tabla_canciones import Tabla_Canciones
from ventanas_clases.bienvenidos import VentanaMusical


app = QApplication(sys.argv)
my_win = QMainWindow()

my_win.setStyleSheet("QMainWindow{background-image: url(ventanas/music.jpg)}")



#creo las interfaces de las ventanas secundarias
win_registro_cancion = Registrar_cancion()
win_listado_cancion = Listado_canciones()
win_tabla_canciones = Tabla_Canciones()

win_bienvenidos = VentanaMusical(my_win, win_registro_cancion, win_listado_cancion, win_tabla_canciones)
win_bienvenidos.setupUi(my_win)

my_win.show()


sys.exit(app.exec_())
