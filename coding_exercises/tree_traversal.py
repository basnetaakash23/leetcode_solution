class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printInOrderTraversal(root):
    if(not root):
        return

    else:
        printInOrderTraversal(root.left)

        print(root.val)

        printInOrderTraversal(root.right)

def treetraversal(arr,root):
    if not root:
        return
    
    else:
        treetraversal(arr, root.left)
        arr.append(root.val)
        treetraversal(arr, root.right)

def isValidBST(root):
    arr = []

    treetraversal(arr, root)

    if(len(arr)==1):
        return True

    for x in range(0, len(arr)-1):
        print("Val",arr[x])
        if(arr[x+1]<arr[x]):
            return False

    return True









if __name__ == "__main__":
    n = Node(2)
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(9)
    n4 = Node(6)
    n5 = Node(7)
    # n3.left = n1
    # n3.right = n4
    # n1.left = n
    # n1.right = n2
    # n4.right = n5
    printInOrderTraversal(n3)
    print(isValidBST(n3))

