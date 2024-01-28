def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def create_complete_binary_tree(arr):
    n = len(arr)
    root = None
    return insert_level_order(arr, root, 0, n)