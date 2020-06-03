import math


class TinyStatistician:

    @staticmethod
    def mean(x):
        # return sum(x) / len(x) if len(x) else None

        # Or, with a for loop
        x_sum = 0
        for nbr in x:
            x_sum += nbr
        return x_sum / len(x) if len(x) else None

    @staticmethod
    def median(x):
        s = sorted(x)
        mid = len(s) // 2
        return (s[mid] + s[~mid]) / 2 if len(x) else None

    @staticmethod
    def quartile(x, percentile):
        s = sorted(x)
        return s[math.ceil(len(s) * percentile / 100) - 1] if len(s) else None

    @staticmethod
    def var(x):
        # if not len(x):
        #     return None
        # x_mean = TinyStatistician.mean(x)
        # return sum([(nbr - x_mean) ** 2 for nbr in x]) / len(x)

        # Or, with a for loop
        x_mean = TinyStatistician.mean(x)
        x_sum = 0
        for nbr in x:
            x_sum += (nbr - x_mean) ** 2

        return x_sum / len(x) if len(x) else None

    @staticmethod
    def std(x):
        return math.sqrt(TinyStatistician.var(x)) if len(x) else None


def test_TinyStatistician(lst):
    print("mean:\t ", TinyStatistician.mean(lst))
    print("median:\t ", TinyStatistician.median(lst))
    print("quartile:", TinyStatistician.quartile(lst, 25))
    print("quartile:", TinyStatistician.quartile(lst, 75))
    print("var:\t ", TinyStatistician.var(lst))
    print("std:\t ", TinyStatistician.std(lst))


if __name__ == "__main__":
    a = [1, 42, 300, 10, 59]
    test_TinyStatistician(a)

    print("\n")
    test_TinyStatistician([1, 2, 10, 500])

    print("\n")
    test_TinyStatistician([])
