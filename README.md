# Hex
## Hex 1.0
Use multiple Machine Learning methods to achieve AI for the broad game HEX

Currenty supports
1. Monte Carlo
2. DDQN


# Hex 1.5
Add Spark to sparallelize the calculation of Monte Carlo.

1. Spark Monte Carlo: SparkMC
Description
   - Use Spark to load the current state
   - Use Spark to clone enough copies
   - Assign each copy an independent _step_ to focus on
   - Use engine functions to run the rest steps based on the current _step_
   - Run win check on each independent sample
Problems:
   - State is tightly associated with Hex class
   - If change all functions that specifically for an object, then too many functions will be static
Steps:
   - Refactor all functions which are dealing with states
   - Using Spark and create appropriate targets and clones
   - Using Spark to make sure the each game will run until end
   - Collect the Spark results
   - Give the Monte Carlo result

