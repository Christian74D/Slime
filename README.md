# Slime Mold Based Pathfinder
#### Video Demo:  https://www.youtube.com/watch?v=RLA8HYphK2k
#### Description:
The algorithm uses principles inspired by cellular automata to replicate the growth of slime mold.

Platform : Python
Packages : Pygame

Slime mold are interesting organisms which spread and grow to connect foods, and optimise its branches to find optimal path.
This is achieved mainly through first spreading and making the most rewarding connections stronger. Then pulsations go through the body of the slime, which further optimises the path through an intresting process, wich is visualised using the code.

The growth of the organism is simulated by using a cellular automata, with each cell having a certain slime value. They interactions with neighbours are fine tuned, by adjusting various constants affecting thier behaviour. Also a spurt of background randomness is provided to mimic nature.

Initially the slime mold grows towards nearby foods with a little bit of randomness. The growth defined by iterations of the cellular automata process are fine tuned, so that the slime does not die out, neither grows too much, a narrrow criticallity is maintained. Then after all points the connected, the slime optimises through series of contraction and relaxation pulsed, which are encoded by slight adjustments to the rules of the cellular automata.

All these processes are acheived by the usage of a 2d array of cells, each cell object has its own properties like slimeicity, randomness, neighbouring cells, etc.

the display framework is made using pygame, and the cells are rendered at thier respective positions every cyle after thier properties have changed.


STRUCTURE OF THE PROJECT

The entire project is a multifile program, run by the main.py file

constants.py has constants like screen size and colour settings, and other specific constants that can control or modify the behaviour of the slime mold.

functions.py has various helper functions, functions to find the direction of food, to check if slime is connecting all points, etc.

square.py defines the cell object and its properties

grid.py initialises a cell for every row and column of the grid required and returns a grid object.

main.py has a event loop, which takes cares of going through every iteration of growth

simulate.py encodes the different behaviours for different stages of growth of the slime mold, which are set to be manually activated by default


INSTRUCTIONS FOR RUNNING THE CODE :
1. Install Python and necessary packages (Refer https://www.youtube.com/watch?v=kSdUHtUb_tw)
2. Run main.py using open with Python.exe
3. Select food points by using the mouse, use left mouse button to deselect a point
4. Click Enter to initialize the grid
5. Click Enter to start the slime growth
6. If food is far away and the slime cant dedect it, click between the food and already existing slime to guide it
7. Repeat step 6 until all points are connected(Do not skip this step as the next algorithm is dependent on the fact that all points are connected)
8. Click Enter to start the optimisation phase
9. Click s in keyboard to stop the simulation, when you are satisfied that the path is optimised
10. Use Backspace to go back a step, and Enter to move front. Always use backspace and ensure you are in the initial stage then close the application, failure to do so might interfere with the iterations and may lead to system overloading
