''''''
'''
이진 검색 트리 준다 -> 그 트리의 루트 가지고 와
그 트리 키  + 걔보다 큰 키들의 합

1. 노드 왼쪽: 노드보다 작은 키
2. 노드 오른쪽: 노드보다 큰 키

'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, root=0, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class Solution(object):
    def bstToGst(self, root):
        self._reverseInorder(root, 0)
        return root

    def _reverseInorder(self, node, sumSoFar):
        if node:
            sumSoFar = self._reverseInorder(node.right, sumSoFar)
            sumSoFar += node.val
            node.val = sumSoFar
            sumSoFar = self._reverseInorder(node.left, sumSoFar)
            return sumSoFar
        return sumSoFar
