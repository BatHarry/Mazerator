# Mazerator
Mazerator is my university project for the second year python class. 
Mazerator is a maze game built on top of pygame. 
In order to generate tge maze a recuraive backlog algorithm is used. 

## Maze package
The maze package contains the building blocks of the maze.
Starting with the Cell class it is basically a datastructure that contains all the required variable for single cell in the maze. 
It is given a a x and y coordinates to to start with. The given x and y coordinates represent the the top left position of the cell and are later used to calculate the other three points of the cell

The maze class is where the maze itself is generated. 
Starting with filling in a two dimensional array of Cell objects which later will be modified.
In order to create a playable maze, the Maze class uses a backlog to go through all the cells and go back if it gets stuck. 
Starting from the first cell the algorithm picks a random adjecent neighbour for its next move and by doing that removes the walls between the current and next cells.
