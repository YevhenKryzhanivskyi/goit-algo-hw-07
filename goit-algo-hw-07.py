class Node:
    """Вузол двійкового дерева пошуку."""
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Вставляє новий ключ у BST."""
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    """Пошук ключа у BST. Повертає вузол або None."""
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)

    return search(root.right, key)


def find_max(root):
    """Повертає найбільше значення у BST."""
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.val


# Тест
if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    # Пошук значення
    value_to_find = 4
    result = search(root, value_to_find)

    if result:
        print(f"У дереві знайдено значення {result.val}")
    else:
        print(f"У дереві не знайдено значення {value_to_find}")

    # Пошук максимального значення
    max_value = find_max(root)
    print(f"Найбільше значення у дереві: {max_value}")