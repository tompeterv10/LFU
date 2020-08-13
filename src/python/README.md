# Python Take Home Question

Disk Backed Queue written in python

## Design Choices
1.  A linked list node is used to track each value of queue in memory.
    Enqueue operation adds the value next to the tail of linkedlist.
    Dequeue operation changes the head to point to next value in linkedlist

2. Once the in-memory is full, values are added to a file (disk storage).
    For the purpose of implementation it is assumed that all values will be integers.

3. For Dequeue operation once the in memory count is less than max in   memory count we pop out from disk storage (or file) by reading the value and enqueue it to the inmemory. We use existing enqueue operation to add it in inmemory. This maintains recent nodes in memory at all points(FIFO)

## External resources

1. File api related syntax https://docs.python.org/3/tutorial/inputoutput.html


## Time Taken

1. It took around 2.5 hours to 3 hours to implement the changes and tests for the project.

2. Test cases covered include tests for enqueue and dequeue operations. Negative case in which dequeue returns exception. Verified total count, memory count, and on diskcount is as expected in each stage of enqueue and dequeue operation. Assert statements to ensure peek returns as expected and returns null when queue is empty.


Test Coverage 

```
platform win32 -- Python 3.8.5, pytest-5.3.5, py-1.9.0, pluggy-0.13.1
rootdir: C:\Users\tpeter\Documents\GitHub\TakeHome-TomPeter\src\python\take_home_package
plugins: cov-2.10.0
collected 3 items

test_queue.py ...                                                                                                                                                                                                              [100%]

----------- coverage: platform win32, python 3.8.5-final-0 -----------
Name                                                                                                                  Stmts   Miss  Cover
-----------------------------------------------------------------------------------------------------------------------------------------
C:\Users\tpeter\Documents\GitHub\TakeHome-TomPeter\src\python\take_home_package\take_home\base\__init__.py                 0      0   100%
C:\Users\tpeter\Documents\GitHub\TakeHome-TomPeter\src\python\take_home_package\take_home\base\base_queue.py              22      0   100%
C:\Users\tpeter\Documents\GitHub\TakeHome-TomPeter\src\python\take_home_package\take_home\implementation\__init__.py       0      0   100%
C:\Users\tpeter\Documents\GitHub\TakeHome-TomPeter\src\python\take_home_package\take_home\implementation\queue.py         64      0   100%
__init__.py                                                                                                               0      0   100%
test_queue.py                                                                                                            68      0   100%
-----------------------------------------------------------------------------------------------------------------------------------------
TOTAL                                                                                                                   154      0   100%


```

