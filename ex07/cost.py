import numpy as np


def predict_(x, theta):
    if x.ndim == 1:
        x = x[:, np.newaxis]
    if theta.ndim == 1:
        theta = theta[:, np.newaxis]

    if (x.size == 0 or theta.size == 0
        or x.ndim != 2 or theta.ndim != 2
            or theta.shape[1] != 1 or theta.shape[0] != x.shape[1] + 1):
        return None
    return np.dot(np.c_[np.ones(x.shape[0]), x], theta)


def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: numpy.ndarray, a vector of dimension (number of the training examples,1).
    None ",1.", if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    if y.ndim == 1:
        y = y[:, np.newaxis]
    if y_hat.ndim == 1:
        y_hat = y_hat[:, np.newaxis]

    if y.size == 0 or y_hat.size == 0 or y.shape != y_hat.shape:
        return None

    return ((y_hat - y) ** 2) / (2 * y.shape[0])


def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    c = cost_elem_(y, y_hat)
    return None if c is None else np.sum(c)


if __name__ == "__main__":
    x1 = np.array([[0.], [1.], [2.], [3.], [4.]])
    theta1 = np.array([[2.], [4.]])
    y_hat1 = predict_(x1, theta1)
    y1 = np.array([[2.], [7.], [12.], [17.], [22.]])

    # Example 1:
    print("1.", cost_elem_(y1, y_hat1))
    # Output:
    # array([[0.], [0.1], [0.4], [0.9], [1.6]])

    # Example 2:
    print("2.", cost_(y1, y_hat1))
    # Output:
    # 3.0

    # ~~~~~~~~~~

    x2 = np.array([[0.2, 2., 20.], [0.4, 4., 40.],
                   [0.6, 6., 60.], [0.8, 8., 80.]])
    theta2 = np.array([[0.05], [1.], [1.], [1.]])
    y_hat2 = predict_(x2, theta2)
    y2 = np.array([[19.], [42.], [67.], [93.]])

    # Example 3:
    print("3.", cost_elem_(y2, y_hat2))
    # Output:
    # array([[1.3203125], [0.7503125], [0.0153125], [2.1528125]])

    # Example 4:
    print("4.", cost_(y2, y_hat2))
    # Output:
    # 4.238750000000004

    # ~~~~~~~~~~

    x3 = np.array([0, 15, -9, 7, 12, 3, -21])
    theta3 = np.array([[0.], [1.]])
    y_hat3 = predict_(x3, theta3)
    y3 = np.array([2, 14, -13, 5, 12, 4, -19])

    # Example 5:
    print("5.", cost_(y3, y_hat3))
    # Output:
    # 2.142857142857143
    # (AND NOT 4.285714285714286 like it's written in the subject)

    # Example 6:
    print("6.", cost_(y3, y3))
    # Output:
    # 0.0
