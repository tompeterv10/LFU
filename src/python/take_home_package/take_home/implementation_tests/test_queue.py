''' Copyright (c) Docugami, Inc. All rights reserved. '''

from take_home.implementation.queue import Queue

def test_peek():
    ''' Simple test of the peek method. '''
    queue = Queue(10)
    queue.enqueue(1)
    assert queue.peek() == 1
