class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinklist():
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        print(cur.elem)

    def append(self, item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def add(self, item):
        node = Node(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此节点是否为头结点

                if cur == self.__head:  # if pre == None:
                    # 头结点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur为尾节点
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = cur.next


if __name__ == "__main__":
    mylist = SingleCycleLinklist()
    mylist.append(0)
    mylist.append(1)
    mylist.add(10)
    mylist.add(2)
    mylist.append(3)

    print(mylist.is_empty())
    print(mylist.length())
    print(mylist.search(0))
    mylist.travel()

    mylist.remove(0)
    # mylist.remove(3)
    mylist.insert(0, 0)
    mylist.insert(3, 22)
    mylist.insert(mylist.length(), 30)
    mylist.travel()
    print(mylist.is_empty())
