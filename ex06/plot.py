import numpy as np
import matplotlib.pyplot as plt


def predict_(x, theta):
    if x.size == 0 or x.ndim != 1 or theta.size != 2 or theta.ndim != 1:
        return None
    return np.dot(np.c_[np.ones(x.shape[0]), x], theta)


def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """
    if x.size != 0 and y.size != 0 and theta.size != 0:
        linear_x = x[::x.shape[0] - 1]
        plt.plot(linear_x, predict_(linear_x, theta), "-r")
        plt.plot(x, y, "ob")
        plt.show()


if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])

    # Example 1:
    theta1 = np.array([4.5, -0.2])
    plot(x, y, theta1)

    # Example 2:
    theta2 = np.array([-1.5, 2])
    plot(x, y, theta2)

    # Example 3:
    theta3 = np.array([3, 0.3])
    plot(x, y, theta3)
