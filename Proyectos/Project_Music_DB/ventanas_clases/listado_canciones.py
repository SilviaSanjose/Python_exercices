from ventanas.ventana_listado import Ui_list_canciones
from modelo.operacionesDB import listar_canciones_lista
from PyQt5.Qt import QMessageBox

canciones = ""

class Listado_canciones(Ui_list_canciones):
    def setupUi(self, my_win):
        super().setupUi(my_win)
        self.my_win = my_win
        global canciones
        self.lstw_canciones.clear()
        
        #Volcar información en listWidget
        canciones = listar_canciones_lista()
        text = ""
        for c in canciones:
            text = "- " + str(c[1]) + "  >>> Artista: " + str(c[2]) + "\n"
            self.lstw_canciones.addItem(text)
        
        self.lstw_canciones.itemClicked.connect(self.mostrar_informacion)
        
    def mostrar_informacion(self):
        indice = self.lstw_canciones.currentRow()
        datos = ""
        datos += "Album: " + canciones[indice][3] + "\n"
        datos += "Año: " + str(canciones[indice][4]) + "\n"
        datos += "Estilo: " + canciones[indice][5] + "\n"
        QMessageBox.about(self.my_win, "Info", datos)

        
        