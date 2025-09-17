import importlib
S = importlib.import_module("arrays.27_remove_element").Solution()

def test_remove_element_basic():
    nums = [3,2,2,3]
    val = 3
    expectedNums = [2,2]
    k = S.removeElement(nums, val)
    assert k == len(expectedNums)
    assert sorted(nums[:k]) == sorted(expectedNums)

def test_remove_element_mixed():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    expectedNums = [0,1,4,0,3]
    k = S.removeElement(nums, val)
    assert k == len(expectedNums)
    assert sorted(nums[:k]) == sorted(expectedNums)

def test_remove_element_none():
    nums = [1,1,1]
    val = 2
    expectedNums = [1,1,1]
    k = S.removeElement(nums, val)
    assert k == len(expectedNums)
    assert sorted(nums[:k]) == sorted(expectedNums)

def test_remove_element_all():
    nums = [2,2,2]
    val = 2
    expectedNums = []
    k = S.removeElement(nums, val)
    assert k == len(expectedNums)
    assert nums[:k] == expectedNums
