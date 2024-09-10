from container import PriorityQueue
from hypothesis import given
from hypothesis.strategies import integers, lists

def test_add_normal_num() -> None:
    """Testing priority queue on a normal set of inputs."""
    pq = PriorityQueue()
    pq.add(1)
    pq.add(-2)
    pq.add(32)
    pq.add(-322)
    assert pq._items == [-322, -2, 1, 32]
    
def test_add_normal_str() -> None:
    """Testing priority queue on a normal set of inputs."""
    pq = PriorityQueue()
    pq.add('a')
    pq.add('b')
    pq.add('c')
    pq.add('a')
    assert pq._items == ['a', 'a', 'b', 'c']

def test_add_same_num() -> None:
    """Testing priority queue with same input."""
    pq = PriorityQueue()
    first = 1
    second = 1
    third = 1
    pq.add(first)
    pq.add(second)
    pq.add(third)
    pq.add(-10)
    pq.add(10)
    assert pq._items == [-10, first, second, third, 10]

@given(lists(integers(), min_size=1, max_size=100))
def test_add_many(items: list[int]) -> None:
    """Testing priority queue with many inputs."""
    pq = PriorityQueue()
    for item in items:
        pq.add(item)

    first = pq.remove()
    while not pq.is_empty():
        assert first <= pq.remove()

if __name__ == '__main__':
    import pytest
    pytest.main(['test_container.py'])