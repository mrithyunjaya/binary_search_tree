class Node(object):
    def __init__(self, val=None):
        self.data = val
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            self._insert(self.head, val)

    def _insert(self, current_node, val):
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(val)

    def print_list(self):
        if self.head is not None:
            return LinkedList._print_list(self.head)

    @staticmethod
    def _print_list(current_node):
        while current_node:
            print current_node.data
            current_node = current_node.next_node

    def print_reverse(self):
        if self.head is not None:
            return LinkedList._print_reverse(self.head)

    @staticmethod
    def _print_reverse(current_node):
        if current_node.next_node is not None:
            LinkedList._print_reverse(current_node.next_node)
        print current_node.data

    def reverse_list(self):
        return self._reverse_list(self.head)

    def _reverse_list(self, current_node):
        if current_node is None:
            return
        elif current_node.next_node is None:
            self.head = current_node
            return
        self._reverse_list(current_node.next_node)
        current_node.next_node.next_node = current_node
        current_node.next_node = None

    
if __name__ == "__main__":
    list = LinkedList()
    list.insert(10)
    list.insert(25)
    list.insert(35)
    list.print_list()
    list.print_reverse()
    list.reverse_list()
    list.print_list()