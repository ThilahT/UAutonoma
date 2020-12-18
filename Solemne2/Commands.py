import os,time
from Environment import Environment

class Game():
    actual_cycle = 0
    actual_environment = None
    
    def __init__(self,actual_cycle=0):
        self.actual_cycle = 0
        self.actual_environment=Environment(25,50)
    
    def newcycles(self):
        self.actual_environment.new_cycle()
        self.actual_cycle = self.actual_cycle + 1
        print("ciclo ",self.actual_cycle)
        
    def print_environment(self):
        self.actual_environment.print_environment()
    
    def new_entitys(self,quantity,entity_type):
        self.actual_environment.create_entitys_command(quantity,entity_type)
    
    def get_map(self):
        return self.actual_environment.get_map()
    
    def get_map_size(self):
        return self.actual_environment.get_map_size()

    def reset(self,map_size,animals):
        print("Reiniciando ciclos... Espere unos segundos")
        if animals <= map_size*map_size:
            print("Reinicio de fauna y flora, LISTO")
            self.actual_environment.reset(animals,map_size)
            self.actual_cycle = 0
        else:
            print("Ha ocurrido un error, intentelo de nuevo.")
            #ERROR
            pass