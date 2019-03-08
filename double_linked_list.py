class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
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

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        node = Node(item)
        cur = self.__head
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() -1 ):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next 
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

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
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next is not None:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next



if __name__ == "__main__":
    mylist = DoubleLinkedList()
    print(mylist.is_empty())
    print(mylist.length())
    mylist.append(9)
    mylist.add(1)
    print(mylist.is_empty())
    print(mylist.length())
    mylist.add(0)
    mylist.append(2)
    mylist.append(3)
    mylist.append(4)
    mylist.append(5)
    print(mylist.is_empty())
    print(mylist.length())
    mylist.travel()
    mylist.insert(0, 100)
    mylist.insert(3, 200)
    mylist.travel()
    mylist.remove(300)
    mylist.remove(100)
    mylist.travel()

