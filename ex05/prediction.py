import numpy as np


def predict_(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """
    if x.size == 0 or x.ndim != 1 or theta.size != 2 or theta.ndim != 1:
        return None
    return np.dot(np.c_[np.ones(x.shape[0]), x], theta)


if __name__ == "__main__":
    x = np.arange(1, 6)

    # Example 1:
    theta1 = np.array([5, 0])
    print(predict_(x, theta1))
    # Output:
    # array([5., 5., 5., 5., 5.])

    # Example 2:
    theta2 = np.array([0, 1])
    print(predict_(x, theta2))
    # Output:
    # array([1., 2., 3., 4., 5.])

    # Example 3:
    theta3 = np.array([5, 3])
    print(predict_(x, theta3))
    # Output:
    # array([ 8., 11., 14., 17., 20.])

    # Example 4:
    theta4 = np.array([-3, 1])
    print(predict_(x, theta4))
    # Output:
    # array([-2., -1., 0., 1., 2.])

    # Empty array
    print(predict_(x, np.array([])))
    print(predict_(np.array([]), theta4))

    # Bad dimension
    print(predict_(x, np.array([[1, 1], [2, 2]])))
    print(predict_(np.array([[1, 1], [2, 2]]), theta4))
