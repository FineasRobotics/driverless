#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/lu.hpp>

/*
 Finds the coefficients of a polynomial p(x) of degree n that fits the data,
 p(x(i)) to y(i), in a least squares sense. The result p is a row vector of
 length n+1 containing the polynomial coefficients in incremental powers.
 
 param:
 xValues        x axis values
 yValues        y axis values
 degree         polynomial degree including the constant
 weights        optional, weights to apply to the y-coordinates of the sample points
 
 return:
 coefficients of a polynomial starting at the constant coefficient and
 ending with the coefficient of power to degree.
*/
template <typename T>
std::vector<T> polyfit_boost(const std::vector<T> &xValues, const std::vector<T> &yValues, const int degree, const std::vector<T>& weights = std::vector<T>()){
    using namespace boost::numeric::ublas;
    
    if (xValues.size() != yValues.size())
        throw std::invalid_argument("X and Y vector sizes do not match");
    
    bool useWeights = weights.size() > 0 && weights.size() == xValues.size();
    
    // one more because of c0 coefficient
    int numCoefficients = degree + 1;
    
    size_t nCount = xValues.size();
    matrix<T> X(nCount, numCoefficients);
    matrix<T> Y(nCount, 1);
    
    // fill Y matrix
    for (size_t i = 0; i < nCount; i++){
        if (useWeights)
            Y(i, 0) = yValues[i] * weights[i];
        else
            Y(i, 0) = yValues[i];
    }
    
    // fill X matrix (Vandermonde matrix)
    for (size_t nRow = 0; nRow < nCount; nRow++){
        T nVal = 1.0f;
        for (int nCol = 0; nCol < numCoefficients; nCol++){
            if (useWeights)
                X(nRow, nCol) = nVal * weights[nRow];
            else
                X(nRow, nCol) = nVal;
            nVal *= xValues[nRow];
        }
    }
    
    
    matrix<T> Xt(trans(X));// transpose X matrix
    
    matrix<T> XtX(prec_prod(Xt, X));// multiply transposed X matrix with X matrix
    
    matrix<T> XtY(prec_prod(Xt, Y));// multiply transposed X matrix with Y matrix
    
    // lu decomposition
    permutation_matrix<int> pert(XtX.size1());
    const std::size_t singular = lu_factorize(XtX, pert);
    
    assert(singular == 0);
    
    lu_substitute(XtX, pert, XtY);
    
    // copy the result to coeff
    return std::vector<T>(XtY.data().begin(), XtY.data().end());
}

/*
 Calculates the value of a polynomial of degree n evaluated at x. The input
 argument coefficients is a vector of length n+1 whose elements are the coefficients
 in incremental powers of the polynomial to be evaluated.
 
 return: Fitted Y values.
*/
template<typename T>
std::vector<T> polyval( const std::vector<T>& coefficients, const std::vector<T>& xValues ){
    size_t nCount = xValues.size();
    size_t nDegree = coefficients.size();
    std::vector<T> yValues( nCount );
    
    for (size_t i = 0; i < nCount; i++ ){
        T yVal = 0;
        T xPowered = 1;
        T xVal = xValues[i];
        for (size_t j = 0; j < nDegree; j++ ){
            yVal += coefficients[j] * xPowered;
            xPowered *= xVal;
        }
        yValues[i] = yVal;
    }
    
    return yValues;
}
