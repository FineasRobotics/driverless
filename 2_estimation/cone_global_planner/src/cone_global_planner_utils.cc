#include <iostream>
#include <vector>
#include <cmath>
#include "cone_global_planner_utils.h"
#include "PolyfitBoost.hpp"
using namespace std;

void print_vector(const vector<vector<long double> > vec){
    cout.precision(15);
    for (unsigned int i = 0; i < vec.size(); i++) 
        printf("%15Lf %15Lf\n", vec[i][0], vec[i][1]);
    cout << endl;  
}

void print_vector_small(const vector<long double> vec){
    cout.precision(15);
    for (unsigned int i = 0; i < vec.size(); i++)
        cout << vec[i] << " ";
    cout << endl;
}

void rotate_array(vector<vector<long double> > &ar, int turn){

    for(unsigned int i=0; i < ar.size(); i++){
        long double tmp = ar[i][0] * -1;
        ar[i][0] = turn * ar[i][1];
        ar[i][1] = turn * tmp;
    }
}

void reject_outliers(vector<vector<long double> > &ar, long double m){
    vector<long double> means;
    vector<long double> stddevs;
    col_means(ar, means);
    col_stddevs(ar, means, stddevs);
    auto outliers_func = [means, stddevs, m](long double num, int coord) -> bool{
        return abs(num - means[coord]) < m * stddevs[coord];
    };

    for (unsigned int i = 0; i < ar.size(); i++) {
        if(!outliers_func(ar[i][0], 0) || !outliers_func(ar[i][1], 1)){
            ar.erase(ar.begin() + i);
        }
    }

}

vector<vector<long double>> middleLine(vector<vector<long double> > &a1, vector<vector<long double> > &a2, int poly_deg, int n_points, bool rotated){
    long double min_a1_x, max_a1_x, min_a2_x, max_a2_x;
    col_min_max(a1, 0, min_a1_x, max_a1_x);
    col_min_max(a2, 0, min_a2_x, max_a2_x);
    
    vector<long double> new_a1_x = linspace(min_a1_x, max_a1_x, n_points);
    vector<long double> new_a2_x = linspace(min_a2_x, max_a2_x, n_points);
    //cout << "a1_linspaced" << endl;
    //print_vector_small(new_a1_x);
        
    try{
        vector<long double> a1_coeffs = polyfit_boost(a1, poly_deg);
        vector<long double> a2_coeffs = polyfit_boost(a2, poly_deg);
        //cout << "a1_coefs" << endl;
        //print_vector_small(a1_coeffs);
        
        vector<long double> new_a1_y = polyval(a1_coeffs, new_a1_x);
        vector<long double> new_a2_y = polyval(a2_coeffs, new_a2_x);
        //cout << "a1_polyvaled" << endl;
        //print_vector_small(new_a1_y);
    
        //vector<vector<long double>> vec(m, vector<int> (n, 0)); for a m*n vector
        vector<vector<long double>> mid_line(n_points, vector<long double> (2, 0.0)); 
        for(int i=0; i < n_points; i++){
            mid_line[i][0] = (new_a1_x[i] + new_a2_x[i])/(long double)2;
            mid_line[i][1] = (new_a1_y[i] + new_a2_y[i])/(long double)2;
        }      
    
        if(rotated)
            rotate_array(mid_line, -1);
        
        return mid_line;
        
    }catch(const char* error_msg){
        rotate_array(a1);
        rotate_array(a2);
        
        return middleLine(a1, a2, poly_deg, n_points, true);
    }
    
}

void col_means(const vector<vector<long double> > &ar, vector<long double> &means) {
    int cols = ar[0].size();
    int rows = ar.size();

    for (int i = 0; i < cols; i++) {
        int sum = 0;

        for (int j = 0; j < rows; j++)
            sum += ar[j][i];
        means.push_back( sum/(long double)rows );
    }

}

void col_stddevs(const vector<vector<long double> > &ar, const vector<long double> &means, vector<long double> &stddevs) {
    int cols = ar[0].size();
    int rows = ar.size();

    for (int i = 0; i < cols; i++) {
        long double variance = 0;

        for (int j = 0; j < rows; j++)
            variance += pow(ar[j][i] - means[i], 2);
        variance = variance/(long double)rows;
        stddevs.push_back( sqrt(variance) );
    }

}

vector<long double> linspace(long double start, long double endd, int num){

    vector<long double> linspaced;

    if (num == 0){ return linspaced; }
    if (num == 1){
        linspaced.push_back(start);
        return linspaced;
    }

    long double delta = (endd - start) / (num - 1);

    for(int i=0; i < num-1; ++i){
        linspaced.push_back(start + delta * i);
    }
    linspaced.push_back(endd);
    return linspaced;
}

void col_min_max(const vector<vector<long double> > &ar, int col, long double &col_max, long double &col_min){
    col_max = col_min = ar[0][col];
    int cols = ar.size();

    if(ar.size() == 1)
        return;

    for (int i = 1; i < cols; i++) {
        if(ar[i][col] > col_max)
            col_max = ar[i][col];
        if(ar[i][col] < col_min)
            col_min = ar[i][col];
    }

}

