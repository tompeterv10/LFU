import pytest

from take_home.implementation.lfu import LFUCache

def test_empty_cache_get():
    '''Test cache initialized with empty/default capacity'''

    cache = LFUCache()
    with pytest.raises(Exception) as excInfo:
        cache.get("test")
    
    expected_exception = "Key doesn't exist."
    assert str(excInfo.value) == expected_exception
    assert cache.minimumFrequency == 0
    assert cache.cache == {}
    assert cache.frequencyMap == {}


def test_empty_cache_put():
    ''''Test cache's put method initialized with empty capacity'''

    cache = LFUCache()
    with pytest.raises(Exception) as excInfo:
        cache.put("test_key", "test_value")

    expected_exception = "Cache capacity is not initialized."
    assert str(excInfo.value) == expected_exception
    assert cache.minimumFrequency == 0
    assert cache.cache == {}
    assert cache.frequencyMap == {}


def test_cache_reaches_max_capacity():
    cache = LFUCache(1)

    # add first key, value
    cache.put("test_key_1", "test_value_1")
    value = cache.get("test_key_1")
    assert value == "test_value_1"

    # add second key value pair
    cache.put("test_key_2", "test_value_2")
    value = cache.get("test_key_2")
    assert value == "test_value_2"


def test_cache_mixed():
    '''Tests the get and put method of lfu cache.'''

    cache = LFUCache(2)
    cache.put("test_key_1", "test_value_1")
    cache.put("test_key_2", "test_value_2")
    value = cache.get("test_key_1")
    assert value == "test_value_1"

    # adding the key of of type integer
    cache.put(3, "test_value_3")

    # Test test_key_2 to verify it's pushed out of cache.
    with pytest.raises(Exception) as excInfo:
        cache.get("test_key_2")
    expected_exception = "Key doesn't exist."
    assert str(excInfo.value) == expected_exception

    value = cache.get(3)
    assert value == "test_value_3"

    # invalidate test_key_1 by adding a new key value pair
    cache.put("test_key_4", "test_value_4")

    with pytest.raises(Exception) as excInfo:
        cache.get("test_key_1")
    expected_exception = "Key doesn't exist."
    assert str(excInfo.value) == expected_exception

    value = cache.get(3)
    assert value == "test_value_3"

    value = cache.get("test_key_4")
    assert value == "test_value_4"


def test_updated_value_in_cache():

    cache = LFUCache(1)
    # add first key, value
    cache.put("test_key_1", "test_value_1")
    value = cache.get("test_key_1")
    assert value == "test_value_1"

    # new value for key_1
    cache.put("test_key_1", "test_value_1.1")
    value = cache.get("test_key_1")
    assert value == "test_value_1.1"
