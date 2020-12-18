import numpy as np
import random,os,Entitys

class Environment:
    __map_size__ = 50
    __map__ = np.full([__map_size__,__map_size__], None, dtype=None, order='C')
    __actual_cycle__ = 0
    __alive_animals_count__ = 0
    __alive_plants_count__ = 0
    __initial_entitys__ = 25
    __entity_list__ = []
    __counter__ = 0
    
    #constructor
    def __init__(self,initial_entitys,map_size):
        self.__initial_entitys__ = initial_entitys
        self.__map_size__ = map_size
        if initial_entitys > (map_size*map_size):
            raise Exception("No pueden haber mas entidades que espacios en el mapa")
        else:
            print("Juego iniciado, creando entidades.")
            self.create_entitys()

    #generador de ciclos
    def new_cycle(self):
        self.__actual_cycle__ += 1
        for x in range(self.__map_size__):
            for y in range(self.__map_size__):
                if self.__map__[x,y] != None:
                    self.cycle_per_entity(self.__map__[x,y])
        print("Ronda ",self.__actual_cycle__," ejecutada.")

    def print_environment(self):
        for i in range(self.__map_size__):
            for n in range(self.__map_size__):
                if self.__map__[i,n] != None:
                    if self.__map__[i,n].get_type() != "planta":
                        print("Eje X: ",i," Eje Y: ",n," Valor actual: ",self.__map__[i,n].get_name(),self.__map__[i,n].check_status())
                    else:
                        print("Eje X: ",i," Eje Y: ",n," Valor actual: ",self.__map__[i,n].get_name())
                else:
                    print("Eje X: ",i," Eje Y: ",n,". Este espacio se encuentra vacío.")

    def reset(self,initial_entitys = 25,map_size = 50):
        print("Reiniciando todo... Espere unos segundos")
        if type(map_size) != int:
            raise Exception("Por favor ingresa un integro.")
        elif map_size < 2:
            raise Exception("El mapa más pequeño permitido es de 2x2.")
        elif initial_entitys < 2:
            raise Exception("El menor numero de entidades a crear es 2.")
        else:
            self.__initial_entitys__ = initial_entitys
            self.__map_size__ = map_size
            self.__actual_cycle__ = 0
            self.__alive_animals_count__ = 0
            self.__alive_plants_count__ = 0
            self.__entity_list__ = []
            self.__counter__ = 0
            self.__map__ = np.full([map_size,map_size], None, dtype=None, order='C')
            print("Juego reiniciado, creando entidades.")
            self.create_entitys()
            
    def get_map(self):
        return self.__map__
    
    def get_map_size(self):
        return self.__map_size__

    def cycle_per_entity(self,entity):
        for i in range(self.__map_size__):
            for n in range(self.__map_size__):
                if entity.get_type() == "animal":
                    steps = entity.movement()
                    self.find_food(steps,entity,i,n)
                    self.try_to_descend(entity)
                elif entity.get_type() == "planta":
                    self.try_to_descend(entity)

    def find_food(self,steps,animal,x,y):
        temp = True
        while temp:
            for i in range(x-steps,x+steps):
                for n in range(y-steps,y+steps):
                    if i >= 0 and i <= (self.__map_size__-1):
                        if n >= 0 and n <= (self.__map_size__-1):
                            if self.__map__[i,n] != None:
                                if animal.get_type() == "planta":
                                    self.__map__[i,n] = None
                                    self.__map__[i,n] = animal
                                    self.__map__[x,y] = None
                                    animal.eat(self.__actual_cycle__)
                                    self.__counter__ -= 1
                                    temp = False
            if animal.alive(self.__actual_cycle__) == False:
                self.__map__[x,y] = None
                self.__counter__ -= 1
                print("El animal en Eje X: ",x," Eje Y: ",y,". Acaba de morir.")
            temp = False

    def try_to_descend(self,entity):
        if entity.can_reproduce(self.__actual_cycle__)==True:
            quantity = entity.__number_of_descendants__
            self.create_descendants(entity,quantity)

    def create_entitys(self):
        #creamos pandas
        temp = int(self.__initial_entitys__/2)
        for n in range(temp):
            randdes = random.randint(1,4)
            entity = Entitys.Animal("animal","panda",4,randdes,0,5,0,3)
            self.__entity_list__.append(entity)
            self.__alive_animals_count__ = self.__alive_animals_count__+1
            self.allocate_entity(entity)
        #creamos bambu
        for n in range(temp):
            randdes = random.randint(1,6)
            entity = Entitys.Vegetation("planta","bambu",2,randdes)
            self.__entity_list__.append(entity)
            self.__alive_plants_count__ = self.__alive_plants_count__+1
            self.allocate_entity(entity)
        print("La creacion de entidades ha terminado")
        
    def create_entitys_command(self,quantity,entity_type):
        if entity_type == "panda":
            #creamos pandas
            for n in range(quantity):
                randdes = random.randint(1,4)
                entity = Entitys.Animal("animal","panda",4,randdes,0,5,0,3)
                self.__entity_list__.append(entity)
                self.__alive_animals_count__ = self.__alive_animals_count__+1
                self.allocate_entity(entity)
        else:
            #creamos bambu
            for n in range(quantity):
                randdes = random.randint(1,6)
                entity = Entitys.Vegetation("planta","bambu",2,randdes)
                self.__entity_list__.append(entity)
                self.__alive_plants_count__ = self.__alive_plants_count__+1
                self.allocate_entity(entity)
        print("La creacion de entidades ha terminado")

    def allocate_entity(self,entity):
        temp = True
        while temp:
            randx = random.randint(0,self.__map_size__-1)
            randy = random.randint(0,self.__map_size__-1)
            if self.__map__[randx,randy] == None:
                self.__map__[randx,randy] = entity
                self.__counter__ += 1
                temp = False
            if self.__counter__ == (self.__map_size__*self.__map_size__):
                print("Fallo al colocar la entidad, matriz llena.")
                print("Esta cría se considerará muerta.")
                

    def create_descendants(self,entity,quantity):
        if entity.get_type() == "animal":
            for n in range(quantity):
                entity.set_last_reproducing(self.__actual_cycle__)
                randdes = random.randint(1,4)
                entity = Entitys.Animal("animal","panda",4,randdes,0,5,0,3)
                self.__entity_list__.append(entity)
                self.__alive_animals_count__ = self.__alive_animals_count__+1
                self.allocate_entity(entity)
            print("El panda ha tenido ",quantity," crias.")
        elif entity.get_type() == "planta":
            for n in range(quantity):
                entity.set_last_reproducing(self.__actual_cycle__)
                randdes = random.randint(1,6)
                entity = Entitys.Vegetation("planta","bambu",2,randdes)
                self.__entity_list__.append(entity)
                self.__alive_plants_count__ = self.__alive_plants_count__+1
                self.allocate_entity(entity)
            print("La planta ha dejado ",quantity," brotes de bambú")


