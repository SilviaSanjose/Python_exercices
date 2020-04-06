from ventanas.ventana_listado import Ui_list_canciones
from modelo.operacionesDB import listar_canciones_lista



class Listado_canciones(Ui_list_canciones):
    def setupUi(self, my_win):
        super().setupUi(my_win)
        
        self.lstw_canciones.clear()
        canciones = listar_canciones_lista()
        text = ""
        for c in canciones:
            text = str(c[0]) + "   " + str(c[1]) + "  Artista: " + str(c[2]) + "  Album/Año: " + str(c[3]) + "/" + str(c[4]) + " >>> " + str(c[5]) + "\n"
            self.lstw_canciones.addItem(text)
        