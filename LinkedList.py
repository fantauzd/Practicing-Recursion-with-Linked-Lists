# Author:  Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 11/13/2023
# Description: Defines a LinkedList class with recursive implementations of the add, remove, contains, insert,
# and reverse methods from the Exploration. Also defines a recursive to_plain_list function that takes no parameters
# and returns a regular Python list that has the same values in the same order, as the current state of the linked list


class Node:
    """
    Represents a node in a linked list. Trivial class with no interface.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT, which contains nodes for each value.
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        """
        Returns the head (first node) of the Linked List
        :return: first node
        """
        return self._head


    def add(self, val, current_node=None, next_node=None):
        """
        Adds a node containing val to the linked list using recursion
        """
        if self._head is None:  # If the list is empty, we add it as head
            self._head = Node(val)
            return

        if current_node is None:  # Initialize current node and next node
            current_node = self._head
            next_node = current_node.next

        if next_node is None:  # True when current node is the last node in the linked list
            current_node.next = Node(val)
            return

        else:
            return self.add(val, next_node, next_node.next)  # moves current node and next node forward


    def display(self):
        """
        Prints out the values in the linked list on the same line, space separated
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


    def remove(self, val, previous_node=None, current_node=None):
        """
        Removes the node containing val from the linked list using recursion
        """
        if self._head is None:  # If the list is empty, we have nothing to remove
            return
        # if the node to remove is the head
        if self._head.data == val:
            if self._head.next is not None:  # and if there is another node
                self._head = self._head.next
                return
            self._head = None  # if the node to remove is head, and it is also the only node in the linked list
            return

        if previous_node is None:  # initialize previous node and current node
            previous_node = self._head  # we call it previous node because we know the head is not the val to remove
            current_node = self._head.next

        if current_node.data == val:  # True when current node is the node we ant to remove
            previous_node.next = current_node.next
            return

        if current_node.next is None:  # True when we are out of nodes to check
            return
        # moves previous node and current node forward
        return self.remove(val, current_node, current_node.next)


    def contains(self, val, current_node=None):
        """
        Return true if value is in list, false otherwise, think of this like a search function that returns true/false
        :param current_node: current node being examined by function
        :param val: value we are searching for in linkedlist
        :return: Boolean value
        """
        #         Note - We cannot implement binary search as we don't have  quick access to elements of a linked list.
        #         Thus, we are forced to use linear search O(N). We can reduce time by half by ordering the list
        #         and stopping the search after reaching greater values.
        #         However, I do not know if our data types will be consistent or if the tests are structured for this.

        if self._head is None:  # if we have an empty list
            return False
        if current_node is None:  # initialize current node
            current_node = self._head

        if current_node.data == val:  # true when we have found the val in our linked list
            return True

        if current_node.next is None:  # true when we have not found the val and we have nothing left to check
            return False

        else:
            return self.contains(val, current_node.next) and True


    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None


    def insert(self, val, pos, pos_counter=0, current_node=None):
        """
        takes as parameters a value and a position (in that order). A position of zero means that the new value will
        become the new first element. A position of one means it will become the new second element, etc.
        A position >= the length of the list means it will be added at the end of the list.
        :param current_node: current node being examined by the function
        :param pos_counter: counter to track the current position being examined
        :param val: value of node
        :param pos: position in linked list to add to
        :return: None
        """
        if self._head is None:  # if the list is empty
            self.add(val)
            return
        if pos == 0:  # if we want to add a new head
            old_head = self._head
            self._head = Node(val)
            self._head.next = old_head
            return

        if current_node is None:  # initialize current and next node
            current_node = self._head
        # We use pos_counter + 1 because we are inserting after current node so pos should be 1 greater than pos_counter
        # if we have reached the correct position to insert node after current value, or if we reached the last node
        if pos == (pos_counter + 1) or current_node.next is None:
            temp = current_node.next
            current_node.next = Node(val)
            current_node.next.next = temp
            return

        else:
            return self.insert(val, pos, pos_counter + 1, current_node.next)


    def reverse(self, current_node=None, next_node=None):
        """
        Reverses the order of the nodes in the linked list by changing the next value each node holds
        :return: None
        """
        if self._head is None or self._head.next is None:
            return
        if current_node is None:
            current_node = self._head
            next_node = current_node.next

        if next_node is None:  # once we reach last node, next becomes none
            self._head = current_node  # time to set our new head
            return
        # save current and next node as we go down recursion, so we can reverse them later
        node_prev = current_node
        next_to_reverse = next_node

        self.reverse(next_node, next_node.next)  # moves to next node until at current node is the last node
        next_to_reverse.next = node_prev  # executes on way back out of recursion, reversing linked list
        next_to_reverse.next.next = None
        return

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def to_plain_list(self, current_node=None, next_node=None, plain_list=None):
        """
        Takes no parameters and returns a regular Python list that has the same values,
        in the same order, as the current state of the linked list.
        :param current_node: current node the function is on
        :param next_node: next node the function will examine
        :param plain_list: a list for storage and return
        :return: the plain list version of the linked list
        """
        if plain_list is None:  # initialize plain list for storage
            plain_list = []

        if self._head is None:  # if linked list has no nodes
            return plain_list

        if current_node is None:  # initialize current and next node
            current_node = self._head
            next_node = self._head.next

        if next_node is None:  # when we are on last node, we must append the current_node's data before returning list
            plain_list.append(current_node.data)
            return plain_list
        else:  # appends item on thew way down to avoid overwriting
            plain_list.append(current_node.data)
            return self.to_plain_list(next_node, next_node.next, plain_list)


#-------------------------------------------------------
listy = LinkedList()
listy.add(1)
listy.add(2)
listy.add(3)
listy.add(4)
listy.display()
listy.insert(5,15)
listy.display()

listy2 = LinkedList()
listy2.add(1)
listy2.add(2)
listy2.add(3)
listy2.add(4)
listy2.display()
listy2.reverse()
listy2.display()