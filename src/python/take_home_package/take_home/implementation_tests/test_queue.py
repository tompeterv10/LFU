''' Copyright (c) Docugami, Inc. All rights reserved. '''
import pytest
from take_home.implementation.queue import Queue

def test_enqueue_and_dequeue():
    ''' Tests enqueue and dequeue. '''

    queue = Queue(2)
    queue.enqueue(1)
    assert queue.peek() == 1
    assert queue.count == 1
    assert queue.in_memory_count == 1

    queue.enqueue(2)
    assert queue.peek() == 1
    assert queue.count == 2
    assert queue._max_in_memory == 2
    assert queue.in_memory_count == 2

    queue.enqueue(3)
    assert queue.peek() == 1
    assert queue.count == 3
    assert queue._on_disk_count == 1
    assert queue._max_in_memory == 2

    val = queue.dequeue()
    assert queue.count == 2
    assert val == 1
    val = queue.dequeue()
    assert queue.count == 1
    assert val == 2
    val = queue.dequeue()
    assert queue.count == 0
    assert val == 3

    with pytest.raises(Exception) as error_info:
        queue.dequeue()
    assert str(error_info.value) == "Queue is empty"


def test_dequeue_on_disk():
    ''' Tests dequeue operation of a disk backed queue.. '''

    # add values to the queue
    queue = Queue(2)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.on_disk_count == 2
    assert queue.max_in_memory == 2
    assert queue.count == 4

    # dequeue
    val = queue.dequeue()
    assert val == 1
    assert queue.in_memory_count == 2 
    assert queue.on_disk_count == 1
    assert queue.count == 3

    val = queue.dequeue()
    assert val == 2
    assert queue.in_memory_count == 2 
    assert queue.on_disk_count == 0
    assert queue.count == 2

    val = queue.dequeue()
    assert val == 3
    assert queue.in_memory_count == 1 
    assert queue.on_disk_count == 0
    assert queue.count == 1

    val = queue.dequeue()
    assert val == 4
    assert queue.in_memory_count == 0 
    assert queue.on_disk_count == 0
    assert queue.count == 0

    # tear down clear the file
    file = open("test.txt","w")
    file.close()


def test_peek():
    """ Tests the peak function of queue. """ 

    # Tests the
    queue = Queue(2)
    queue.enqueue(1)
    assert queue.peek() == 1

    val = queue.dequeue()
    assert val == 1
    assert queue.peek() == None
    