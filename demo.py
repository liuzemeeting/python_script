import sys


def dd(id):
    """

    :param id:
    :return:
    """
    print("id", id[:])
    if id == 1:
        print("我是1")
    else:
        print("fffffffff")


if __name__ == "__main__":
    # dd(sys.argv)
    a = 10
    if a > 9:
        print("1")
    elif a > 8:
        print("2")
    elif a > 7:
        print("12")
    elif a > 6:
        print("4")
    elif a > 5:
        print("15")
    elif a > 4:
        print("1666")
    else:
        print("fffffffffffffffff")