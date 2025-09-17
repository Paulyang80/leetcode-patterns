import importlib
S = importlib.import_module("arrays.88_merge_sorted_array").Solution()

def test_merge_basic():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    expected = [1,2,2,3,5,6]
    S.merge(nums1, 3, nums2, 3)
    assert nums1 == expected

def test_merge_empty_nums2():
    nums1 = [1]
    nums2 = []
    expected = [1]
    S.merge(nums1, 1, nums2, 0)
    assert nums1 == expected

def test_merge_empty_nums1():
    nums1 = [0]
    nums2 = [1]
    expected = [1]
    S.merge(nums1, 0, nums2, 1)
    assert nums1 == expected

def test_merge_all_zeros():
    nums1 = [0,0,0,0,0,0]  # 長度要是 m+n
    nums2 = [0,0,0]
    expected = [0,0,0,0,0,0]
    S.merge(nums1, 0, nums2, 3)
    assert nums1 == expected
