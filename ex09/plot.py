import numpy as np
import matplotlib.pyplot as plt


def predict_(x, theta):
    if x.ndim == 1:
        x = x[:, np.newaxis]
    if theta.ndim == 2 and theta.shape[1] == 1:
        theta = theta.flatten

    if (x.size == 0 or theta.size == 0
        or x.ndim != 2 or theta.ndim != 1
            or theta.shape[0] != x.shape[1] + 1):
        return None

    # np.dot(a,b): a is an N-D array and b is a 1-D array
    # => it is a sum product over the last axis of a and b.
    return np.dot(np.c_[np.ones(x.shape[0]), x], theta)


def cost_(y, y_hat):
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


def plot_with_cost(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exception.
    """
    if x.size != 0 and y.size != 0 and theta.size != 0:
        # Data points
        plt.plot(x, y, "ob")

        # Prediction line
        y_hat = predict_(x, theta)
        plt.plot(x, y_hat, "-r")

        # Cost
        plt.title(f"cost: {cost_(y, y_hat)}")

        # Diff line between y and y_hat
        for x_val, y_val, y_hat_val in zip(x, y, y_hat):
            plt.plot([x_val, x_val], [y_val, y_hat_val], "--r")

        plt.show()


if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([11.52434424, 10.62589482,
                  13.14755699, 18.60682298, 14.14329568])

    # Example 1:
    theta1 = np.array([18, -1])
    plot_with_cost(x, y, theta1)

    # Example 2:
    theta2 = np.array([14, 0])
    plot_with_cost(x, y, theta2)

    # Example 3:
    theta3 = np.array([12, 0.8])
    plot_with_cost(x, y, theta3)
