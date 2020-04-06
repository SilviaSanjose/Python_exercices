from ventanas.ventana_bienvenida import Ui_music_window



class VentanaMusical(Ui_music_window):
    def __init__(self, my_win, registro, listado, tabla):
        self.registro = registro
        self.listado = listado
        self.tabla = tabla
        self.my_win = my_win
        
    def setupUi(self, my_win):
        super().setupUi(my_win)
        self.sub_menu_registro.triggered.connect(self.mostrar_registrar_cancion)
        self.sub_meni_listado_canciones.triggered.connect(self.mostrar_listado_canciones)
        self.sub_menu_tabla_Canciones.triggered.connect(self.mostrar_tabla_canciones)
        
    def mostrar_registrar_cancion(self):
        self.registro.setupUi(self.my_win)
        
    def mostrar_listado_canciones(self):
        self.listado.setupUi(self.my_win)
        
    def mostrar_tabla_canciones(self):
        self.tabla.setupUi(self.my_win)
    
   
        
    
        