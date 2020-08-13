# Copyright (c) Docugami, Inc. All rights reserved.

from take_home.base.base_queue import BaseQueue


class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class Queue(BaseQueue):
    ''' Abstract base class for queue implementations. '''

    def __init__(self, max_in_memory: int):
        super().__init__(max_in_memory)
       
        self.head = None
        self.tail = None
        self._in_memory_count = 0
        self._on_disk_count = 0


    @property
    def count(self) -> int:
        return self._in_memory_count + self._on_disk_count

    @property
    def in_memory_count(self) -> int:
        return self._in_memory_count
        

    @property
    def on_disk_count(self) -> int:
        return self._on_disk_count


    def peek(self) -> object:
        """Returns the value of head node, or first item in queue without updating the queue."""
        
        # if queue is empty we return None
        if self.count == 0:
            return None
        
        return self.head.value


    def enqueue(self, value):

        # first node is added as head and tail.
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
            self._in_memory_count += 1
        else:

            # if in memory is full, then we write to disk
            if self.max_in_memory == self.in_memory_count:

                # write to disk
                file = open("test.txt", "a")
                file.write(str(value)+"\n")
                file.close()
                self._on_disk_count += 1
            else:
                # write to in_memory
                newNode = Node(value)
                self.tail.next = newNode
                self.tail = newNode
                self._in_memory_count += 1


    def dequeue(self) -> object:

        # if queue is empty raise exception
        if self.count == 0:
            raise Exception("Queue is empty")

        # if head node is not null, dequeue
        if self.head:
            return_val = self._dequeue_memory()

        return return_val


    def _dequeue_memory(self) -> object:
        """dequeues from in memory """

        # always return the head node from memory
        return_val = self.head.value
        self.head = self.head.next
        self._in_memory_count -= 1

        # if we have space in memory, we move node from disk to in_memory
        if self.in_memory_count < self.max_in_memory:
            # dequeue from disk and enqueue to memory
            if self.on_disk_count > 0:
                value_from_disk = self._dequeue_disk()
                self.enqueue(value_from_disk)

        return return_val


    def _dequeue_disk(self) -> object:
        """ Dequeues from disk."""

        f = open('test.txt', 'r+')
        return_val = int(f.readline())
        data = f.read()
        f.seek(0)
        f.write(data)
        f.truncate()
        f.close()
        self._on_disk_count -= 1
        return return_val
