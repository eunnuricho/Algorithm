import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
candidate = list(map(int, input().split()))

def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    else:
        return binarySearch(arr, target, start, mid - 1)


for target in candidate:
    print(binarySearch(cards, target, 0, len(cards) - 1), end="\n")