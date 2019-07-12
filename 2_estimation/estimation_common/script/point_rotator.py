import numpy as np
import matplotlib.pyplot as plt

def rotate_array(array, turn=1):
    return np.array([ [ turn * point[1], turn * -point[0]] for point in array])

def main():
    a = np.array([ [ -3, 1], [ 3, 1], [ 3, -1], [ -3, -1] ])
    a = rotate_array(a, -1)
    a = rotate_array(a)
    plt.scatter(a[:, 0], a[:, 1], c='orange')
    plt.show()

if __name__ == "__main__":
    main()
