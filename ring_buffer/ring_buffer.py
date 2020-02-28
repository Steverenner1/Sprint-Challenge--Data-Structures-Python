# Beginning Challenge
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If storage is not full, adding to tail
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # Updating storage
        elif self.storage.length == self.capacity:
            current_head = self.storage.head
        # If storage is full, remove head to make more space
            self.storage.remove_from_head()
        # Add to tail, which takes in the new item
            self.storage.add_to_tail(item)
            if current_head == self.current:
                self.current = self.storage.tail
        
        # if (self.storage.length == self.capacity):
        #     if (self.current.next is not None):
        #         self.current.value = item
        #         self.current = self.current.next
        #     elif (self.current.next is None):
        #         self.storage.tail.value = item
        #         self.current = self.storage.head
        # else:
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.head
        #     self.storage.length += 1
        # if self.storage.length == self.capacity:
        #     remove = self.storage.head
        #     self.storage.remove_from_head()
        #     self.storage.add_to_tail(item)
        #     if remove == self.current:
        #         self.current = self.storage.tail
        #     elif self.storage.length < self.capacity:
        #         self.storage.add_to_tail(item)
        #         self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        my_node = self.current
        list_buffer_contents.append(my_node.value)
        if my_node.next is not None:
            node = my_node.next
        else:
            node = self.storage.head
        # looping through each node and appending the values
        while node is not my_node:
            list_buffer_contents.append(node.value)
            if node.next is not None:
                node = node.next
            else:
                node = self.storage.head
        
        return list_buffer_contents

        # if self.storage.length == 0:
        #     return 'Nothing'
        # my_node = self.current
        # list_buffer_contents.append(my_node.value)
        # if my_node.next:
        #     nxt = my_node.next
        # else:
        #     nxt = self.storage.head
        # while nxt != my_node:
        #     list_buffer_contents.append(nxt.value)
        #     if nxt.next:
        #         nxt = nxt.next
        #     else:
        #         nxt = self.storage.head

        # TODO: Your code here


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
