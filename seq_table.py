# coding: utf-8


class SeqList:

    def __init__(self, max=10):
        self.num = 0
        self.max = max
        self.data = [None] * self.max

    # 判断线性表是否是空
    def is_empty(self):
        return self.num

    # 判断是否全满
    def is_full(self):
        return self.num is self.max

    # 获取线性表中某一个位置的元素
    def __getitem__(self, item):
        if not isinstance(item, int):
            return TypeError
        if 0 <= item < self.max:
            return self.data[item]
        return TypeError

    # 修改线性表中某一位置的元素
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < self.max:
            return self.data[key]
        raise TypeError

    # 按值查找元素的位置
    def getLoc(self, value):
        for i in range(self.num):
            if self.data[i] == value:
                return i
        return -1

    # 统计线性表的个数
    def Count(self):
        return self.num

    # 表末尾插入数据
    def appendlist(self, value):
        if self.num >= self.max:
            raise TypeError
        else:
            self.data[self.num] = value
            self.num += 1

    # 表任意位置插入数据
    def insert(self, i, value):
        if not isinstance(i, int):
            return TypeError
        for j in range(self.num, i, i-1):
            self.data[j] = self.data[j-1]
        self.data[i] = value
        self.num += 1

    # 删除某一个位置的操作
    def delete(self, i):
        for j in range(i, self.num):
            self.data[j] = self.data[j+1]
        self.num -= 1

    # 输出操作
    def printlist(self):
        for i in range(0, self.num):
            print(self.data[i])

    # 销毁操作
    def destory(self):
        self.__init__()