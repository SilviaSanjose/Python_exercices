from ventanas.ventana_usuarios import Ui_usuarios
from modelo.clases import Usuario
from modelo.operacionesDB import registro_usuario_db, mostrar_usuarios,\
    buscar_usuario
from PyQt5.Qt import QMessageBox


class Registro_usuario(Ui_usuarios):
    
    def setupUi(self, my_win):
        super().setupUi(my_win)
        self.my_win = my_win
        
        self.btn_save_usuario.clicked.connect(self.alta_usuario)
        
        #vuelco los nombres de los usuarios en el combox
        for element in mostrar_usuarios():
            for name in element:
                self.cbx_buscar_usuario.addItem(name)
                
        self.cbx_buscar_usuario.currentIndexChanged.connect(self.mostrar_usuario)        
          
    def mostrar_usuario(self):       
        user_name = self.cbx_buscar_usuario.itemText(self.cbx_buscar_usuario.currentIndex())
        user = buscar_usuario(user_name)
        datos = "Usuario: " + user[1] + "  Email: " + user[2] + "\nNewsletter: " + user[3] + "\nInformación Eventos: " + user[4]
        
        self.lbl_datos_usuario.setText(datos) 
        
    def alta_usuario(self):
        usuario = Usuario()
        usuario.usuario = self.txt_nombre_usuario.text()
        usuario.email = self.txt_email.text()
        if self.checkBox.isChecked():
            usuario.newsletter = "Si"
        
        if self.rbtn_si.isChecked():
            usuario.eventos = "Si"
        if self.rbtn_no.isChecked():
            usuario.eventos = "No"
        
        registro_usuario_db(usuario)   
        
        QMessageBox.about(self.my_win ,"OK", "Usuario de alta")
     
        self.setupUi(self.my_win)   
        
    