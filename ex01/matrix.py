class MatrixException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Matrix():

    def __init__(self, *args):
        if (len(args) == 2 and
                isinstance(args[0], list) and
                isinstance(args[1], tuple)):
            # from list + tuple
            self.__init_from_list(args[0])
            if self.shape != args[1]:
                raise MatrixException(
                    "Shape doesn't correspond to the given matrix")

        elif len(args) == 1:
            if isinstance(args[0], list):
                # from list
                self.__init_from_list(args[0])
            elif isinstance(args[0], tuple) and len(args[0]) == 2:
                # from tuple
                self.shape = args[0]
                self.data = [[0.0] * self.shape[1]
                             for n in range(self.shape[0])]
            else:
                raise MatrixException("Bad initialisation")

        else:
            raise MatrixException("Bad initialisation")

    def __init_from_list(self, lst):
        self.data = [[float(nbr) for nbr in raw] for raw in lst]
        self.shape = (len(self.data), len(self.data[0]))

        for raw in self.data:
            if len(raw) != self.shape[1]:
                raise MatrixException(
                    "Can't cast given list to matrix (bad shape)")

    def column(self, n):
        return [raw[n] for raw in self.data]

    def raw(self, n):
        return self.data[n]

    @staticmethod
    def __add(lm, rm):
        if not isinstance(lm, Matrix) or not isinstance(rm, Matrix):
            raise MatrixException("Can only add Matrix together")
        if lm.shape != rm.shape:
            raise MatrixException("Can't add matrix of different dimension")

        result = []
        for l_raw, r_raw in zip(lm.data, rm.data):
            result.append([l_nbr + r_nbr for l_nbr,
                           r_nbr in zip(l_raw, r_raw)])

        return Matrix(result)

    @staticmethod
    def __sub(lm, rm):
        if not isinstance(lm, Matrix) or not isinstance(rm, Matrix):
            raise MatrixException("Can only substract Matrix together")
        if lm.shape != rm.shape:
            raise MatrixException(
                "Can't substract matrix of different dimension")

        result = []
        for l_raw, r_raw in zip(lm.data, rm.data):
            result.append([l_nbr - r_nbr for l_nbr,
                           r_nbr in zip(l_raw, r_raw)])

        return Matrix(result)

    @staticmethod
    def __mul_with_scalar(matrix, scalar):
        result = []

        for raw in matrix.data:
            result.append([nbr * scalar for nbr in raw])

        return Matrix(result)

    @staticmethod
    def __mul(lm, rm):
        if not isinstance(lm, Matrix) or not isinstance(rm, Matrix):
            raise MatrixException(
                "Can only multiply Matrix with Matrix or scalar")
        if lm.shape[1] != rm.shape[0]:
            raise MatrixException(
                "Matrix multiplication is only possible between "
                "compatible dimension (m, n) * (n, p)")

        result = Matrix((lm.shape[0], rm.shape[1]))
        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                # sum(left.raw(i) * right.column(j))
                result.data[i][j] = sum(
                    [l_nbr * r_nbr for l_nbr,
                        r_nbr in zip(lm.raw(i), rm.column(j))]
                )

        return result

    @staticmethod
    def __div(left, right):
        if isinstance(left, Matrix) and isinstance(right, (int, float)):
            return Matrix([[nbr / right for nbr in raw] for raw in left.data])
        elif isinstance(left, (int, float)) and isinstance(right, Matrix):
            return Matrix([[left / nbr for nbr in raw] for raw in right.data])
        else:
            raise MatrixException("You can only divide Matrix with scalars")

    def __str__(self):
        return "M[\n" + "\n".join([str(raw) for raw in self.data]) + "]"

    def __repr__(self):
        return f"Matrix({self.data})"
        # return str(self.__dict__)

    def __add__(self, right_side):
        return Matrix.__add(self, right_side)

    def __radd__(self, left_side):
        return Matrix.__add(left_side, self)

    def __sub__(self, right_side):
        return Matrix.__sub(self, right_side)

    def __rsub__(self, left_side):
        return Matrix.__sub(left_side, self)

    def __truediv__(self, right_side):
        return Matrix.__div(self, right_side)

    def __rtruediv__(self, left_side):
        return Matrix.__div(left_side, self)

    def __mul__(self, right_side):
        if isinstance(right_side, (int, float)):
            return Matrix.__mul_with_scalar(self, right_side)
        else:
            return Matrix.__mul(self, right_side)

    def __rmul__(self, left_side):
        if isinstance(left_side, (int, float)):
            return Matrix.__mul_with_scalar(self, left_side)
        else:
            return Matrix.__mul(left_side, self)
