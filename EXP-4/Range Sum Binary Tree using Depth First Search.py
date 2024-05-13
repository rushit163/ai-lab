# ITERATIVE APPROACH 
class Solution(object): 
 def rangeSumBST(self, root, L, R): 
 def dfs(node): 
 if node: 
 if L <= node.val <= R: 
 self.ans += node.val 
 if L < node.val: 
26
 dfs(node.left) 
 if node.val < R: 
 dfs(node.right) 
 self.ans = 0 
 dfs(root) 
 return self.ans 
# RECURSIVE APPROACH 
class Solution(object): 
 def rangeSumBST(self, root, L, R): 
 ans = 0 
 stack = [root] 
 while stack: 
 node = stack.pop() 
 if node: 
 if L <= node.val <= R: 
 ans += node.val 
 if L < node.val: 
 stack.append(node.left) 
 if node.val < R: 
 stack.append(node.right) 
 return ans 


bst = TreeNode(10) 
bst.left = TreeNode(5) 
bst.right = TreeNode(15) 
bst.left.left = TreeNode(3) 
bst.left.right = TreeNode(7) 
bst.right.right = TreeNode(18) 
min = int(input("Enter the Lower value of the range : ")) 
max = int(input("Enter the Higher value of the range : ")) 
sol = rangeSumBST(bst, min, max) 
print(f"The sum of the nodes in the range {min} and {max} is {sol}") 

