from vector import Vector, VectorException


def test_vector():
    # Init with list
    vec = Vector([1, 2, 3])
    print("1. ", vec.__dict__)

    # Init with size
    vec = Vector(10)
    print("2. ", vec.__dict__)

    # Init with range
    vec = Vector((40, 42))
    print("3. ", vec.__dict__)

    # Add
    print("4. ", Vector(3) + Vector((10, 13)))

    # Add scalar
    print("5. ", Vector([8]) + 2)
    print("6. ", 2 + Vector([8]))

    # Add with diffrent size
    try:
        print("7. ", Vector(3) + Vector(5))
        print("7. ~~~ Error ~~~")
    except VectorException as e:
        print("7. ", e)

    # Sub
    print("8. ", Vector(3) - Vector((10, 13)))

    # Sub with scalar
    print("9. ", Vector([10]) - 5)
    print("10. ", 5 - Vector([10]))

    # Sub with diffrent size
    try:
        print("11. ", Vector(3) - Vector(5))
        print("11. ~~~ Error ~~~")
    except VectorException as e:
        print("11. ", e)

    # Div with scalars
    print("12. ", Vector([10, 20, 30]) / 2)
    print("13. ", 12 / Vector([2, 3, 4, 5]))

    # Div with 2 vectors
    try:
        print("14. ", Vector(10) / Vector(10))
        print("14. ~~~ Error ~~~")
    except VectorException as e:
        print("14. ", e)

    # Mul with scalars
    print("15. ", Vector(4) * 4)
    print("16. ", 4 * Vector(4))
    print("17. ", Vector(4) * 2.5)
    print("18. ", 2.5 * Vector(4))

    # Mul with Vector
    print("19. ", Vector(4) * Vector(4))

    # Mul with diffrent size
    try:
        print("20. ", Vector(3) * Vector(5))
        print("20. ~~~ Error ~~~")
    except VectorException as e:
        print("20. ", e)

    # str and repr
    cool_vector = Vector(5)

    print(cool_vector)
    print(repr(cool_vector))

    # `repr()` can be used to create the same Vector
    # res = eval(repr(cool_vector))
    # print(res)


if __name__ == "__main__":
    test_vector()
