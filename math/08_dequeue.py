class Queue():
    """队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队列头部中添加一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队列尾部添加一个元素"""
        return self.__list.append(item)

    def pop_front(self):
        """从队列中头部删除一个元素"""
        self.__list.pop(0)

    def pop_rear(self):
        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)