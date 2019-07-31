import matplotlib.pyplot as plt
import numpy as np

def middleLine(a1, a2, poly_deg=4, n_points=100, plot=True):
    min_a1_x, max_a1_x = min(a1[:, 0]), max(a1[:, 0])
    new_a1_x = np.linspace(min_a1_x, max_a1_x, n_points)
    a1_coefs = np.polyfit(a1[:, 0], a1[:, 1], poly_deg)
    new_a1_y = np.polyval(a1_coefs, new_a1_x)

    min_a2_x, max_a2_x = min(a2[:, 0]), max(a2[:, 0])
    new_a2_x = np.linspace(min_a2_x, max_a2_x, n_points)
    a2_coefs = np.polyfit(a2[:, 0], a2[:, 1], poly_deg)
    new_a2_y = np.polyval(a2_coefs, new_a2_x)

    midx = [np.mean([new_a1_x[i], new_a2_x[i]]) for i in range(n_points)]
    midy = [np.mean([new_a1_y[i], new_a2_y[i]]) for i in range(n_points)]

    if plot:
        plt.plot(a1[:, 0], a1[:, 1], c='black')
        plt.plot(new_a1_x, new_a1_y, c='blue')
        plt.plot(a2[:, 0], a2[:, 1], c='black')
        plt.plot(new_a2_x, new_a2_y, c='blue')
        plt.plot(midx, midy, '--', c='black')
        plt.show()
    
    return np.array([[x, y] for x, y in zip(midx, midy)])

def main():
    a1 = np.array([[ 1233.87375018,  1230.07095987],
       [ 1237.63559365,  1253.90749041],
       [ 1240.87500801,  1264.43925132],
       [ 1245.30875975,  1274.63795396],
       [ 1256.1449357 ,  1294.48254424],
       [ 1264.33600095,  1304.47893299],
       [ 1273.38192911,  1313.71468591],
       [ 1283.12411536,  1322.35942538],
       [ 1293.2559388 ,  1330.55873344],
       [ 1309.4817002 ,  1342.53074698],
       [ 1325.7074616 ,  1354.50276051],
       [ 1341.93322301,  1366.47477405],
       [ 1358.15898441,  1378.44678759],
       [ 1394.38474581,  1390.41880113]])

    a2 = np.array([[ 1152.27115094,  1281.52899302],
       [ 1155.53345506,  1295.30515742],
       [ 1163.56506781,  1318.41642169],
       [ 1168.03497425,  1330.03181319],
       [ 1173.26135672,  1341.30559949],
       [ 1184.07110925,  1356.54121651],
       [ 1194.88086178,  1371.77683353],
       [ 1202.58908737,  1381.41765447],
       [ 1210.72465255,  1390.65097106],
       [ 1227.81309742,  1403.2904646 ],
       [ 1244.90154229,  1415.92995815],
       [ 1261.98998716,  1428.56945169],
       [ 1275.89219696,  1438.21626352],
       [ 1289.79440676,  1447.86307535],
       [ 1303.69661656,  1457.50988719],
       [ 1323.80994319,  1470.41028655],
       [ 1343.92326983,  1488.31068591],
       [ 1354.31738934,  1499.33260989],
       [ 1374.48879779,  1516.93734053],
       [ 1394.66020624,  1534.54207116]])

    #making 1/4 circle
    # theta = np.linspace(0, np.pi/2, 30)
    # x = np.cos(theta)
    # y = np.sin(theta)
    # z = x*0.8
    # w = y*0.8
    # a1 = np.column_stack((x, y))
    # a2 = np.column_stack((z, w))

    #making 1/2 circle
    # theta = np.linspace(0, np.pi, 50)
    # r1 = np.sqrt(0.6)
    # r2 = np.sqrt(0.4)
    # x = r1*np.cos(theta)
    # y = r1*np.sin(theta)
    # z = r2*np.cos(theta)
    # w = r2*np.sin(theta)
    # a1 = np.column_stack((x, y))
    # a2 = np.column_stack((z, w))

    middleLine(a1, a2, 4, 150, True)

if __name__ == "__main__":
    main()
