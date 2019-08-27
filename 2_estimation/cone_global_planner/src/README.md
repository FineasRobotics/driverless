## vector<vector<long double>> middleLine(vector<vector<long double> > &a1, vector<vector<long double> > &a2, int poly_deg=6, int n_points=100, bool rotated=false)
First it creates 2 new vectors(lines) that estimate the old vectors and are the same length(length = n_points).
Then it calculates the average between each x and each y of the new arrays, returning a new middle line.
If it can't calculate the middle line, the 2 vectors are rotated and the operation starts over.

Source: https://stackoverflow.com/questions/49037902/how-to-interpolate-a-line-between-two-other-lines-in-python

## void rotate_array(vector<vector<long double> > &ar, int turn=1)
Edits the original vector.
It rotates the points of the vector by 90/-90 degrees,
depending on the turn argument(1 for 90 degrees, -1 for -90 degrees)

## void reject_outliers(vector<vector<long double> > &ar, long double m=2.3)
Edits the original vector. Removes points that are way off the lines, to calculate a better path.

Source: https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list

## void col_min_max(const vector<vector<long double> > &ar, int col, long double &col_max, long double &col_min)
Calculates the minimum and maximum, given a vector and the desired column.

## void col_means(const vector<vector<long double> > &ar, vector<long double> &means)
Calculates the mean for x and y column.
Populates a means vector.

## void col_stddevs(const vector<vector<long double> > &ar, const vector<long double> &means, vector<long double> &stddevs)
Calculates the standard deviation for x and y column.
Populates a stddevs vector.

## vector<long double> linspace(long double start, long double endd, int num);
Check numpy.linspace documentation.

Source: https://stackoverflow.com/questions/27028226/python-linspace-in-c

## print_vector_small, print_vector
Prints a 1d(small) vector and a 2d vector respectively.
