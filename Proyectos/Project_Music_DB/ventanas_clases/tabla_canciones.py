from ventanas.ventana_tabla_listado import Ui_tabla_canciones
from modelo.operacionesDB import listar_canciones_lista
from PyQt5.Qt import QTableWidgetItem
from functools import partial

class Tabla_Canciones(Ui_tabla_canciones):
    def setupUi(self, my_win):
        super().setupUi(my_win)
        
        canciones = listar_canciones_lista()
        fila = 0
        for c in canciones:
            columna = 0
            self.tableWidget.insertRow(fila)
            for i in c:
                celda= QTableWidgetItem(str(i))
                self.tableWidget.setItem(fila, columna, celda)
                columna +=1
            fila += 1
            
        self.btn_editar.clicked.connect(partial(self.editar_cancion, c[0])  )
        self.btn_eliminar.clicked.connect(self.eliminar_cancion)
        
        
    def editar_cancion(self, ed):
        print("HOla caracola", ed)
        
    def eliminar_cancion(self):
        print("HOla caracola")