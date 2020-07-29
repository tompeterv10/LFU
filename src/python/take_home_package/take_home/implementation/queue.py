# Copyright (c) Docugami, Inc. All rights reserved.

from take_home.base.base_queue import BaseQueue

class Queue(BaseQueue):
    ''' Abstract base class for queue implementations. '''
    def __init__(self, max_in_memory: int):
        super().__init__(max_in_memory)
        raise NotImplementedError()

    @property
    def count(self) -> int:
        raise NotImplementedError()

    @property
    def in_memory_count(self) -> int:
        raise NotImplementedError()

    @property
    def on_disk_count(self) -> int:
        raise NotImplementedError()

    def enqueue(self, value):
        raise NotImplementedError()

    def dequeue(self) -> object:
        raise NotImplementedError()

    def peek(self) -> object:
        raise NotImplementedError()
