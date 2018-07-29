class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            self._insert(self.root, val)

    def _insert(self, current_node, val):
        if val < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(val)
                current_node.left_child.parent = current_node
            else:
                self._insert(current_node.left_child, val)
        elif val > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(val)
                current_node.right_child.parent = current_node
            else:
                self._insert(current_node.right_child, val)
        else:
            print "Trying to insert data which is already in the tree"

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, current_node, val):
        if current_node is not None:
            if val == current_node.value:
                print ("the value you searching for is present"), val
                return True
            elif val < current_node.value:
                return self._search(current_node.left_child, val)
            elif val > current_node.value:
                return self._search(current_node.right_child, val)
        else:
            print "the element is not found"

    def _find(self, current_node, val):
        if current_node is not None:
            if val == current_node.value:
                # print current_node
                return current_node
            elif val < current_node.value:
                return self._find(current_node.left_child, val)
            elif val > current_node.value:
                return self._find(current_node.right_child, val)
        else:
            print "the element is not found"

    def delete(self, val):
        return self._delete_node(self.root, val)

    def _delete_node(self, current_node, val):
        if self.search(val):
            temp = self._find(current_node, val)
            if temp.right_child is None and temp.left_child is None:
                if temp.left_child is None or temp.parent.left_child.value == val:
                    temp.parent.left_child = None
                    temp.parent = None
                    print "value deleted", val
                elif temp.parent.right_child.value == val:
                    temp.parent.right_child = None
                    temp.parent = None
                    print "value deleted", val
            elif temp.left_child is not None and temp.right_child is not None:
                temp1 = temp.right_child
                while temp1.left_child is not None:
                    temp1 = temp1.left_child
                temp.value = temp1.value
                temp1.parent.left_child = None
                temp1.parent = None
                print "value deleted", val
            elif temp.left_child is not None or temp.right_child is not None:
                if temp.left_child is not None:
                    temp1 = temp.left_child
                    temp.value = temp1.value
                    temp1.parent.left_child = None
                    print "value deleted", val
                if temp.right_child is not None:
                    temp1 = temp.right_child
                    temp.value = temp1.value
                    temp1.parent.right_child = None
                    print "value deleted", val
                temp1.parent = None
        else:
            print "no data found to delete"

    def print_node(self):
        if self.root is None:
            return False


if __name__ == "__main__":
    BST = BinarySearchTree()

    BST.insert(10)
    BST.insert(11)
    BST.insert(12)
    BST.insert(7)
    BST.insert(5)
    BST.insert(9)
    BST.delete(5)
    BST.search(5)
    BST.delete(9)
    BST.delete(18)
    BST.delete(10)
    BST.search(10)
    BST.delete(12)
    BST.search(12)
