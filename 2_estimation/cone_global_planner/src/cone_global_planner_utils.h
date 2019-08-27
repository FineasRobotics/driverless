#include <vector>
using namespace std;

void rotate_array(vector<vector<long double> > &ar, int turn=1);
void col_means(const vector<vector<long double> > &ar, vector<long double> &means);
void col_stddevs(const vector<vector<long double> > &ar, const vector<long double> &means, vector<long double> &stddevs);
void reject_outliers(vector<vector<long double> > &ar, long double m=2.3);
vector<long double> linspace(long double start, long double endd, int num);
void col_min_max(const vector<vector<long double> > &ar, int col, long double &col_max, long double &col_min);
vector<vector<long double>> middleLine(vector<vector<long double> > &a1, vector<vector<long double> > &a2, int poly_deg=6, int n_points=100, bool rotated=false);
void print_vector(const vector<vector<long double> > vec);
void print_vector_small(const vector<long double> vec);
