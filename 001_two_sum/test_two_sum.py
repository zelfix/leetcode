from typing import List


def gen_lists(nums: List[int]):
    return [nums, nums[::-1]]


def two_sum(nums: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(nums):
        if h.get(target - num) is not None:
            return [i, h.get(target - num)]
        else:
            h[num] = i


def test_two_sum():
    assert two_sum(nums=[2, 7, 11, 15], target=9) in gen_lists([1, 0])
    assert two_sum(nums=[3, 2, 4], target=6) in gen_lists([1, 2])
    assert two_sum(nums=[3, 3], target=6) in gen_lists([0, 1])
