from matrix import Matrix, MatrixException


def test_matrix():
    # Init with list
    m = Matrix([[1, 2], [3, 4], [5, 6]])
    print("\n1.", m.__dict__)

    # Init with bad list
    try:
        print("\n2.", Matrix([[1, 2], [3, 4, 5, 6]]))
        print("\n2.~~~ Error ~~~")
    except MatrixException as e:
        print("\n2.", e)

    # Init with tuple
    m = Matrix((3, 2))
    print("\n3.", m.__dict__)

    # Init with list and tuple
    m = Matrix([[1, 1, 1], [2, 2, 2]], (2, 3))
    print("\n4.", m.__dict__)

    # Init with bad list and tuple
    try:
        print("\n5.", Matrix([[1, 2], [3, 4]], (10, 10)))
        print("\n5.~~~ Error ~~~")
    except MatrixException as e:
        print("\n5.", e)

    # Defining some simple matrix to test operation
    m1_22 = Matrix([[1, 1], [1, 1]])
    m_22 = Matrix([[1, 2], [3, 4]])
    m_33 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Add
    print("\n6.", m1_22 + m_22)

    # Add matrix of different dimension
    try:
        print("\n7.", m_22 + m_33)
        print("\n7.~~~ Error ~~~")
    except MatrixException as e:
        print("\n7.", e)

    # Sub
    print("\n8.", m_22 - m1_22)

    # Sub matrix of different dimension
    try:
        print("\n9.", m_22 - m_33)
        print("\n9.~~~ Error ~~~")
    except MatrixException as e:
        print("\n9.", e)

    # Mul with scalar
    print("\n10.", m_22 * 11)
    print("\n11.", 11 * m_22)

    # Mul between Matrix
    print("\n12.", Matrix([[1, 3], [2, 5]]) * Matrix([[0, 1], [3, 2]]))
    # (Should be -> [[9, 7], [15, 12]])

    # Mul with not compatible matrix
    try:
        print("\n13.", m_22 * m_33)
        print("\n13.~~~ Error ~~~")
    except MatrixException as e:
        print("\n13.", e)

    # Div with scalar
    print("\n14.", m_22 / 2)
    print("\n15.", 10 / m_22)

    # str and repr
    print(f"\n16. \n{Matrix((5,6))}")
    print("\n17.", repr(m_22))

    # `repr()` can be used to create the same Vector
    res = eval(repr(m_22))
    print(f"\n18. \n{res}")


if __name__ == "__main__":
    test_matrix()
