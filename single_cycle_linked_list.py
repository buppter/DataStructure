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
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 先判断此节点是否为头结点
                # 头结点
                if cur == self.__head:  # if pre == None:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    mylist = SingleCycleLinklist()
    print(mylist.is_empty())
    print(mylist.length())

    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.append(4)
    mylist.append(5)
    mylist.add(10)
    print(mylist.is_empty())
    print(mylist.length())
    mylist.insert(0, 100)
    mylist.insert(4, 44)
    mylist.insert(mylist.length(), 200)
    mylist.insert(13, 300)
    mylist.travel()
    print(mylist.search(44))
    print(mylist.search(4000))
    mylist.remove(10)
    mylist.travel()
    mylist.remove(100)
    mylist.travel()
    mylist.remove(44)
    mylist.travel()
    mylist.remove(200)
    mylist.travel()
