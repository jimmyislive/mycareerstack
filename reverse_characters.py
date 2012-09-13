
"""
Given a linked list containing characters that form a string such as

--------- "my career stack" ---------
Reverse the characters of each word, keeping the order of the words same such 
that the output will be

--------- "ym reerac kcats" ---------

*******************************************************
logic to swap a word: keep swapping adjacent ones until u reach the end. repeat 
n times.

note: this is a simgly linked list, so no back pointers.

stack
tsack
tasck
tacsk
tacks => s

tack
atck
actk
ackt => t

ack
cak
cka => a

ck
kc => c

k => k

kcats
"""

import random

#for convenience lets just assume there are a max of 1000 nodes in the linked 
#list (logic easily be changed to accomodate max memory size)

MEMORY = range(1000)

class Node(object):

    def __init__(self, char):
        self.char = char
        self.next = None

class LinkedList(object):

    def __init__(self, string):
        self.head = None
        self.tail = None
        self.store = {}

        self._init(string)

    def _init(self, string):
        """Create the LL given a string."""

        for char in string:
            self.push(char)

    def push(self, char):
        node = Node(char)
        index = random.choice(MEMORY)
        self.store[index] = node

        if not self.head:
            self.head = self.tail = index
        else:
            self.store[self.tail].next = index
            self.tail = index

        MEMORY.remove(index)

    def reverse(self):
        running_ptr = self.head
        while (running_ptr):

            #if it's a space, skip it
            while not self.store[running_ptr].char.strip():
                running_ptr = self.store[running_ptr].next

            #get the word boundary
            wordboundary_ptr  = running_ptr
            word_len = 1
            while self.store[wordboundary_ptr].next and self.store[self.store[wordboundary_ptr].next].char.strip():
                wordboundary_ptr = self.store[wordboundary_ptr].next
                word_len += 1

            swap_ptr = prev_ptr = running_ptr
            end_ptr = wordboundary_ptr

            for i in range(word_len - 1):
                while swap_ptr != end_ptr:
                    tmp = self.store[swap_ptr].char
                    self.store[swap_ptr].char = self.store[self.store[swap_ptr].next].char
                    self.store[self.store[swap_ptr].next].char = tmp

                    prev_ptr = swap_ptr
                    swap_ptr = self.store[swap_ptr].next

                end_ptr = prev_ptr
                swap_ptr = running_ptr

            running_ptr = self.store[wordboundary_ptr].next

    def __str__(self):
        str = []
        ptr = self.head
        while (ptr):
            str.append(self.store[ptr].char)
            ptr = self.store[ptr].next

        return ''.join(str)

if __name__ == '__main__':

    sentence = LinkedList("my career stack")
    assert str(sentence) == "my career stack"
    sentence.reverse()
    assert str(sentence) == "ym reerac kcats"

    sentence = LinkedList("hello world")
    assert str(sentence) == "hello world"
    sentence.reverse()
    assert str(sentence) == "olleh dlrow"

