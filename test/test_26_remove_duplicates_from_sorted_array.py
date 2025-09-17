import importlib
S = importlib.import_module("arrays.26_remove_duplicates_from_sorted_array").Solution()

def test_remove_duplicates_basic():
    nums = [1,1,2]
    expected = [1,2]
    k = S.removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected

def test_remove_duplicates_long():
    nums = [0,0,1,1,1,2,2,3,3,4]
    expected = [0,1,2,3,4]
    k = S.removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected

def test_remove_duplicates_all_unique():
    nums = [1,2,3,4,5]
    expected = [1,2,3,4,5]
    k = S.removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected

def test_remove_duplicates_all_same():
    nums = [2,2,2,2,2]
    expected = [2]
    k = S.removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected

# def test_remove_duplicates_empty():
#     nums = []
#     expected = []
#     k = S.removeDuplicates(nums)
#     assert k == len(expected)
#     assert nums[:k] == expected
