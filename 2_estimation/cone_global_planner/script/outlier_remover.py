import numpy as np

def reject_outliers_1(data, m=2):
    mean = np.floor( [np.mean(data[:, 0]), np.mean(data[:, 1])] )
    std = np.floor( [np.std(data[:, 0]), np.std(data[:, 1])] )

    def outliers_func(num, coord=0):
        return abs(num - mean[coord]) < m * std[coord]
    
    return data[(outliers_func(data[:, 0], 0)) & (outliers_func(data[:, 1], 1))]

def reject_outliers_2(data, m=2.5):
    
    def outliers_func(num):
        d = np.abs(data - np.median(data))
        mdev = np.median(d)
        s = d/(mdev if mdev else 1.)
        return s<m

    xy = outliers_func(data[:, 0])

    return data[xy[:, 0] & xy[:, 1]]

def main():
    data = np.array([[ 1233.87375018,  1230.07095987],
       [ 1237.63559365,  1253.90749041],
       [ 1240.87500801,  1264.43925132],
       [ 1245.30875975,  1274.63795396],
       [ 1250.30875975,  1100], #outlier
       [ 1256.1449357 ,  1294.48254424],
       [ 1264.33600095,  1304.47893299],
       [ 1273.38192911,  1313.71468591],
       [ 1283.12411536,  1322.35942538],
       [ 1293.2559388 ,  1330.55873344],
       [ 1309.4817002 ,  1342.53074698],
       [ 1325.7074616 ,  1354.50276051],
       [ 1341.93322301,  1366.47477405],
       [ 1358.15898441,  1378.44678759],
       [ 1394.38474581,  1415.41880113]])
    
    print(reject_outliers_2(data))

if __name__ == "__main__":
    main()