# project-7

**For this module and the next one, more test results are visible in Gradescope before the due date than usual, however if you miss any of those, the penalty will be more strict (see the rubric for details).**

Write a LinkedList class that has **recursive** implementations of the `add` and `remove` methods described in the Exploration.  It should also have **recursive** implementations of the `contains`, `insert`, and `reverse` methods described in the exercises.  The reverse method should **not** change the _data_ value each node holds - it must rearrange the order of the nodes in the linked list (by changing the _next_ value each node holds).

It should have a **recursive** method named `to_plain_list` that takes no parameters (unless they have default arguments) and returns a regular Python list that has the same values (from the `data` attribute of the Node objects), in the same order, as the current state of the linked list.

The `head` data member of the LinkedList class must be private and have a get method defined (named get_head), which should return the first Node object in the list (not the value stored inside it).

As in the iterative LinkedList in the exploration, the data members of the Node class don't have to be private.  The reason for that is because Node is a trivial class that contains only two data members and no methods (besides init), so there's not a need for encapsulation.  Another way of putting it is that there's no need to separate interface from implementation because there is no interface (public methods of the class).

All the methods should have the arguments in the same order as you saw in the Lesson. You may use default arguments and/or helper functions. 

Your recursive functions must **not**:
* use any loops
* use any variables declared outside of the function
* use any mutable default arguments (see the Code Style Requirements)

Here's an example of how a recursive version of the display() method from the lesson could be written:
```
    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)
```

All your classes must be in a single file named: **LinkedList.py**
