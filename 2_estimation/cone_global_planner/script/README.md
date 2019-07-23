## middle_line_finder.py
Contains the middleLine function. It takes 2 arrays and returns an array.
First it creates 2 new arrays that estimate the old arrays and are the same length.
Then it calculates the average between each x and each y of the new arrays.

In main there are many different examples.
You can run it as it is, or uncomment the example you want to run.

## point_sorter.py
Contains the opt order function. It takes an array and returns an array.
It is sorting points to form a continuous line.
First it creates a nearest neighbour graph to connect each of the nodes to its 2 nearest neighbors.
Then, it find the shortest path from starting node(if not given, the 0 node will be selected)
After that, it find the path with smallest cost from all sources.
Returns the sorted array

In main there is 1 example using a sin function that get shuffled and then gets
sorted by opt_order function.

## point_rotator.py
Contains the rotate_array function. It takes an array and returns an array.
It rotates the points of the array by 90/-90 degrees depending on the turn argument(1 for 90, -1 for -90)

## outlier_remover.py
Contains the reject_outliers function. It takes an array and returns an array.
It returns the array without the outlier points.

## global_planner.py
Example that uses these functions.
