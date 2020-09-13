# forest-town

The objective of the game is to manage a 19th century west coast logging town, keeping it afloat as long as possible.



## Decisions
1. How many trees to log (ratios or numbers)
2. How many houses to build (ratios or numbers)
3. How many stores to build (ratios or numbers)
4. How many roads (railroads)
5. How many supplies to procure

## Environment
A XxX grid of characters that represent objects in game. The most important is the tree character (T/t).

* T/t - Tree
* _ - fallen tree

* h H - Housing
* C - commercial
* W - water
* M - mountain

### Trees have 4 states:
1. Sapling - t
2. Mature tree - T
3. Fallen - /
4. Logged - #
5. " " - empty ground

1 basic time unit = 1 turn

### Natural growth ideas:
t -> T,/
T -> /,#
\# -> " "
" " -> t

t -> T - (Turns since planting * .20) + R(0-1) > 1
T -> /

# Conventions
* _Row-first for multidimensional lists!_ - for Jon
