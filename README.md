The algorithm uses principles inspired by cellular automata to replicate the growth of slime mold.

Platform : Python
Packages : Pygame

Slime mold are interesting organisms which spread and grow to connect foods, and optimise its branches to find optimal path.
This is achieved mainly through first spreading and making the most rewarding connections stronger. Then pulsations go through the body of the slime, which further optimises the path through an intresting process, wich is visualised using the code.

The growth of the organism is simulated by using a cellular automata, with each cell having a certain slime value. They interactions with neighbours are fine tuned, by adjusting various constants affecting thier behaviour. Also a spurt of background randomness is provided to mimic nature.

Initially the slime mold grows towards nearby foods with a little bit of randomness. The growth defined by iterations of the cellular automata process are fine tuned, so that the slime does not die out, neither grows too much, a narrrow criticallity is maintained. Then after all points the connected, the slime optimises through series of contraction and relaxation pulsed, which are encoded by slight adjustments to the rules of the cellular automata.

All these processes are acheived by the usage of a 2d array of cells, each cell object has its own properties like slimeicity, randomness, neighbouring cells, etc.
