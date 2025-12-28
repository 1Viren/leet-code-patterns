Intuition

Initially, a brute-force approach using two nested loops can be used to count all negative numbers in the grid. However, this results in a time complexity of O(m × n), which is not optimal.
Since the grid is sorted in non-increasing order both row-wise and column-wise, once we encounter a negative number, all elements to the right in the same row are also negative. To take advantage of this property, we start from the bottom-left corner of the matrix. This position allows us to eliminate either an entire row or an entire column with each step.

Approach

We initialize our position at the bottom-left cell of the grid. While staying within bounds:
If the current value is negative, then all elements to the right in that row are also negative. We add the number of remaining columns to the count and move up one row.
If the current value is non-negative, then any negative values must lie further to the right, so we move right by one column.
This strategy ensures that at each step we eliminate either a row or a column from further consideration.

Complexity

Time Complexity: O(m + n)
Each row and column is visited at most once.

Space Complexity: O(1)
Only a constant amount of extra space is used.
