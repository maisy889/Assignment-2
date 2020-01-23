''' Importing all functions and libraries '''

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import matplotlib.pyplot
import matplotlib.animation 
import csv
import tkinter
import DrunksAgentframework


''' Defining number of drunks'''

# Creates a container to hold a list #
drunks = []
# Sets the number of drunks #
num_of_drunks = 25


''' Creating the environment '''
''' The following imports a txt file which contains values in a grid format. This creates the environment '''
''' Each value defines a pixel within the environment; 0 = empty space, 1 = Pub, 10-250 = Houses '''

# Creates a container to hold the data for the environment #
environment = []

# Opens the txt file containing values that will be used to build the environment #
with open('TownLayout.txt', newline='') as f:                   
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = [] 
        for value in row:
            rowlist.append(value)   
        environment.append(rowlist)
# Closes the reader #
f.close()


''' Test environment is correctly outputting'''
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.colorbar()
    
''' Setting the area '''
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0,0,1,1])


''' Output map of paths walked saved as "routes"'''
# Creates another container to hold the data for the steps taken by the drunks #
routes = []

# This sets up a second environment where the number of steps the drunks take #
# through the environment can be recorded #
width = len(environment)
height = len(environment[0])

for i in range(height):
    rowlist = []
    for j in range(width):
        rowlist.append(0)
    routes.append(rowlist)     
            
    
'''Initialise Drunks. This gives each drunk a number as they leave the pub. 
To make these correspond with the house numbers, they are multiplied by 10''' 
   
for j in range(num_of_drunks):
    home_num = (j+1)*10
    drunks.append(DrunksAgentframework.Drunks(environment, drunks, home_num, routes))
    print(home_num)

carry_on = True


'''Updates the animation display showing the drunks moving within the environment'''
def update (frame_number):
    
    # Clears the display # 
    fig.clear()
    global carry_on
    
    # Creates the visual plot #
    matplotlib.pyplot.xlim(0, len(environment))
    matplotlib.pyplot.ylim(0, len(environment[0]))
    matplotlib.pyplot.imshow(environment)
    
    # Plots the drunks within the environment #
    for i in range(num_of_drunks):
        matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)
       
    # Keeps a count of how many drunks have made it home #    
    drunks_athome = 0   
        
    for i in range(num_of_drunks):
        # If the drunks assigned home number equals the environment values then #
        # drunk is counted as making it home #
        if drunks[i].home_num == drunks[i].environment[drunks[i].x][drunks[i].y]:
            drunks[i].athome == True
            # Count how many drunks have made it home #
            drunks_athome = drunks_athome + 1      
            #print(drunks[i].home_num, "I made it home")
        else:
            drunks[i].athome == False
            drunks[i].move()
            # This adds one to the environment recording the drunks routes #
            routes[drunks[i].x][drunks[i].y] += 1
        
    # If all the drunks make it home, stop
    if drunks_athome == num_of_drunks:         
        carry_on = False
        print("All drunks are home")


    
'''General function'''    
def gen_function(b = [0]):
    a = 0
    global carry_on                
    while (a < 1000) & (carry_on) :
        yield a			            
        a = a + 1


'''Sets the 'run' fuction for the animation'''
def run():
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

'''Builds the main GUI window with tkinter'''
root = tkinter.Tk()
root.wm_title("Town Planning Model")

## Creating a menu in GUI ##
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)

#Close the model#    
def close():
    root.destroy()
    
'''Exporting the route that has been walked'''
def write():
    f2= open('routes.txt', 'w', newline='') 
    writer = csv.writer (f2, delimiter = ',')
    for row in routes:
        writer.writerow(row)
    f2.close()
    
#Create a button to close the model
btn = tkinter.Button(root, text = 'Close Model', bd = '5', 
                          command = close)  
# Set the position of button on the bottom of the window
btn.pack(side = 'bottom')

#Create a button to close the model
btn = tkinter.Button(root, text = 'Export Routes', bd = '5', 
                          command = write)  
# Set the position of button on the bottom of the window
btn.pack(side = 'bottom')

# Create a button to run the model #
btn = tkinter.Button(root, text = 'Run Model', bd = '5', 
                          command = run)  
# Set the position of button on the bottom of the window #
btn.pack(side = 'bottom')

canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
