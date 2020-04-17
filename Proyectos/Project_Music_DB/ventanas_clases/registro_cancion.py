from ventanas.ventana_registro import Ui_registro_window
from modelo.clases import Cancion
from modelo.operacionesDB import registro_canciones_db
from PyQt5.Qt import QFileDialog, QPixmap, QMessageBox
import shutil
from validadores import validador_cancion
from validadores.validador_cancion import expresion_titulo, expresion_artista,\
    expresion_album, expresion_estilo


class Registrar_cancion(Ui_registro_window):
    
    def setupUi(self, my_win):
        super().setupUi(my_win)
        self.my_win = my_win
      
        self.btn_save.clicked.connect(self.incluir_cancion)
        self.btn_seleccion_img.clicked.connect(self.seleccionar_imagen)
     
    def incluir_cancion(self):
        cancion = Cancion()
        cancion.titulo = self.txt_titulo.text()
        if not validador_cancion.validacion(cancion.titulo, expresion_titulo):
            self.txt_titulo.setStyleSheet("background-color: white; color: red")
            self.txt_titulo.setText("***ERROR***")
            return
        else:
            self.txt_titulo.setStyleSheet("background-color: white; color: black")
            
        cancion.artista = self.txt_artista.text()
        if not validador_cancion.validacion(cancion.artista, expresion_artista):
            self.txt_artista.setStyleSheet("background-color: white; color: red")
            self.txt_artista.setText("***ERROR***")
            return
        else:
            self.txt_artista.setStyleSheet("background-color: white; color: black")
            
        cancion.album = self.txt_album.text()
        if not validador_cancion.validacion(cancion.album, expresion_album):
            self.txt_album.setStyleSheet("background-color: white; color: red")
            self.txt_album.setText("***ERROR***")
            return
        else:
            self.txt_album.setStyleSheet("background-color: white; color: black")
            
        cancion.anio = self.comboBox.itemText(self.comboBox.currentIndex())
            
        cancion.estilo = self.txt_estilo.text()
        if not validador_cancion.validacion(cancion.estilo, expresion_estilo):
            self.txt_estilo.setStyleSheet("background-color: white; color: red")
            self.txt_estilo.setText("***ERROR***")
            return
        else:
            self.txt_estilo.setStyleSheet("background-color: white; color: black")
        
        id_cancion = registro_canciones_db(cancion)
        try:
            shutil.move("temporal/img.jpg", "imagenes/" + str(id_cancion)+ ".jpg")   #movemos la img temporal, a images con nombre del id
        except:
            QMessageBox.about(self.my_win, "Info", "Registrando sin portada")
            
        self.txt_titulo.setText("")
        self.txt_artista.setText("")
        self.txt_album.setText("")
        self.comboBox.clear()
        self.txt_estilo.setText("")
    
    def seleccionar_imagen(self):
        file = QFileDialog.getOpenFileName()
        ruta = file[0]   #seleccionamos sólo la ruta
        shutil.copy(ruta,"temporal/img.jpg")
        pixmap = QPixmap("temporal/img.jpg")
        img_redim = pixmap.scaledToHeight(self.lbl_img.height())  #imagen se ajusta de alto (alto del label)
        self.lbl_img.setPixmap(img_redim)
        
        