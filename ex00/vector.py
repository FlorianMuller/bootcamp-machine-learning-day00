class VectorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Vector():
    def __init__(self, init):
        if isinstance(init, list):
            self.values = [float(nbr) for nbr in init]
            self.size = len(init)
        elif isinstance(init, int):
            self.values = [float(nbr) for nbr in range(init)]
            self.size = init
        elif isinstance(init, tuple) and len(init) == 2:
            self.values = [float(nbr) for nbr in range(*init)]
            self.size = len(self.values)

    @staticmethod
    def __scalar_to_vec(nbr):
        if isinstance(nbr, int) or isinstance(nbr, float):
            return Vector([float(nbr)])
        return nbr

    @staticmethod
    def __add(l_vec, r_vec):
        if not l_vec.size == r_vec.size:
            raise VectorException("Can't add vector of different size")
        return Vector([l_nbr + r_nbr for l_nbr, r_nbr in
                      zip(l_vec.values, r_vec.values)])

    @staticmethod
    def __sub(l_vec, r_vec):
        if not l_vec.size == r_vec.size:
            raise VectorException("Can't subtract vector of different size")
        return Vector([l_nbr - r_nbr for l_nbr, r_nbr in
                      zip(l_vec.values, r_vec.values)])

    @staticmethod
    def __div(left, right):
        if isinstance(left, Vector) and isinstance(right, (int, float)):
            return Vector([l_nbr / right for l_nbr in left.values])
        elif isinstance(left, (int, float)) and isinstance(right, Vector):
            return Vector([left / r_nbr for r_nbr in right.values])
        else:
            raise VectorException("You can only divide Vector with scalars")

    @staticmethod
    def __mul(vec, other):
        if isinstance(other, (int, float)):
            return Vector([nbr * other for nbr in vec.values])
        elif isinstance(other, Vector):
            if not vec.size == other.size:
                raise VectorException("Can't multiply vector"
                                      " of different size")
            return sum([l_nbr * r_nbr for l_nbr, r_nbr in
                       zip(vec.values, other.values)])

    def __str__(self):
        return f"V{str(self.values)}"

    def __repr__(self):
        return f"Vector({self.values})"
        # return str(self.__dict__)

    def __add__(self, right_side):
        return Vector.__add(self, Vector.__scalar_to_vec(right_side))

    def __radd__(self, left_side):
        return Vector.__add(Vector.__scalar_to_vec(left_side), self)

    def __sub__(self, right_side):
        return Vector.__sub(self, Vector.__scalar_to_vec(right_side))

    def __rsub__(self, left_side):
        return Vector.__sub(Vector.__scalar_to_vec(left_side), self)

    def __truediv__(self, right_side):
        return Vector.__div(self, right_side)

    def __rtruediv__(self, left_side):
        return Vector.__div(left_side, self)

    def __mul__(self, right_side):
        return Vector.__mul(self, right_side)

    def __rmul__(self, left_side):
        # No diffrence, so left side to the right
        return Vector.__mul(self, left_side)
