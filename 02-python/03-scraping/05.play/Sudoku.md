2.1 Number of Islands（岛屿的个数）(python)
采用深度优先遍历的方法构建一个沉没相邻岛屿的函数，在发现岛屿时递归调用沉没函数，则发现岛屿的次数即为岛屿的个数

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        re = 0
        if grid:
            height = len(grid)
            width = len(grid[0])
            def sink(i, j):
                nonlocal height,width
                if 0 <= i < height and 0 <= j < width and int(grid[i][j]):
                    grid[i][j] = '0'
                    for a, b in zip([i-1,i,i+1,i],[j,j-1,j,j+1]):
                        sink(a, b)
            
            for m in range(height):
                for n in range(width):
                    if int(grid[m][n]):
                        re += 1
                        sink(m, n)
        return re
```


2.2 Valid Sudoku（有效的数独）(python)
依次检查行，检查列，检查每个9方格
执行用时 : 64 ms, 在Valid Sudoku的Python3提交中击败了97.42% 的用户
内存消耗 : 13 MB, 在Valid Sudoku的Python3提交中击败了97.41% 的用户

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            lst = [value for value in row if value != '.']
            if len(set(lst)) != len(lst):
                return False
            
        for n in range(9):
            lst = [board[x][n] for x in range(9) if board[x][n] != '.']
            if len(set(lst)) != len(lst):
                return False
            
        for row in [0,3,6]:
            for col in [0,3,6]:
                lst = [board[row + i][col + j] for i in range(3) for j in range(3) if board[row + i][col + j] != '.']
                if len(set(lst)) != len(lst):
                    return False
        return True
```
