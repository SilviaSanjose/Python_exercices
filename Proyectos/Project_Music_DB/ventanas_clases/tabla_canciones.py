from ventanas.ventana_tabla_listado import Ui_tabla_canciones
from modelo.operacionesDB import listar_canciones_lista, borrar_cancion,\
    obtener_cancion_por_id, guardar_cambios_cancion_db
from PyQt5.Qt import QTableWidgetItem, QMessageBox
from functools import partial
from modelo.clases import Cancion


class Tabla_Canciones(Ui_tabla_canciones):
    def __init__(self, my_win, editar):
        self.editar = editar
        self.my_win = my_win

    def setupUi(self, my_win):
        super().setupUi(my_win)
        self.my_win = my_win

        #creación la tabla
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

        self.btn_editar.clicked.connect(partial(self.editar_eliminar_cancion, "editar"))
        self.btn_eliminar.clicked.connect(partial(self.editar_eliminar_cancion, "eliminar"))

    def editar_eliminar_cancion(self, accion):
        val_id = self.spx_numero_id.value()
        if val_id == 0:
            QMessageBox.about(self.my_win, "Error", "Tienes que seleccionar un ID")
        else:
            if accion == "eliminar":
                eliminar = QMessageBox.question(self.my_win, "Alerta", "¿Quieres eliminar esa canción?")
                if eliminar == QMessageBox.Yes:
                    borrar_cancion(val_id)
                    self.setupUi(self.my_win)
            elif accion == "editar":
                editar = QMessageBox.question(self.my_win, "Alerta", "¿Quieres modificar esa canción?")
                if editar == QMessageBox.Yes:
                    self.editar_cancion(val_id)

    def editar_cancion(self,id_editar):
        self.editar.setupUi(self.my_win)
        cancion_a_editar = obtener_cancion_por_id(id_editar)
        self.editar.txt_titulo.setText(cancion_a_editar.titulo)
        self.editar.txt_artista.setText(cancion_a_editar.artista)
        self.editar.txt_album.setText(cancion_a_editar.album)
        self.editar.txt_anio.setText(str(cancion_a_editar.anio))
        self.editar.txt_estilo.setText(cancion_a_editar.estilo)
        self.editar.btn_cambiar.clicked.connect(partial(self.guardar_cambios_cancion,cancion_a_editar.id))

    def guardar_cambios_cancion(self, id_guardar):
        cancion_editada = Cancion()
        cancion_editada.id = id_guardar
        cancion_editada.titulo = self.editar.txt_titulo.text()
        cancion_editada.artista = self.editar.txt_artista.text()
        cancion_editada.album = self.editar.txt_album.text()
        cancion_editada.anio = self.editar.txt_anio.text()
        cancion_editada.estilo = self.editar.txt_estilo.text()

        guardar_cambios_cancion_db(cancion_editada)

        QMessageBox.about(self.my_win, "Info", "Cambios Guardados")
       
        self.setupUi(self.my_win)









