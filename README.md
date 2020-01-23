# Programming for Geographical Information Analysts: Core Skills - Assignment 2: Town Planning for Drunks

Student ID: 201273936

This is the second assessment for the module GEOG5990 as part of the MSc Geographic Information Systems course at the University of Leeds. 
More information about this can be found at: https://github.com/maisy889/Assignment-2 

## Overview
The agent-based model has been created in Spyder (Anaconda 3) on Windows using Python coding language 3.7.

The aim of the assignment was to create an agent-based model that shows an animation of drunks trying to find their way home from the pub and saves the different routes they walk as a text file.

The overall structure and code used within this project was adapted from the first assignment in this module, which can found here.  

## Files

The files needed to run the model are as follows:
•	TownPlanning.py: The operational model 
•	DrunksAgentframework.py: The agent framework defining the Drunk class and its functions
•	TownLayout.txt: A raster file (300x300) which represents the town environment that the drunks move in. Houses are defined by the numbers 10 – 250, the pub is defined by 1’s and the rest of the empty space is 0. 

All files are available to download on Github [here] (https://github.com/maisy889/Assignment-2)

This project is licensed under the GNU General Public License v.3.0 - see [here] (https://github.com/maisy889/Assignment-2/blob/master/LICENSE)

## Setup

The environment was created by inputting text file which contains values in a grid format. The value of each pixel defines a feature within the environment: 0 = empty space; 1 = Pub; 10-250 = Houses. By using MatPlotLib these values can be visualised as a graphic.

The agents (aka ‘Drunks’) have been designed to move within the environment from the pub to their homes. When run, the model completes the following:

•	Builds an environment from a text file and draws it 
•	Create the agents, aka ‘drunks’
•	Gives each drunk a number that corresponds to one of the houses on the map
•	Models the drunks leaving the pub and walking to their homes
•	Each point on the map that a drunk walks through is increased by 1 and saved 
•	By clicking a button once the animation is complete the cumulative values of the drunks routes is saved as a txt file

There are 25 drunk agents which are assigned a number when they are generated between 10-250, which matches one for each of the houses within the environment. The drunks will then move in a random direction until they get to their house. Every pixel that a drunk walks over has a value of 1 added to it in a separate ‘routes’ list.
A condition has been set that once all the drunks are home or once the animation has run 1000 times (whichever happens first) the animation will stop. At this point the routes taken by the drunks can be exported to a text file. 

The MatPlotLib animation function is used to create a moving animation of the graph.
The General User Interface (GUI) was created using tkinter. 

## Operation guide

It is recommended that you run this model in Spyder (Anaconda 3) and the following instructions are for this software. 

Firstly, download the above files from the GitHub repository (above). Ensure that all files are stored within the same folder.
 
Open both the DrunksAgentframework.py and TownPlanning.py within Python. To ensure that the animation runs correctly, you need to set the Graphics option to Tkinter. You can do this by selecting: Tools > Preferences > IPython Console > Graphics, and then from the drop-down select Tkinter.

Run the DrunksAgentframework file first, and once this has completed run the model file within Spyder. This will pop out a tkinter GUI window called ‘Town Planning Model’ (an additional window called ‘Figure 1’ will also appear, it will not be used). There is a button ‘Run Model’ at the bottom of the screen which will start the model. If you wish to end the animation early, click the ‘Close Model’ button.

Once the animation completes, click the button ‘Export Routes’. This will export a txt file to the same folder that holds the model files and will show the number of steps the drunks took on each pixel. 

## Known issues and suggested improvements

Initially when the drunks were first animated, they all moved the same distance at the same time. This caused the model to look quite uniform, which didn’t reflect the nature of ‘drunks’. To change this, I decided to randomise how many steps they take each turn from 5 to 10, which created a more erratic pattern of movement. However, because the drunks had no point of focus for their movement, it would take a very long time for them to reach home and the animation would usually come to a stop due to the number of iterations being met before all the drunks reached home.

Different approaches could be taken to improve this:
•	Creating a way that drunks can be aware of the general direction of their home 
•	Making it so that the drunks cannot retrace their own steps

Another issue is that the drunks can sometimes come to a stop outside of the boundary of the house. When testing, the console would print the house number and declare that the drunk had reached their home, despite them standing up to 20 pixels away from it. I am not entirely sure what is causing this issue and it would require further troubleshooting. 

An additional improvement would to have the routes.txt file display at the end of the animation to visually show the routes that the drunks took.

