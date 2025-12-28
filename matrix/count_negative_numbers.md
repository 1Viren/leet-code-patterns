Intuition
Since the grid is sorted in non-increasing order both row-wise and column-wise, when we encounter a negative number, all elements to the right in that row are also negative. To efficiently count them without checking every cell, we start from the bottom-left corner, which allows us to eliminate either a full row or a full column at each step.

Approach
We initialize our position at the bottom-left cell of the grid. While we stay within bounds:
If the current value is negative, then all elements to the right in that row are also negative, so we add (number of remaining columns) to our count and move up one row.
If the current value is non-negative, then negatives (if any) must be further to the right, so we move right one column.
This way, each step eliminates a row or a column.

Complexity
Time complexity:
O(m + n)
Space complexity:
O(1)
