import random

#clase entidades
class Entitys:
    name = ""
    __months_to_breed__ = 2
    __number_of_descendants__ = random.randint(1, 4)
    __last_reproducing__ = 0

    #constructor
    def __init__(self,entity_class,name,months_to_breed,number_of_descendants,last_reproducing = 0 ):
        self.name = name
        self.__months_to_breed__ = months_to_breed
        self.__number_of_descendants__ = number_of_descendants
        self.__last_reproducing__ = last_reproducing
        self.__entity_class__ = entity_class

    #getters
    def get_descendants(self):
        return self.__number_of_descendants__

    def get_name(self):
        return self.name

    def get_type(self):
        return self.__entity_class__

    def get_months_to_breed(self):
        return self.__months_to_breed__

    def get_last_reproducing(self):
        return self.__last_reproducing__
    
    def set_last_reproducing(self,actual_cycle):
        self.__last_reproducing__ = actual_cycle

    def can_reproduce(self,actual_cycle) -> bool:
        #noseporquechuchadaerroraveces
        if int(int(actual_cycle) - int(self.__last_reproducing__)) > int(self.__months_to_breed__):
            return True
        else:
            return False

class Vegetation(Entitys):
    pass

class Animal(Entitys):
    __months_to_starve__ = random.randint(1,3)
    __last_eated__ = 0
    __plant_type__ = ""
    steps_of_movement = 1

    #constructor
    def __init__(self,entity_class,name,months_to_breed,number_of_descendants,last_reproducing,steps_of_movement,last_eated,months_to_starve):
        super().__init__(entity_class,name,months_to_breed,number_of_descendants,last_reproducing)
        self.__months_to_starve__ = months_to_starve
        self.__last_eated__ = last_eated
        self.steps_of_movement = steps_of_movement

    #getters
    def movement(self):
        return self.steps_of_movement

    def eating_preference(self):
        return self.__plant_type__

    def alive(self,actual_cycle):
        if self.__last_eated__ != 0:
            if actual_cycle - self.__last_eated__ > self.__months_to_starve__:
                return True
            else:
                return False
        else:
            return True

    def eat(self,actual_cycle):
        self.__last_eated__ = actual_cycle

    def check_status(self):
        if self.__last_eated__ == 0:
            status = "Feliz"
        elif self.__last_eated__ == 1:
            status = "Hambriento"
        elif self.__last_eated__ == 2:
            status = "Desnutrido"
        elif self.__last_eated__ == 3:
            status = "A punto de morir"         
        txt = "Su estado actual es: " + status + " y le faltan " + str(self.__months_to_starve__) + " ciclos para morir de hambre."
        return txt