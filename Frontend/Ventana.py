from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFrame, QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtGui import QIcon, QPixmap

class Ventana:

    def __init__(self):

        app = QApplication([]) # Crear una de PyQt
        ventana = QMainWindow() # Crear una ventana

        #Paleta Colores

        self.colorFondo = '#373739'
        self.primerGris = "#19191a"
        self.segundoGris = "#4A4A4D"
        self.textoGris = "#C6C6C6"

        # Hacer el resize correspondiente de tkinter
        X, Y = self.obtenerProporciones(70, 70)
        ventana.resize(X, Y)

        icono = QIcon(r"Frontend/Imagenes/Icono.png")
        ventana.setWindowIcon(icono)
        ventana.setWindowTitle("ADN")
        ventana.setStyleSheet("background-color: {};".format(self.colorFondo))

        self.generarFrames(ventana)

        ventana.show()  
        app.exec() # Mainloop de tkinter

    def obtenerProporciones(self, Ancho, Largo):

        pantalla = QGuiApplication.primaryScreen()
        pantallaSize = pantalla.size()

        X = (pantallaSize.width()) * Ancho // 100
        Y =  (pantallaSize.height()) * Largo // 100

        return X, Y;

    def generarFrames(self, Ventana):

        widgetPrincipal = QWidget(Ventana)
        Contenedor = QVBoxLayout(widgetPrincipal)

        primerFrame = QFrame()
        primerFrame.setStyleSheet(f"background-color : {self.segundoGris};")
        primerFrame.setContentsMargins(0, 0, 0, 0)
        Contenedor.addWidget(primerFrame, 5)

        segundoFrame = QFrame()
        segundoFrame.setStyleSheet(f"background-color: red;")
        segundoFrame.setContentsMargins(0, 0, 0, 0)
        Contenedor.addWidget(segundoFrame, 80)

        tercerFrame = QFrame()
        tercerFrame.setStyleSheet(f"background-color: blue;")
        tercerFrame.setContentsMargins(0, 0, 0, 0)
        Contenedor.addWidget(tercerFrame, 15)

        Ventana.setCentralWidget(widgetPrincipal)
