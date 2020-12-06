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
   
   - Original board use 1 and 2 to represent two different states, how to associate them with player colors
Steps:
   - Re-design and refactor functions
   - Using Spark and create appropriate targets and clones
   - Using Spark to make sure the each game will run until end
   - Collect the Spark results
   - Give the Monte Carlo result


Step 1: Re-design and refactor functions (HexRF)

Current Functions: HexEngine
   __init__(self)
   
   _encode_point(self, coordinate)
   _decode_point(self, point)
   _adj_nodes(self, point)
   _BFS(self)
   
   @staticmethod init_board(n)
   @staticmethod create_new(n, human_color_red, human_move_first, gui, ai)
   *@staticmethod create_exist(board, human_color_red, round, gui, ai)
   @staticmethod create_AI_only(n, AI_1_red, AI_1_first, gui, ai)
   
   *wining_check(self)
   available_moves(self)
   available_encoded_moves(self)
   move(self, point, useGui=True)
   next(self)
   update_gui(self)
   *clone(self, useGui = False, useAI = False)
   reset(self)
   run(self)
   
Refactor Description:
   - Basic unit is Hex class, but need to solve when there are tremendous copies
   - One problem is how to use BFS with those copies
   - Another problem is how to do steps with copies
   - Constructoring each one using an additional class is expensive
   
   - Player should be an independent class and HexEngine only cares board not player
   - Player is responsible for its AI algorithm
   - Color information is stored in player and HexEngine should not use color as flags
   - Monte Carlo should have an independent BFS algorithm which doesn't mess with the main one used by HexEngine
   - Player should use Monte Carlo and receive current state from HexEngine
   
Refactor Design:
   Player:
      __init__(self, color, ai = None)

      next(self, index, board)         # index presents the index of the player
           
      
      
   HexEngine:
      __init__(self, n, player1, player2, gui, player1First = True)
      
      _encodePoint(self, coordinate)
      _decodePoint(self, point)
      _adjNodes(self, point)
      _bfs(self)
      
      checkWin(self)
      availableMoves(self)
      *available_encoded_moves(self)
      move(self)
      update_gui(self)
      *clone(self, useGui = False, useAI = False)
      reset(self)
      run(self)


## Hex 1.0
Use multiple Machine Learning methods to achieve AI for the broad game HEX

Currenty supports
1. Monte Carlo
2. DDQN
   
   
   
   
   
   
   
   
   
   
   
   
   
