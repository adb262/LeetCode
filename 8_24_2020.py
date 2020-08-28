class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(self, head: ListNode) -> ListNode:
    """
    Given a singly linked list, group all odd nodes together 
    followed by the even nodes. Please note here we are talking about 
    the node number and not the value in the nodes.

    You should try to do it in place. 
    The program should run in O(1) space complexity and O(nodes) time complexity.
    """
    if not head or not head.next:
        return head
    llO = ListNode(head.val)
    n = head.next
    llE = ListNode(n.val)
    original = llE
    current = n.next
    n = False
    originalO = llO

    while current:
        temp = current.next
        if not n:
            llO.next = current
            llO = current
        else:
            llE.next = current
            llE = current
        current = temp
        n = not n

    if llE.next:
        llE.next = None
    if llO.next:
        llO.next = None
    llO.next = original

    return originalO


def searchRange(nums, target):
    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].
    """
    if not nums:
        return [-1, -1]
    pointer = len(nums) // 2
    res = set()

    def rightSearch(nums, target):
        index = 0
        result = []
        while index < len(nums):
            if nums[index] > target:
                break
            if nums[index] == target:
                result.append(index)
            index += 1
        return result

    def leftSearch(nums, target, index):
        result = []
        while index >= 0:
            if nums[index] < target:
                break
            if nums[index] == target:
                result.insert(0, index)
            index -= 1
        return result

    resRight = list(map(lambda x: x + pointer + 1,
                        rightSearch(nums[pointer+1:], target)))
    resLeft = leftSearch(nums[:pointer+1], target, pointer)
    res = resLeft + resRight
    return [res[0], res[-1]] if res else [-1, -1]


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    while left < right:
        mid = left + ((right - left) // 2)
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left
