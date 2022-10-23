import sys
import pytest


def findPairs(arr, target):
    arr.sort()
    start, end = 0, len(arr) -1
    result = []
    while start < end:
        p_sum = arr[start] + arr[end]
        if p_sum > target:
            end -=1
        elif p_sum < target:
            start +=1
        else: 
            result.append((arr[start], arr[end]))
            start +=1
            end -=1
    return result



def test_valid_input():
    assert set(findPairs([3,3,3,3,2,8,9,2,6,2,16,1,2,5,5,7,2,12,-2],10)) == set([(-2, 12), (1, 9), (2, 8), (3, 7), (5, 5)])


def test_invalid_input():
    assert set(findPairs([3,3,3],9)) != set([(3,3,3)])


def test_empty_input():
    assert set(findPairs([],10)) == set([])


def tests_runner():
    test_valid_input()
    test_invalid_input()
    test_empty_input()



arg_array = []
if len(sys.argv)==3:
    for elem in sys.argv[1].split(","):
        arg_array.append(int(elem))
    print('Result:', findPairs(arg_array, int(sys.argv[2])))
else:
    print('Program requires 2 arguments (arr, target).')