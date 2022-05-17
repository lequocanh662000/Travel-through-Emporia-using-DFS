# Travel-through-Emporia-using-DFS

Input format
  * The first line will contain m and n, the # of rows and columns, respectively.
  * Following that will be m lines and there are n digits for each line, separated by spaces.
  * Each digit on each line could be 0, 1, 2, 3
    - 2 indicates the place Bastian will start his journey.
    - 3 indicates the place Bastian will finish his journey in Emporia.
    - 0 indicates an empty place that Bastian can move to.
    - 1 indicates an obstacle that Bastian can not move to.
  * The input data will be provided from stdin.
  
  Output
  * A single number, the # of the ways Bastian can travel from the start to the destination, not missing any empty places in Emporia.

Example
Sample Input:

 4 4  
 3 1 1 2    
 0 0 0 0   
 0 0 0 0    
 0 0 0 0   

Sample Output:

4

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Explanation:

In this case, the Emporia map is a matrix of 4 by 4 and there are 2 obstacles at (0, 1) and (0,2). The start place and destination place are at (0,3) and (0,0). After the calculation, Bastian found 4 different ways to traverse from 2 to 3.
