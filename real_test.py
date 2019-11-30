
import copy


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __copy__(self):
        # self.val = x.val
        # self.next = x.next
        # self.random = x.random
        print("hehhe")
    @property
    def __deepcopy__(self, x):
        self.val = x.val
        self.next = x.next
        self.random = x.random
        print("Fdsafsa")
        return x


test = Node(23)
test_q = Node(23)
# test_3= copy.deepcopy(test)
print(getattr(test, "val"))
print(id(test))
