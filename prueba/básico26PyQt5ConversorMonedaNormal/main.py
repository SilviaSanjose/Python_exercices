#vamos a usar el archivo generado de la ventana directamente.
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_python
import sys

'''Opcional: Incorporar un botón para transformar los euros introducidos a otra moneda que queramos OK
Un segundo botón más para transformar a otro tipo de moneda distinto
Mostrar icono en el botón correspondiente de conversión.
pyuic5 -x -o ventana_python.py ventana_principal.ui 
pyrcc5 -o icons_rc.py icons.qrc
'''
def transformar_a_dolares():
    introducido = ui.entrada_euros.text()
    introducido_float = float(introducido)
    dolares = introducido_float * 1.1
    ui.resultado_dolar.setText("Resultado en dolares: " + "{:.2f}".format(dolares))  #redondea a 2 decimales
#end transformar_a_dolares
def transformar_a_dolares_canadienses():
    introducido = ui.entrada_euros.text()
    introducido_float = float(introducido)
    canadienses = introducido_float * 1.55
    ui.resultado_dolar_canada.setText("Resultado en dolares canadienses: " + "{:.2f}".format(canadienses))

def transformar_a_libras():
    introducido = ui.entrada_euros.text()
    introducido_float = float(introducido)
    libras = introducido_float * 0.91
    ui.resultado_libra.setText("Resultado en libras: " + str(round(libras,2)))  
#end transformar_a_libras   
    
#líneas obligatorias de PyQt5
app = QtWidgets.QApplication(sys.argv)    #Para arrancar pyQt5
MainWindow = QtWidgets.QMainWindow()     #crear y preparar ventana principal

#creamos objeto de la clase en el archivo generado y lo usa para preparar la ventana
#principal llamada MainWindow para que tenga todo lo que pusimos en el designer.
ui = ventana_python.Ui_MainWindow()
ui.setupUi(MainWindow)

#todos los componentes puestos en la ventana por el designer estan ui
ui.boton_convertir_dolares.clicked.connect(transformar_a_dolares)
ui.boton_convertir_d_canadiense.clicked.connect(transformar_a_dolares_canadienses)
ui.boton_convertir_libra.clicked.connect(transformar_a_libras)


MainWindow.show()    #se muestra la ventana principal de PyQt5
sys.exit(app.exec_())