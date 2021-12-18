"""
1.2-单链表
"""
from typing import Any, Optional

# noinspection PyUnresolvedReferences
__all__ = ["__repr__", "__len__", "__getitem__", "__setitem__", "__iter__", "__add__",
           "insert", "append", "pop", "remove", "reverse", "index", "count", "show",
           "isempty", "middle_element", ]


# 单链表的节点
class Node:
    def __init__(self, data: Any):
        """
        初始化类实例
        >>> Node(20)
        Node(20)
        >>> Node("hello, world!")
        Node(hello, world!)
        >>> Node(None)
        Node(None)
        """
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        """
        类描述
        >>> Node(10).__repr__()
        'Node(10)'
        """
        return f"Node({self.data})"

# 单链表类
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        """
        单链表字符串描述
        >>> linked_list = LinkedList()
        >>> linked_list.insert(0, 1)
        >>> linked_list.insert(0, 3)
        >>> linked_list.insert(len(linked_list), 5)
        >>> linked_list
        3->1->5
        """
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        """
        返回链表长度
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert(len(linked_list), 'tail')
        >>> linked_list.insert(0, 'head')
        >>> len(linked_list)
        2
        >>> linked_list.pop()
        'tail'
        >>> linked_list.remove('head')
        >>> len(linked_list)
        0
        """
        return len(tuple(iter(self)))

    def __iter__(self) -> Any:
        """
        迭代器
        >>> linked_list = LinkedList()
        >>> linked_list.insert(len(linked_list), "tail1")
        >>> linked_list.insert(len(linked_list), "tail2")
        >>> linked_list.insert(len(linked_list), "tail3")
        >>> for node in linked_list:
        ...     node
        'tail1'
        'tail2'
        'tail3'
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __getitem__(self, index: int) -> Any:
        """
        重载[], get
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert(i, i+1)
        >>> all(str(linked_list[i]) == str(i+1) for i in range(0, 10))
        True
        >>> linked_list[len(linked_list)]
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node

    def __setitem__(self, index: int, data: Any) -> None:
        """
        重载[], set
        >>> linked_list = LinkedList()
        >>> for i in range(0,10):
        ...     linked_list.insert(i, i)
        >>> linked_list[0] = 'hello, world'
        >>> linked_list
        hello, world->1->2->3->4->5->6->7->8->9
        >>> linked_list[-10] = 6666
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index <= len(self):
            raise ValueError("list index out of range.")

        #new_node = Node(data)

        current = self.head
        for i in range(index):
            current = current.next
        #new_node.next = current.next
        current.data = data

    #cdef __add__(self, linkedlist: LinkedList,) -> LinkedList:
    def __add__(self, linkedlist: Any, ) -> Any:
        """
        重载+
        >>> linked_list1 = LinkedList()
        >>> linked_list2 = LinkedList()
        >>> for i in range(0,10):
        ...     linked_list1.insert(i, i)
        >>> linked_list2.insert(0, 'hello, world')
        >>> linked_list2
        hello, world
        >>> linked_list1[len(linked_list1)-1]
        9
        >>> linked_list1 = linked_list1 + linked_list2
        >>> linked_list1
        0->1->2->3->4->5->6->7->8->9->hello, world
        """
        assert isinstance(linkedlist, LinkedList)

        if self.isempty():
            return linkedlist

        if linkedlist.isempty():
            return self

        tmp = self.head
        for _ in range(len(self)-1):
            tmp = tmp.next
        tmp.next = linkedlist.head

        return self

    def insert(self, index: int, data: Any) -> None:
        """
        链表插入节点
        >>> linked_list = LinkedList()
        >>> linked_list.insert(len(linked_list), 'first')
        >>> linked_list.insert(len(linked_list), 'second')
        >>> linked_list.insert(len(linked_list), 'third')
        >>> linked_list
        first->second->third
        >>> linked_list.insert(1, 'fourth')
        >>> linked_list
        first->fourth->second->third
        >>> linked_list.insert(3, 'fifth')
        >>> linked_list
        first->fourth->second->fifth->third
        """
        if not 0 <= index <= len(self):
            raise IndexError('list index out of range.')

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            tmp = self.head
            for _ in range(index-1):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node

    def append(self, data: Any) -> None:
        """
        链表在最后插入节点
        >>> linked_list = LinkedList()
        >>> linked_list.insert(len(linked_list), 'tail1')
        >>> linked_list
        tail1
        >>> linked_list.insert(len(linked_list), 'tail2')
        >>> linked_list
        tail1->tail2
        >>> linked_list.insert(len(linked_list), 'tail3')
        >>> linked_list
        tail1->tail2->tail3
        """
        self.insert(len(self), data)

    def pop(self, index: int = -1) -> Any:
        """
        删除第index个节点，默认删除最后一个节点，并返回节点
        >>> linked_list = LinkedList()
        >>> linked_list.pop()
        Traceback (most recent call last):
        ...
        IndexError: pop from empty list.
        >>> linked_list.insert(len(linked_list), 'first')
        >>> linked_list.insert(len(linked_list), 'second')
        >>> linked_list.insert(len(linked_list), 'third')
        >>> linked_list
        first->second->third
        >>> linked_list.pop(1)
        'second'
        >>> linked_list.pop()
        'third'
        >>> linked_list.pop(5)
        Traceback (most recent call last):
        ...
        IndexError: List index out of range.
        """
        if self.isempty():
            raise IndexError('pop from empty list.')

        if index == -1:
            index = len(self)-1

        if not 0 <= index <= len(self) - 1:
            raise IndexError('List index out of range.')

        pop_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            tmp = self.head
            for _ in range(index - 1):
                tmp = tmp.next
            pop_node = tmp.next
            tmp.next = tmp.next.next

        return pop_node.data

    def remove(self, data: Any) -> None:
        """
        删除值为data的节点
        >>> linked_list = LinkedList()
        >>> linked_list.remove(1)
        Traceback (most recent call last):
        ...
        ValueError: remove from empty list.
        >>> linked_list.insert(len(linked_list), 'first')
        >>> linked_list.insert(len(linked_list), 'second')
        >>> linked_list.insert(len(linked_list), 'third')
        >>> linked_list
        first->second->third
        >>> linked_list.remove('second')
        >>> linked_list
        first->third
        >>> linked_list.remove('third')
        >>> linked_list
        first
        >>> linked_list.remove(5)
        Traceback (most recent call last):
        ...
        ValueError: LinkedList.remove(x): x not in list.
        """
        if self.isempty():
            raise ValueError('remove from empty list.')

        prv = tmp = self.head
        # 如果是头节点
        if data == self.head.data:
            self.head = self.head.next
            return
        else:
            tmp = tmp.next
            # 遍历链表删除值为data的节点，找不到则报异常
            for _ in range(len(self)-1):
                if data == tmp.data:
                    prv.next = prv.next.next
                    return
                prv = tmp
                tmp = tmp.next
            if tmp and data == tmp.data:
                prv.next = prv.next.next
                return
            else:
                raise ValueError('LinkedList.remove(x): x not in list.')

    # 反转链表
    def reverse(self) -> None:
        """
        链表反序
        >>> linked_list = LinkedList()
        >>> linked_list.insert(0, "third")
        >>> linked_list.insert(0, "second")
        >>> linked_list.insert(0, "first")
        >>> linked_list
        first->second->third
        >>> linked_list.reverse()
        >>> linked_list
        third->second->first
        """
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def index(self, data: Any) -> Any:
        """
        返回值为data的索引
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert(i, i+1)
        >>> linked_list.index(9)
        8
        >>> linked_list.index(11)
        Traceback (most recent call last):
        ...
        ValueError: LinkedList.index(x): x not in list.
        """
        for i, node in enumerate(self):
            if data == node:
                return i
        else:
            raise ValueError('LinkedList.index(x): x not in list.')

    def count(self):
        return len(tuple(iter(self)))

    def isempty(self) -> bool:
        """
        Check if linked list is empty.
        >>> linked_list = LinkedList()
        >>> linked_list.isempty()
        True
        >>> linked_list.insert(0, "first")
        >>> linked_list.isempty()
        False
        """
        return self.head is None

    def middle_element(self) -> Optional[int]:
        """
        >>> link = LinkedList()
        >>> for i in range(0, 10):
        ...     link.insert(len(link), i)
        >>> link.middle_element()
        5
        """
        slow_pointer = self.head
        fast_pointer = self.head

        if self.isempty():
            raise IndexError('middle_element from empty list.')

        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer.data

    def show(self) -> None:  # print every node data
        """
        This method prints every node data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert(0, "first")
        >>> linked_list.insert(0, "second")
        >>> linked_list.insert(0, "third")
        >>> linked_list.show()
        third->second->first
        """
        print(self)

def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    linked_list = LinkedList()
    assert linked_list.isempty() is True
    assert str(linked_list) == ""

    try:
        linked_list.pop(0)
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.pop(-1)
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert(0, 0)
    linked_list.insert(len(linked_list), 11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.pop(0) == 0
    assert linked_list.pop(9) == 10
    assert linked_list.pop(-1) == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))

    assert all(linked_list[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        linked_list[i] = -i
    assert all(linked_list[i] == -i for i in range(0, 9)) is True

    linked_list.reverse()
    assert str(linked_list) == "->".join(str(i) for i in range(-8, 1))


def test_singly_linked_list_2() -> None:
    """
    This section of the test used varying data types for input.
    >>> test_singly_linked_list_2()
    """
    input = [
        -9,
        100,
        Node(77345112),
        "dlrow olleH",
        7,
        5555,
        0,
        -192.55555,
        "Hello, world!",
        77.9,
        Node(10),
        None,
        None,
        12.20,
    ]
    linked_list = LinkedList()

    for i in input:
        linked_list.insert(len(linked_list), i)

    # Check if it's empty or not
    assert linked_list.isempty() is False
    assert (
        str(linked_list) == "-9->100->Node(77345112)->dlrow olleH->7->5555->0->"
        "-192.55555->Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the head
    result = linked_list.pop(0)
    assert result == -9
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None->None->12.2"
    )

    # Delete the tail
    result = linked_list.pop(-1)
    assert result == 12.2
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None->None"
    )

    # Delete a node in specific location in linked list
    result = linked_list.pop(10)
    assert result is None
    assert (
        str(linked_list) == "100->Node(77345112)->dlrow olleH->7->5555->0->-192.55555->"
        "Hello, world!->77.9->Node(10)->None"
    )

    # Add a Node instance to its head
    linked_list.insert(0, Node("Hello again, world!"))
    assert (
        str(linked_list)
        == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
        "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None"
    )

    # Add None to its tail
    linked_list.insert(len(linked_list), None)
    assert (
        str(linked_list)
        == "Node(Hello again, world!)->100->Node(77345112)->dlrow olleH->"
        "7->5555->0->-192.55555->Hello, world!->77.9->Node(10)->None->None"
    )

    # Reverse the linked list
    linked_list.reverse()
    assert (
        str(linked_list)
        == "None->None->Node(10)->77.9->Hello, world!->-192.55555->0->5555->"
        "7->dlrow olleH->Node(77345112)->100->Node(Hello again, world!)"
    )


if __name__ == "__main__":
    from doctest import testmod
    testmod()







