from ventanas.ventana_registro import Ui_registro_window
from modelo.clases import Cancion
from modelo.operacionesDB import registro_canciones_db

class Registrar_cancion(Ui_registro_window):
    
    def setupUi(self, my_win):
        super().setupUi(my_win)
      
        self.btn_save.clicked.connect(self.incluir_cancion)
        
     
    def incluir_cancion(self):
        cancion = Cancion()
        cancion.titulo = self.txt_titulo.text()
        cancion.artista = self.txt_artista.text()
        cancion.album = self.txt_album.text()
        cancion.anio = self.txt_anio.text()
        cancion.estilo = self.txt_estilo.text()
        
        registro_canciones_db(cancion)
        
        self.txt_titulo.setText("")
        self.txt_artista.setText("")
        self.txt_album.setText("")
        self.txt_anio.setText("")
        self.txt_estilo.setText("")