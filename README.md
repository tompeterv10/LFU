# LFU

# Data Structures used are the following:
Dictionary - Cache uses dictionary to store the nodes in doubly linkedlist as values for every key that is added to the cache.
Frequency Map - A dictionary is used to store the all the frequency values generated on each call of cache. Key is the frequency and values are doubly linked list consisting of nodes which are the key, value pairs added to cache.

Time Complexity - O(1) and Space complexity - O(K) - K be the capacity of cache.

# Unit Test Results
PS C:\Users\tom\Documents\GitHub\LFU\src> py -m pytest .\take_home\implementation_tests\test_lfu.py
===================================================================== =====================================================================
platform win32 -- Python 3.8.5, pytest-5.3.5, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\tom\Documents\GitHub\LFU\src
plugins: cov-3.0.0
collected 5 items

take_home\implementation_tests\test_lfu.py .....                                                                                                          [100%]

====================================================================== 5 passed in 0.12s =======================================================================

# Test Coverage report

PS C:\Users\tom\Documents\GitHub\LFU\src> py -m pytest --cov-report term-missing --cov=.\take_home\implementation
===================================================================== test session starts ======================================================================
platform win32 -- Python 3.8.5, pytest-5.3.5, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\tom\Documents\GitHub\LFU\src
plugins: cov-3.0.0
collected 5 items

take_home\implementation_tests\test_lfu.py .....                                                                                                          [100%]

----------- coverage: platform win32, python 3.8.5-final-0 -----------
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
take_home\implementation\__init__.py       0      0   100%
take_home\implementation\lfu.py           63      0   100%
--------------------------------------------------------------------
TOTAL                                     63      0   100%


====================================================================== 5 passed in 0.26s ======================================================================= 





