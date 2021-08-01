class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def travel(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def insertAt(self, middle, data):
        if not middle:
            return
        node = Node(data)
        node.next = middle.next
        middle.next = node

    def delNode(self, remove):
        head = self.head
        if head:
            if head.data == remove:
                self.head = head.next
                head = None
                return

        while head is not None:
            if head.data == remove:
                break
            prev = head
            head = head.next

        if head is None:
            return

        prev.next = head.next
        head = None


def main():
    theLinkList = LinkList()
    theLinkList.head = Node('Mon')
    n2 = Node('Tue')
    n3 = Node('Wed')

    theLinkList.head.next = n2
    n2.next = n3
    n3.next = Node('Thu')

    theLinkList.travel()
    print('\r\n')
    theLinkList.insert('Sun')
    theLinkList.travel()
    print('\n')
    theLinkList.append('Fri')
    theLinkList.travel()


if __name__ == '__main__':
    main()


