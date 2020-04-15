from ventanas.ventana_tabla_listado import Ui_tabla_canciones
from modelo.operacionesDB import listar_canciones_lista, borrar_cancion,\
    obtener_cancion_por_id, guardar_cambios_cancion_db
from PyQt5.Qt import QTableWidgetItem, QMessageBox, QLabel, QPixmap, QFileDialog
from functools import partial
from modelo.clases import Cancion
import pathlib
import shutil
from validadores import validador_cancion
from validadores.validador_cancion import expresion_titulo, expresion_artista,\
    expresion_album, expresion_estilo

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
            #añado la imagen correspondiente al nº de id
            portada = QLabel()
            objeto_ruta = pathlib.Path("imagenes/" + str(c[0])+ ".jpg")
            existe = objeto_ruta.is_file()
            if existe:
                pixmap = QPixmap("imagenes/" + str(c[0])+ ".jpg")
                redimensionar_img = pixmap.scaledToHeight(40)
                portada.setPixmap(redimensionar_img)
                self.tableWidget.setCellWidget(fila, columna, portada)
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
        self.editar.comboBox.itemText(cancion_a_editar.anio)
        self.editar.txt_estilo.setText(cancion_a_editar.estilo)
        self.editar.btn_cambiar.clicked.connect(partial(self.guardar_cambios_cancion,cancion_a_editar.id))
        self.editar.btn_seleccion_img.clicked.connect(self.seleccionar_imagen)

    def guardar_cambios_cancion(self, id_guardar):
        cancion_editada = Cancion()
        cancion_editada.id = id_guardar
        cancion_editada.titulo = self.editar.txt_titulo.text()
        if not validador_cancion.validacion(cancion_editada.titulo, expresion_titulo):
            self.editar.txt_titulo.setStyleSheet("background-color: white; color: red")
            self.editar.txt_titulo.setText("***ERROR***")
            return
        else:
            self.editar.txt_titulo.setStyleSheet("background-color: white; color: black")
            
        cancion_editada.artista = self.editar.txt_artista.text()
        if not validador_cancion.validacion(cancion_editada.artista, expresion_artista):
            self.editar.txt_artista.setStyleSheet("background-color: white; color: red")
            self.editar.txt_artista.setText("***ERROR***")
            return
        else:
            self.editar.txt_artista.setStyleSheet("background-color: white; color: black")
            
        cancion_editada.album = self.editar.txt_album.text()
        if not validador_cancion.validacion(cancion_editada.album, expresion_album):
            self.editar.txt_album.setStyleSheet("background-color: white; color: red")
            self.editar.txt_album.setText("***ERROR***")
            return
        else:
            self.editar.txt_album.setStyleSheet("background-color: white; color: black")
            
        cancion_editada.anio = self.editar.comboBox.itemText(self.editar.comboBox.currentIndex())
        
        cancion_editada.estilo = self.editar.txt_estilo.text()
        if not validador_cancion.validacion(cancion_editada.estilo, expresion_estilo):
            self.editar.txt_estilo.setStyleSheet("background-color: white; color: red")
            self.editar.txt_estilo.setText("***ERROR***")
            return
        else:
            self.editar.txt_estilo.setStyleSheet("background-color: white; color: black")

        guardar_cambios_cancion_db(cancion_editada)
        try:
            shutil.move("temporal/img.jpg", "imagenes/" + str(id_guardar)+ ".jpg")
        except:
            QMessageBox.about(self.my_win, "Info", "Modificando sin portada")

        QMessageBox.about(self.my_win, "Info", "Cambios Guardados")
        
        #llamada a cargar nuevamente la ventana de Tabla de canciones
        self.setupUi(self.my_win)

    def seleccionar_imagen(self):
        file = QFileDialog.getOpenFileName()
        ruta = file[0]   #seleccionamos sólo la ruta
        shutil.copy(ruta,"temporal/img.jpg")
        pixmap = QPixmap("temporal/img.jpg")
        img_redim = pixmap.scaledToHeight(self.editar.lbl_img.height())  #imagen se ajusta de alto (alto del label)
        self.editar.lbl_img.setPixmap(img_redim)







