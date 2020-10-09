def fibonacci_tree_inorder(n):
    if n == 1 or n == 2:
        print(n, end=" ")
        return
    if n == 0 or n == -1:
        return
    fibonacci_tree_inorder(n - 2)
    print(n, end=" ")
    fibonacci_tree_inorder(n - 1)

fibonacci_tree_inorder(5)
print()

def fibonacci_tree_preorder(n):
    if n == 1 or n == 2:
        print(n, end=" ")
        return
    if n == 0 or n == -1:
        return
    print(n, end=" ")
    fibonacci_tree_preorder(n - 2)
    fibonacci_tree_preorder(n - 1)

fibonacci_tree_preorder(5)
print()

def fibonacci_tree_postorder(n):
    if n == 1 or n == 2:
        print(n, end=" ")
        return
    if n == 0 or n == -1:
        return
    fibonacci_tree_postorder(n - 2)
    fibonacci_tree_postorder(n - 1)
    print(n, end=" ")

fibonacci_tree_postorder(5)
print()

