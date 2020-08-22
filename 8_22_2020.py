def pascalsTriangle(numRows: int) -> List[List[int]]:
    """
    Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
    """
    dp = [[1] * x for x in range(1, numRows+1)]
    for index in range(numRows):
        for r in range(len(dp[index])):
            if r and r != index:
                dp[index][r] = dp[index-1][r] + dp[index-1][r-1]
    return dp


def widthOfBinaryTree(root: TreeNode) -> int:
    """
    Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.
    
    The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.
    """
    q = deque()
    q.append((root, 1))
    ans = 1
        
    while q:
        size = len(q)
        ans = max(ans, q[-1][1] - q[0][1] + 1)
        for _ in range(size):
            node, pos = q.popleft()
            
            if node.left:
                q.append((node.left, 2 * pos))
            
            if node.right:
                q.append((node.right, 2 * pos + 1))

    return ans

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Given preorder and inorder traversal of a tree, construct the binary tree.
    
    Note:
    You may assume that duplicates do not exist in the tree.
    """
    if not preorder:
        return
    pos = inorder.index(preorder[0])
    root = TreeNode(preorder[0])
    root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
    root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])
    return root

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
    """
    maxArea = l = 0
    r = len(height) - 1

    while (l < r):
        maxArea = max(maxArea, min(height[l], height[r])*(r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxArea


class BSTIterator:
    """
    Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
    
    Calling next() will return the next smallest number in the BST.
    """
    
    def __init__(self, root: TreeNode):
        self.node = root
        self.listFormat = self.getNodes(root)
        self.index = 0
    
    def getNodes(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root]
        return self.getNodes(root.left) + [root] + self.getNodes(root.right)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.index += 1
            return self.listFormat[self.index-1].val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < len(self.listFormat)


