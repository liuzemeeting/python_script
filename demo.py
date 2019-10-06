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
    dd(sys.argv)