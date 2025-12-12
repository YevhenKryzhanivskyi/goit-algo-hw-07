class Node:
    # Клас, що представляє вузол у бінарному дереві пошуку (BST).

    def __init__(self, key: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.val: int = key


def insert(node: Node | None, key: int) -> Node:
    # Вставляє новий ключ у BST. Повертає корінь дерева.
    if node is None:
        return Node(key)

    if key < node.val:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def search(node: Node | None, key: int) -> Node | None:
    if node is None or node.val == key:
        return node

    if key < node.val:
        return search(node.left, key)

    return search(node.right, key)


def find_max(node: Node | None) -> int | None:
    # Повертає найбільше значення у BST або None, якщо дерево порожнє.
    if node is None:
        return None

    current = node
    while current.right is not None:
        current = current.right

    return current.val


def find_min(node: Node | None) -> int | None:
    # Повертає найменше значення у BST або None, якщо дерево порожнє.
    if node is None:
        return None

    current = node
    while current.left is not None:
        current = current.left

    return current.val


def sum_bst(node: Node | None) -> int:
    # Повертає суму всіх значень у BST.
    if node is None:
        return 0
    return node.val + sum_bst(node.left) + sum_bst(node.right)


if __name__ == "__main__":
    # Побудова дерева
    root: Node | None = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    # Пошук значення
    value_to_find = 4
    result = search(root, value_to_find)

    if result is not None:
        print(f"У дереві знайдено значення {result.val}")
    else:
        print(f"У дереві не знайдено значення {value_to_find}")

    # Пошук максимального значення
    max_value = find_max(root)
    print(f"Найбільше значення у дереві: {max_value}")

    # Пошук мінімального значення
    min_value = find_min(root)
    print(f"Найменше значення у дереві: {min_value}")

    # Сума всіх значень
    total_sum = sum_bst(root)
    print(f"Сума всіх значень у дереві: {total_sum}")
