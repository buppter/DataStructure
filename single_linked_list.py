class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinklist():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def append(self, item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

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
        while cur is not None:
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
    mylist = SingleLinklist()
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
