import numpy as np


def cost_(y, y_hat):
    """Computes the mean squared error of two non-empty numpy.ndarray, without any for loop. The
    ,→ two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    The mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.ndarray.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """
    if y.ndim == 2 and y.shape[1] == 1:
        y = y.flatten()
    if y_hat.ndim == 2 and y_hat.shape[1] == 1:
        y_hat = y_hat.flatten()

    if (y.size == 0 or y_hat.size == 0
        or y.ndim != 1 or y_hat.ndim != 1
            or y.shape != y_hat.shape):
        return None

    y_diff = y_hat - y
    return np.dot(y_diff, y_diff) / (2 * y.shape[0])


if __name__ == "__main__":
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])

    # Example 1:
    print(cost_(X, Y))
    # Output:
    # 2.142857142857143
    # (AND NOT 4.285714285714286 like it's written in the subject)

    # Example 2:
    print(cost_(X, X))
    # Output:
    # 0.0
