'''
1. 이진트리 노드 개수 입력
2. 루트-왼쪽-오른쪽 노트 주어진다 N줄 만큼
3. 전위 > 중위 > 후위 차례대로 결과 출력
4. 루트는 항상 A
'''
import sys
input = sys.stdin.readline

# 1. 이진 트리 노드의 개수가 주어진다
N = int(input())

tree = {}
for n in range(N):
    # 2. N줄에 걸쳐서 각 노드, 왼쪽 노드, 오른쪽 노드 주어진다.
    root, left, right = input().split()
    tree[root] = [left, right]

# 3. 전위 순회 preorder (루트-왼쪽-오른쪽)
def preorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        print(root, end='')
        preorder(left)
        preorder(right)

# 4. 중위 순회 inorder (왼쪽-루트-오른쪽)
def inorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        inorder(left)
        print(root, end='')
        inorder(right)

# 5. 후위 순회 postorder (왼쪽-오른쪽-루트)
def postorder(root):
    if root != '.':
        left = tree[root][0]
        right = tree[root][1]
        postorder(left)
        postorder(right)
        print(root, end='')

# 6. A가 항상 루트 노드
preorder('A')
print()
inorder('A')
print()
postorder('A')
