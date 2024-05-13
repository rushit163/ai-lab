class Solution(object):
    def rangeSumBST(self, root, L, R):
        if root == None:
            return 0
        res = 0
        q = [root]
        while q:
            next = []
            for node in q:
                if L <= node.val <= R:
                    res += node.val
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            q = next
        return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right = TreeNode(7)
bst.right.right = TreeNode(18)

min_val = int(input("Enter the Lower value of the range : "))
max_val = int(input("Enter the Higher value of the range : "))

sol = Solution()
result = sol.rangeSumBST(bst, min_val, max_val)

print(f"The sum of the nodes in the range {min_val} and {max_val} is {result}")

