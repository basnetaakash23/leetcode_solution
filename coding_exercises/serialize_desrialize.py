import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
# def creatBTree(data, index):
#     pNode = None
#     if index < len(data):
#         if data[index] == None:
#             return
#         pNode = TreeNode(data[index])
#         pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
#         pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
#     return pNode 

def createBTree(data):
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = collections.deque([tree])
    while True:
        head = fringe.popleft()
        try:
            head.left = TreeNode(next(n))
            fringe.append(head.left)
            head.right = TreeNode(next(n))
            fringe.append(head.right)
            
        except StopIteration:
            break
    return tree

lst = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
root = createBTree(lst)
# lst1 = [1,2]
# root1 = creatBTree(lst1, 0)

def serialize(root):
    q = collections.deque([root])
    string = []
    while q:
        node = q.popleft()
            
        if node is None: 
            string.append("#")
        else:
            string.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

    return (string)   
    return ",".join(string)

    ans = []
    def dfs(node):
        if node == None:
            ans.append('#')
            return
        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans
    # q = [root]
    # # s = ""
    # s = []

    # while(q):
    #     arr = []
    #     for node in q:
            
    #         if(node == "*"):
    #             s.append("*")
    #             continue

    #         s.append(node.val)
    #         if(node.left):
    #             arr.append(node.left)

    #         else:
    #             arr.append("*")

    #         if(node.right):
    #             arr.append(node.right)

    #         else:
    #             arr.append("*")

    #     # print(arr)
    #     q = arr

    # return s


def deserialize(data):
    # if not data: return 

    # qTokens = collections.deque(data)
    # root = TreeNode(qTokens.popleft())

    # qNodes = collections.deque([root])
        
    # while qNodes:
    #     node = qNodes.popleft()
            
    #     left = qTokens.popleft()
    #     right = qTokens.popleft()
            
    #     if left:
    #         node.left = TreeNode(left)    
    #         qNodes.append(node.left)

    #     if right:
    #         node.right = TreeNode(right)    
    #         qNodes.append(node.right)

    # return root
    # # data = collections.deque(s)
    # # def dfs():
    # #     if data:
    # #         i = data.popleft()
    # #     else: return None
    # #     if i is '#': return None
    # #     node = TreeNode(str(i))
    # #     node.left = dfs()
    # #     node.right = dfs()
    # #     return node
    # # return dfs()
    # # print(" ", len(s))
    root = TreeNode(int(data[0]))
    q = collections.deque([root])
    tree_nodes = collections.deque(data[1:])
    while q:
        node = q.popleft()
        left = tree_nodes.popleft()
        right = tree_nodes.popleft()
        if(left!="#"):
            node.left = TreeNode(left)
            q.append(node.left)

        if(right!="#"):
            node.right = TreeNode(right)
            q.append(node.right)

    return root
#         print("Start",index)
#         for node in q:
#             q.pop(0)
            
#             try:
#                 if(s[index] == "*"):
#                     node.left = None
#                     index += 1
#                     #print(index)

#                 else:
#                     node.left = TreeNode(int(s[index]))
#                     arr.append(node.left)
#                     index += 1
#                     #print(index)

#                 if(s[index] == "*"):
#                     node.right = None
#                     index += 1
#                     #print(index)

#                 else:
#                     node.right = TreeNode(int(s[index]))
#                     arr.append(node.right)
#                     index +=1
#             except:
#                 return root

#         # print("End:",index)
#         q.extend(arr)
#     return root

# # print(serialize(root))
def level_order(r):
    q = [r]
    while(q):
        arr = []
        for node in q:
            print(node.val)
            if(node.left):
                arr.append(node.left)

            if(node.right):
                arr.append(node.right)

        q = arr
level_order(deserialize(serialize(root)))



def inorder_traversal(r):
    if r:
        inorder_traversal(r.left)
        print(r.val)
        inorder_traversal(r.right)




print("***")
# l = deserialize("123**45")
# level_order(l)
#inorder_traversal(l)
#print(inorder_traversal(deserialize("123**45")))

   