import sys
from R16_19QListWidget.pelu_dialog import Ui_Pelu_Dialog
from PyQt5.Qt import QDialog, QApplication, QInputDialog, QListWidgetItem
'''
Agregar elementos en lista: click derecho/edit Items
Para multiple selección en una lista, en designer, se tiene que indicar en 'selectionmode'
'''

class TratamientosPelu(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pelu_Dialog()
        self.ui.setupUi(self)
        
        self.ui.lst_tratamientos.itemClicked.connect(self.seleccion)  #unica selección en campo texto
        
        self.ui.lst_tratamientos.itemSelectionChanged.connect(self.elementos_seleccion)  #para selección múltiple
        
        self.ui.btn_agregar_tto.clicked.connect(self.agregar_tratamiento)  #agregar nuevos item a la lista
        
        self.ui.btn_editar.clicked.connect(self.editar_tratamientos)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_tratamientos)
        self.ui.btn_eliminar_todos.clicked.connect(self.eliminar_todos_tratamientos)
        
        self.show()
        
    def seleccion(self):  #mostrar en text única selección
        self.ui.lbl_resultados.setText("Has seleccionado: {}".format(self.ui.lst_tratamientos.currentItem().text()))
    
    def elementos_seleccion(self):  #selección multiple en caja list
        self.ui.lst_trat_seleccionados.clear()    #borra si hubiese algún elemento ya.
        tratamientos = self.ui.lst_tratamientos.selectedItems()
        
        for t in list(tratamientos):
            self.ui.lst_trat_seleccionados.addItem(t.text())
    
    def agregar_tratamiento(self):   #añadir elementos del campo text 
        self.ui.lst_tratamientos.addItem(self.ui.txt_agregar_tto.text())
        
        self.ui.txt_agregar_tto.setText("")   #para dejar el campo en blanco una vez añadido el elemento
        self.ui.txt_agregar_tto.setFocus()    #volver a poner cursor en caja del texto
        
    def editar_tratamientos(self):
        item_editar = self.ui.lst_tratamientos.currentRow()    #selecciona el elemento de la fila seleccionada
        
        #da 2 variables, una para el texo que se ponga y otra para crear un input
        texto, resultado = QInputDialog.getText(self, "Ingresar", "Ingresar nuevo tratamiento ")
        
        if resultado == True and (len(texto) !=0):
            self.ui.lst_tratamientos.takeItem(item_editar)    #quita ese item
            self.ui.lst_tratamientos.insertItem(item_editar, QListWidgetItem(texto))    #añade nuevo item en esa fila
                   
    def eliminar_tratamientos(self):
        item_borrar = self.ui.lst_tratamientos.currentRow()   #selecciona item de la fila actual
        self.ui.lst_tratamientos.takeItem(item_borrar)       #quitar item
        
    
    def eliminar_todos_tratamientos(self):
        self.ui.lst_tratamientos.clear()
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    folleto = TratamientosPelu()
    
    sys.exit(app.exec_())
    