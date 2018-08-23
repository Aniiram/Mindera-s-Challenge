# Adjacent cCells Challenge
Graduate Challenge by Mindera's. 

##### Rules:
*  Cells are considered adjacent if they both contain a 1 (one) and are next to each other horizontally or vertically (not diagonally).
*  Groups containing a single cell should not be considered
*  The order of points or groups outputted by the program is not relevant

##### Example
For a grid input of:
```
[[0,0,0,1,0,0,1,1],
 [0,0,1,1,1,0,1,1],
 [0,0,0,0,0,0,1,0],
 [0,0,0,1,0,0,1,1],
 [0,0,0,1,0,0,1,1]]
```

Expected output:
```
[ [0,3], [1,2], [1,3], [1,4] ]
[ [0,6], [0,7], [1,6], [1,7], [2,6], [3,6], [3,7], [4,6], [4,7] ]
[ [3, 3], [4,3] ]
```

##### Tecnhonogies used: 
*  Python3

