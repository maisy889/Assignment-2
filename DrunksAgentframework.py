import random

''' Creating the Agent class, aka the Drunks '''

class Drunks():
    
    def __init__(self, environment, drunks, home_num, routes):
        
        # Feeding the environment into the agents
        self.environment = environment  
        
        # Setting the environment width and height
        self.width = len(environment)
        self.height = len(environment[0])   
        
        # Feeding in the list of agents
        self.drunks = drunks            
        
        # These are coordinates taken from within the 'Pub'
        self.y = 139                    
        self.x = 148                    
        
        # This is linking each of the drunks to a home, numbers are between 10 to 250 (25 total)
        self.home_num = home_num  
        
        # This links to the walked routes that each drunk generates
        self.routes = routes        
        
        # The condition that all drunks are at home starts is False
        self.athome = False             
        
        
    # Defines how the drunks move in a random direction within the environment #
                
    def move(self):
        
        # Move a random number of steps between 5 to 10 #
        dx = random.randint(5,10)
        dy = random.randint(5,10)
        
        # Defines the movement along the y axis #
        if random.random() < 0.5:
            self.y = (self.y + dy) % self.height
        else:
            self.y = (self.y - dy) % self.height
            
        if random.random() < 0.5:
            self.x = (self.x + dx) % self.width  
        else:
            self.x = (self.x - dx) % self.width 
        
        
    # Gives string with x and y values #
            
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)