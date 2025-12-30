Intuition

A 3×3 magic square has very strict properties: it must contain the numbers 1 through 9 exactly once, every row, column, and diagonal must sum to the same value, and the center must always be 5.
Because a magic square must be a contiguous 3×3 block, the problem reduces to checking each possible 3×3 subgrid inside the given grid and counting how many satisfy these fixed rules.

Approach

We slide a 3×3 window across the grid by choosing each possible top-left corner where a 3×3 subgrid can fit.
For every such subgrid, we first apply fast eliminations (such as checking whether the center is 5 and whether all values are distinct and between 1 and 9).
If those checks pass, we then verify that all three rows, all three columns, and both diagonals sum to 15.
Each subgrid that satisfies all conditions is counted as a magic square.

Time complexity
O(m×n)

Space complexity
O(1)
