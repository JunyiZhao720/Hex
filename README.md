# Hex

## Hex 1.5
Add Spark to sparallelize the calculation of Monte Carlo.

Spark Monte Carlo
Description
   - Use Spark to load the current state
   - Use Spark to clone enough copies
   - Assign each copy an independent _step_ to focus on
   - Use engine functions to run the rest steps based on the current _step_
   - Run win check on each independent sample
Problems:
   - State is tightly associated with Hex class
   - If change all functions specifically for an object, then too many functions will be static
   - Too many contructors
   
   - Original state use 1 and 2 to represent two different states, how to associate them with player colors
   - HexGui needs to be changed to associate with player as well
Steps:
   - Re-design and refactor functions
   - Using Spark and create appropriate targets and clones
   - Using Spark to make sure the each game will run until end
   - Collect the Spark results
   - Give the Monte Carlo result


Step 1: Re-design and refactor functions (HexRF)
   
Refactor Description:
   - Basic unit is Hex class, but need to solve when there are tremendous copies
   - One problem is how to use BFS with those copies
   - Another problem is how to do steps with copies
   - Constructoring each one using an additional class is expensive
   
   - Player should be an independent class and HexEngine only cares state not player
   - Player is responsible for its AI algorithm
   - Color information is stored in player and HexEngine should not use color as flags
   - Monte Carlo should have an independent BFS algorithm which doesn't mess with the main one used by HexEngine
   - Player should use Monte Carlo and receive current state from HexEngine
   

Step 2: Spark re-implementation
   - Using Spark and create appropriate targets and clones
   - Using Spark to make sure that each game will run until end
   - Collect the Spark results
   - Give the Monte Carlo result

## Hex 1.0
Use multiple Machine Learning methods to achieve AI for the broad game HEX

Currenty supports
1. Monte Carlo
2. DDQN
   
   
   
   
   
   
   
   
   
   
   
   
   
