from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter,QPen, QColor,QImage
from PyQt5.QtCore import Qt , QRect

class GridWidget(QWidget):
    #definimos el tamaño por defecto del widget
    __widht__,__height__=500,500
    __map_size__= 50
    grey= QImage('grey.jpg')
    black= QImage('black.jpg')
    green= QImage('green.jpg')
    __map__ = None
    temp=0
    
    def __init__(self,parent=None):
        super(GridWidget,self).__init__(parent) 

    #creamos el paintEvent, para poder utilizar update y dibujar con esa acción
    def paintEvent(self, event):
        self.__width__= event.rect().width()
        self.__height__= event.rect().height()
        paint= QPainter()
        paint.begin(self)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#808080"))
        paint.setPen(pen)
        paint.drawRect(event.rect().x(), event.rect().y(), self.__width__-1, self.__height__-1)
        self.draw_matrix(paint)
        paint.end()
        
    #definimos el mapa, para utilizarlo en el draw_matrix
    def set_map(self,mapdata):
        self.__map__=mapdata
    
    #definimos el tamaño del mapa
    def set_map_size(self,mapsize):
        self.__map_size__=mapsize

    #dibujamos la matriz según el contenido de cada sector dentro de la matriz __map__
    def draw_matrix(self,paint):
        paint= QPainter()
        paint.begin(self)
        pen = QPen()
        pen.setColor(QColor("#000000"))
        paint.setPen(pen)
        dimensions = (self.__width__ -2) / self.__map_size__

        for x in range (self.__map_size__):
            x_pixel = dimensions * x
            for y in range (self.__map_size__):
                y_pixel = dimensions * y
                paint.drawRect(x_pixel,y_pixel,dimensions-1,dimensions-1)
                if self.__map__[x,y] == None:
                    paint.drawImage(QRect(x_pixel,y_pixel,self.__map_size__-1,self.__map_size__-1),self.grey)
                else:
                    if self.__map__[x,y].get_type() == "planta":
                        paint.drawImage(QRect(x_pixel,y_pixel,self.__map_size__-1,self.__map_size__-1),self.green)
                    elif self.__map__[x,y].get_type() == "animal":
                        paint.drawImage(QRect(x_pixel,y_pixel,self.__map_size__-1,self.__map_size__-1),self.black)
                    else:
                        paint.drawImage(QRect(x_pixel,y_pixel,self.__map_size__-1,self.__map_size__-1),self.grey)
                    
    #definimos una función para actualizar el mapa
    def reset(self,map_size=50):
        self.__map_size__ = map_size
        self.update()