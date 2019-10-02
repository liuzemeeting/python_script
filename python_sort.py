a = [59,1, 2, 43, 3, 9, 7, 6]


def bubble_sort(data):
    """
    冒泡排序算法的运作如下：
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
    :param data:
    :return:
    """
    length = len(data)
    for i in range(length):
        for j in range(1, length-i):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
    return data


if __name__ == "__main__":
    data = bubble_sort(a)
    print(data)