import sys
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow
from PyQt5.QtCore import Qt
from GridWidget import GridWidget
from ControllerWidget import Actions
from Commands import Game
import ctypes

class MainWindow(QMainWindow):
    
    #inicializamos la variable actual_game para prevensión de errores.
    actual_game = None
    
    #construimos la ventana principal y iniciamos los widgets
    def __init__ (self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setGeometry(100,100,1100,950)
        self.setWindowTitle("Animales V2")
        self.grid= GridWidget(parent=self)
        self.actual_game = Game()
        self.grid.set_map(self.actual_game.get_map())
        self.grid.set_map_size(self.actual_game.get_map_size())
        self.setCentralWidget(self.grid)

        self.actions = Actions(self)
        self.addDockWidget(Qt.RightDockWidgetArea,self.actions)

        self.actions.reset.clicked.connect(self.reset)
        self.actions.newcycles.clicked.connect(self.newcycles)
        self.actions.new_entitys_bambu.clicked.connect(lambda: self.create_new_entity("bambu"))
        self.actions.new_entitys_panda.clicked.connect(lambda: self.create_new_entity("panda"))
        self.actions.actualizar.clicked.connect(self.update)

    #definimos la variable reset, esta generará un reinicio en el juego.
    
    
    #definimos una función para actualizar el mapa luego de cada acción.
    def update(self):
        self.grid.set_map(self.actual_game.get_map())
        map_size = self.actual_game.get_map_size()
        self.grid.reset(map_size)
        
    #definimos una función para crear las nuevas entidades  
    def create_new_entity(self,entity_type):
        new_entitys = self.actions.__new_entitys__.value()
        if entity_type == "panda":
            self.actual_game.new_entitys(new_entitys,"panda")
        else:
            self.actual_game.new_entitys(new_entitys,"bambu")
        map_size = self.actual_game.get_map_size()
        self.grid.reset(map_size)
    
    #definimos una función para crear los nuevos ciclos
    def newcycles(self):
        cycles = self.actions.__cycles__.value()
        map_size = self.actual_game.get_map_size()
        for n in range(0,cycles):
            self.actual_game.newcycles()
            self.grid.reset(map_size)
        print("Nuevos ciclos...")
        
    def reset(self):
        print("Reseteando...")
        map_size = self.actions.__mapsize__.value()
        animals = self.actions.__animals__.value()
        #verificamos que el tamaño y cantidad de animales sean correctos
        if map_size >= 2:
            if animals >= 2:
                self.actual_game.reset(map_size,animals)
                self.grid.set_map_size(map_size)
                self.update()
            else:
                ctypes.windll.user32.MessageBoxW(0, "La cantidad de entidades es menor a la mínima para iniciar el juego.", "Error!", 0)
                pass
        else:
            ctypes.windll.user32.MessageBoxW(0, "El mapa es demasiado pequeño para iniciar el juego, el mínimo es de 2x2.", "Error!", 0)
            pass
        self.update()

#iniciamos la ventana principal
CurrentExitCode = 0
app = QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
