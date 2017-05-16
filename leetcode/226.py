'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    '''
    recursive
    O(n)
    '''
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None: return None
        else:
            if root.left != None:
                root.left = self.invertTree(root.left)
            if root.right != None:
                root.right = self.invertTree(root.right)
            root.left, root.right = root.right, root.left
            return root

class Solution:
    '''
    non-recursive
    O(n)
    '''
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root == None: return None
        q = [root]
        while len(q) != 0:
            front = q.pop(0)
            if front.left: q.append(front.left)
            if front.right: q.append(front.right)
            front.left, front.right = front.right, front.left

        return root


if __name__ == '__main__':
    # pass
    # need to construct a binary tree
